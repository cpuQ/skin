@echo off
setlocal EnableDelayedExpansion

set "input_folder=ununsed"
set "output_folder=unused_amped"
set "amplification_db=16"

for %%F in ("%input_folder%\*.wav") do (
    sox "%%F" "%output_folder%\%%~nF.wav" gain !amplification_db!
)

echo Amplification complete.
endlocal