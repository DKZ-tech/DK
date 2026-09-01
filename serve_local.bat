@echo off
rem =====================================================
rem  DK site local preview (Jekyll)
rem  Ruby installed at E:\Ruby
rem  Preview URL: http://127.0.0.1:4000/DK/
rem =====================================================
cd /d D:\Github_projects\DK
call E:\Ruby\bin\ridk.cmd enable
echo Starting Jekyll server... (Ctrl+C to stop)
call bundle exec jekyll serve
pause
