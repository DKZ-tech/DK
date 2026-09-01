#!/usr/bin/env python3
"""
Batch-optimize images in images/ for the DK academic homepage.

Run from the repository root:
    python scripts/optimize_images.py

What it does:
- GIFs: resize to ~480 px wide, drop every 2nd/3rd frame, keep animation.
- Avatar (profile1.jpg): resize to 400 px wide.
- Other JPEGs: resize to <=1080 px wide, quality 85.
- PNGs: try palette quantization; if JPEG is significantly smaller,
  convert to JPEG and update all Markdown references automatically.
- Skips favicons / site icons.
"""
from PIL import Image
import os
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
IMAGE_DIR = REPO / 'images'

SKIP_NAMES = {
    'favicon.ico', 'favicon.svg', 'manifest.json',
    'apple-touch-icon-180x180.png', 'favicon-32x32.png',
    'favicon-192x192.png', 'favicon-512x512.png',
}


def resize_jpeg(src: Path, dst: Path, max_width: int, quality: int):
    im = Image.open(src)
    if im.mode in ('RGBA', 'P'):
        im = im.convert('RGB')
    w, h = im.size
    if w > max_width:
        im = im.resize((max_width, int(h * max_width / w)), Image.LANCZOS)
    im.save(dst, 'JPEG', quality=quality, optimize=True, progressive=True)


def optimize_png(src: Path, max_width: int):
    """Return (new_path, fmt). May convert PNG -> JPEG if JPEG wins."""
    im = Image.open(src)
    if im.mode == 'RGBA':
        bg = Image.new('RGB', im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        im = bg
    elif im.mode == 'P':
        im = im.convert('RGB')

    w, h = im.size
    if w > max_width:
        im = im.resize((max_width, int(h * max_width / w)), Image.LANCZOS)

    # Try palette PNG
    im_q = im.quantize(colors=128, method=Image.Quantize.MEDIANCUT)
    png_path = src.with_suffix('.png')
    im_q.save(png_path, 'PNG', optimize=True)
    png_size = png_path.stat().st_size

    # Try high-quality JPEG
    jpg_path = src.with_suffix('.jpg')
    im.save(jpg_path, 'JPEG', quality=90, optimize=True, progressive=True)
    jpg_size = jpg_path.stat().st_size

    if jpg_size < png_size * 0.85:
        png_path.unlink(missing_ok=True)
        return jpg_path, 'JPEG'
    else:
        jpg_path.unlink(missing_ok=True)
        return png_path, 'PNG'


def optimize_gif(src: Path, max_width: int = 480, step: int = 3, colors: int = 128):
    im = Image.open(src)
    frames = []
    durations = []
    for i in range(0, getattr(im, 'n_frames', 1), step):
        im.seek(i)
        frame = im.convert('RGB')
        w, h = frame.size
        if w > max_width:
            frame = frame.resize((max_width, int(h * max_width / w)), Image.LANCZOS)
        frame = frame.quantize(colors=colors, method=Image.Quantize.MEDIANCUT)
        frames.append(frame)
        durations.append(im.info.get('duration', 100))

    frames[0].save(
        src, save_all=True, append_images=frames[1:],
        optimize=True, duration=durations, loop=0, disposal=2
    )
    return src


def update_markdown_renames(renames: dict):
    """Update all .md references when a PNG is converted to JPG."""
    if not renames:
        return
    for md in REPO.rglob('*.md'):
        if '_site' in md.parts:
            continue
        text = md.read_text(encoding='utf-8')
        new_text = text
        for old, new in renames.items():
            new_text = re.sub(rf"{re.escape(old)}(?=[\"')\\s]|\Z)", new, new_text)
        if new_text != text:
            md.write_text(new_text, encoding='utf-8')
            print(f"  updated references: {md.relative_to(REPO)}")


def main():
    results = []
    renames = {}

    for entry in sorted(IMAGE_DIR.iterdir()):
        if not entry.is_file():
            continue
        if entry.name.lower() in SKIP_NAMES:
            continue

        orig_size = entry.stat().st_size
        suffix = entry.suffix.lower()

        if suffix == '.gif':
            optimize_gif(entry)
            new_size = entry.stat().st_size
            im = Image.open(entry)
            results.append((entry.name, orig_size, new_size, f"GIF {im.size[0]}px"))

        elif suffix in ('.jpg', '.jpeg'):
            max_w = 400 if entry.name == 'profile1.jpg' else 1080
            quality = 85
            resize_jpeg(entry, entry, max_w, quality)
            new_size = entry.stat().st_size
            results.append((entry.name, orig_size, new_size, f"JPEG {max_w}px"))

        elif suffix == '.png':
            new_path, fmt = optimize_png(entry, max_width=1080)
            new_size = new_path.stat().st_size
            results.append((entry.name, orig_size, new_size, fmt))
            if new_path.suffix == '.jpg' and entry != new_path:
                entry.unlink(missing_ok=True)
                renames[entry.name] = new_path.name

    update_markdown_renames(renames)

    print(f"\n{'File':<25} {'Orig':>10} {'New':>10} {'Format':<14}")
    print("-" * 64)
    total_orig = total_new = 0
    for name, orig, new, fmt in results:
        print(f"{name:<25} {orig/1024:>8.0f}KB {new/1024:>8.0f}KB {fmt:<14}")
        total_orig += orig
        total_new += new
    print("-" * 64)
    print(f"{'TOTAL':<25} {total_orig/1024:>8.0f}KB {total_new/1024:>8.0f}KB")


if __name__ == '__main__':
    main()
