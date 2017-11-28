@echo off

echo Seasoning Virtual Machine [Version 1.0.0]
echo (c) 2017, Seaoning-Virtual-Machine. BSD 3-Clause.
echo/
echo Type "credits", "license" or "info" for more information. Type "exit" to leave.

:ask
set /p Type="Type >>> "
set /p File=">>> "
if [%File%] == [exit] goto exit
if [%File%] == [credits] goto credits
if [%File%] == [license] goto license
if [%File%] == [info] goto info
if [%File%] == [exit] goto exit

python source.py %File% %Type%

goto ask

:credits
echo Everything: DeflatedPickle
goto ask

:license
type LICENSE
goto ask

:info
echo The Seasoning Virtual Machine is a virtual machine designed to support many language implementations.
goto ask

:exit
echo Returning to the world.