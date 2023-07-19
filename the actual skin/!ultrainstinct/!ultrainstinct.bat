@echo off
setlocal

rem set the paths to the two directories
set "dir1=%~dp0.."
set "dir2=%~dp0"

rem find all files in this folder
for %%F in ("%dir1%\*") do (
    rem check if the file exists in skin folder
    if exist "%dir2%\%%~nxF" (
        rem swap files
        echo swapping %%F and %dir2%\%%~nxF...
        move /y "%%F" "%temp%\%%~nxF.tmp" >nul
        move /y "%dir2%\%%~nxF" "%%F" >nul
        move /y "%temp%\%%~nxF.tmp" "%dir2%\%%~nxF" >nul
    )
)

echo files swapped
echo make sure to reload the skin in game!
echo press any key to close...
pause >nul

endlocal
