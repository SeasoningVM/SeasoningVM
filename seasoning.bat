@echo off

echo Seasoning Virtual Machine [Version 1.0.0]
echo (c) 2017, Seaoning-Virtual-Machine. BSD 3-Clause.
echo.
echo Type "credits", "license" or "info" for more information. Type "exit" to leave.
echo Type "file" to enter file reader mode or enter "insert" to enter an ASM interpreter mode

set Source=""

:ask
set /p Mode=">>> "

if [%Mode%] == [exit] goto exit
if [%Mode%] == [credits] goto credits
if [%Mode%] == [license] goto license
if [%Mode%] == [info] goto info
if [%Mode%] == [end] goto end
if [%Mode%] == [insert] echo ASM Interpreter Mode & goto interpreter
if [%Mode%] == [file] echo ASM File Reader & goto fileReader
goto ask

:interpreter
set /p Input=">>> "
if "%Input%" == "EOF" goto exit
if "%Input%" == "" goto interpreter
python source.py %Input% "source"
set Input=""
goto interpreter

:filereader
set /p File=">>> "
if "%File%" == "" echo No file entered! & goto filereader
if exist %File% (
    python source.py %File% "file"
) else (
    rem echo This file does not exist.
    set Source=%Source%%File%,
)
goto filereader

:end
set Source=%Source%"
python source.py %Source% "source"
goto ask

:credits
echo Everything: DeflatedPickle
echo Help: assyrianic
goto ask

:license
type LICENSE
goto ask

:info
echo The Seasoning Virtual Machine is a virtual machine designed to support many language implementations.
goto ask

:exit
echo Returning to the world.
