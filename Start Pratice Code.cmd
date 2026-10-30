@echo off
cd /d "%~dp0"
if exist "runtime\python.exe" (
  "runtime\python.exe" launch.py
) else (
  python launch.py
)
if errorlevel 1 pause
