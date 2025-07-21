@echo off
REM Code Morningstar Windows Deployment Script
echo 🌟 Code Morningstar Windows Deployment
echo =====================================

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ and try again
    pause
    exit /b 1
)

REM Run the Python deployment script
python deploy.py

REM Keep window open if script fails
if errorlevel 1 (
    echo.
    echo ❌ Deployment failed. Check the error messages above.
    pause
)
