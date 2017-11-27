@echo off
setlocal EnableDelayedExpansion

echo Seasoning Virtual Machine 1.0.0
echo Type "credits", "license" or "info" for more information. Type "exit" to leave.

:ask
set /p File=">>> "
if [%File%] == [exit] goto exit
if [%File%] == [credits] goto credits
if [%File%] == [license] goto license
if [%File%] == [info] goto info
if [%File%] == [exit] goto exit

python -u source.py %File%

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