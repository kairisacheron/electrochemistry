@echo off
echo ========================================================
echo Pushing Electrochemistry Master to GitHub...
echo If Git asks you to sign in, please authorize in browser.
echo ========================================================
echo.
cd /d "%~dp0"
git push -u origin main
echo.
echo ========================================================
if %ERRORLEVEL% EQU 0 (
    echo SUCCESS: Repository successfully pushed to GitHub!
    echo Now enable GitHub Pages in your repo settings:
    echo https://github.com/kairisacheron/electrochemistry/settings/pages
) else (
    echo PUSH FAILED: Please check your GitHub authorization.
)
echo ========================================================
pause
