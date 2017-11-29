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
    python source.py %File% "file"
) else (
    echo This file does not exist.
)
goto filereader

:reset
set Source="
goto interpreter

:halt
set Source=%Source%"
python source.py %Source% "source"
goto ask

:credits
echo DeflatedPickle, assyrianic, Dew Wisp
goto ask

:license
type LICENSE
goto ask

:info
echo The Seasoning Virtual Machine is a virtual machine designed to support many language implementations.
goto ask

:exit
echo Returning to the world.
