@echo off
setlocal EnableDelayedExpansion

echo Seasoning Virtual Machine 1.0.0
echo Type "credits", "license" or "info" for more information. Type "exit" to leave.

:ask
set /p File=">>> "
echo %File%
if [%File%] == [exit] goto exit

python -u source.py %File%

goto ask

:credits

:license

:info

:exit
echo Returning to the world.