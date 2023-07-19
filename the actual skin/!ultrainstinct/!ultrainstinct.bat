@echo off
setlocal

rem set the paths to the two files
set "file1=%~dp0..\skin.ini"
set "file2=%~dp0skin.ini"

rem check if both files exist
if not exist "%file1%" (
    echo ERROR: %file1% not found.
    exit /b 1
)
if not exist "%file2%" (
    echo ERROR: %file2% not found.
    exit /b 1
)

rem swap the two files
echo swapping %file1% and %file2%...
move /y "%file1%" "%temp%\skin.tmp" >nul
move /y "%file2%" "%file1%" >nul
move /y "%temp%\skin.tmp" "%file2%" >nul

echo files swapped, press any key to close
pause >nul

endlocal
