@echo off
cls
color b
cd build
pyinstaller --onefile --clean  ../CompileCfg.spec
pause
