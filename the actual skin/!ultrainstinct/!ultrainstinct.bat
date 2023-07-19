@echo off
setlocal

rem Set the paths to the two files
set "file1=%~dp0..\skin.ini"
set "file2=%~dp0skin.ini"

rem Check if both files exist
if not exist "%file1%" (
    echo ERROR: %file1% not found.
    exit /b 1
)
if not exist "%file2%" (
    echo ERROR: %file2% not found.
    exit /b 1
)

rem Swap the two files
echo Swapping %file1% and %file2%...
move /y "%file1%" "%temp%\skin.tmp" >nul
move /y "%file2%" "%file1%" >nul
move /y "%temp%\skin.tmp" "%file2%" >nul

echo Done.
endlocal
