@echo off
cd /d "%~dp0"
if exist "runtime\python.exe" (
  "runtime\python.exe" install.py
) else (
  python install.py
)
if errorlevel 1 (
  echo.
  echo Install Python 3.10 or newer, add it to PATH, then try again.
  pause
)
