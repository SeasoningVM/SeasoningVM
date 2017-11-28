@echo off

echo Seasoning Virtual Machine [Version 1.0.0]
echo (c) 2017, Seaoning-Virtual-Machine. BSD 3-Clause.
echo/
echo Type "credits", "license" or "info" for more information. Type "exit" to leave.

set Source="

:ask
set /p Insert=">>> "

if [%Insert%] == [exit] goto exit
if [%Insert%] == [credits] goto credits
if [%Insert%] == [license] goto license
if [%Insert%] == [info] goto info
if [%Insert%] == [exit] goto exit

if [%Insert%] == [end] goto end

if exist %Insert% (
    python source.py %Insert% "file"
) else (
    rem echo This file does not exist.

    set Source=%Source%%Insert%,
)

goto ask

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
