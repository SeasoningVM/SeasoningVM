@echo off
echo Seasoning Virtual Machine 1.0.0
echo Type "credits", "license" or "info" for more information.
:ask
set /p File= ">>> "
python -u source.py %File%
goto ask