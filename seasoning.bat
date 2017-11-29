@echo off

echo Seasoning Virtual Machine [Version 1.0.0]
echo (c) 2017, Seaoning-Virtual-Machine. BSD 3-Clause.
echo.
echo Type "credits", "license" or "info" for more information. Type "exit" to leave.
echo Type "file" to enter file reader mode or enter "insert" to enter an ASM interpreter mode

:main
set Source="

:ask
set /p Mode=">>> "

rem Checks for menu commands.
if [%Mode%] == [exit] goto exit
if [%Mode%] == [credits] goto credits
if [%Mode%] == [license] goto license
if [%Mode%] == [info] goto info

if [%Mode%] == [insert] (
    echo ASM Interpreter Mode. Type "leave" to go to main.
    goto interpreter
)

if [%Mode%] == [file] (
    echo ASM File Reader. Type "leave" to go to main.
    goto fileReader
)
goto ask

:interpreter
set /p Input="ASM >>> "

if [%Input%] == [exit] goto exit
if [%Input%] == [reset] goto reset
if [%Input%] == [leave] goto main

if [%Input%] == "" goto interpreter

rem Appends the input and a comma to the source.
set Source=%Source%%Input%,
if [%Input%] == [HALT] goto halt
goto interpreter

:filereader
set /p File="File >>> "

if [%File%] == [exit] goto exit
if [%File%] == [leave] goto main

if "%File%" == "" (
    echo No file entered.
    goto filereader
)

if exist %File% (
    rem Sends the file to the VM with the mode "file".
    python source.py %File% "file"
) else (
    echo This file does not exist.
)
goto filereader

:reset
rem Resets the source.
set Source="
goto interpreter

:halt
rem Finishes off the source by adding the HALT and a quote.
set Source=%Source%"
rem Sends the source to the VM with the mode "source".
python source.py %Source% "source"
goto ask

:credits
echo DeflatedPickle, assyrianic, Dew Wisp
goto ask

:license
rem Types out the license file.
type LICENSE
goto ask

:info
echo The Seasoning Virtual Machine is a virtual machine designed to support many language implementations.
goto ask

:exit
echo Returning to the world.
