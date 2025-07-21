#!/usr/bin/env python3
"""
Code Morningstar Deployment Script
Handles environment setup, dependency installation, and application startup.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, cwd=None, check=True):
    """Run a command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error running command: {cmd}")
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
        sys.exit(1)
    return result

def check_python_version():
    """Ensure Python 3.8+ is available."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("Error: Python 3.8+ is required")
        sys.exit(1)
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")

def setup_virtual_environment():
    """Create and activate virtual environment."""
    venv_path = Path(".venv")
    
    if not venv_path.exists():
        print("Creating virtual environment...")
        run_command(f"{sys.executable} -m venv .venv")
    else:
        print("✅ Virtual environment already exists")
    
    # Return the path to the Python executable in the venv
    if os.name == 'nt':  # Windows
        return venv_path / "Scripts" / "python.exe"
    else:  # Unix-like
        return venv_path / "bin" / "python"

def install_dependencies(python_exe):
    """Install Python dependencies."""
    print("Installing backend dependencies...")
    run_command(f"{python_exe} -m pip install --upgrade pip")
    run_command(f"{python_exe} -m pip install -r backend/requirements.txt")
    print("✅ Dependencies installed")

def setup_environment():
    """Setup environment configuration."""
    env_example = Path("backend/.env.example")
    env_file = Path("backend/.env")
    
    if not env_file.exists() and env_example.exists():
        print("Creating .env file from template...")
        shutil.copy(env_example, env_file)
        print("✅ Environment file created")
        print("📝 Please edit backend/.env to configure your settings")
    elif env_file.exists():
        print("✅ Environment file already exists")
    else:
        print("⚠️ No environment template found")

def run_tests(python_exe):
    """Run the test suite."""
    print("Running tests...")
    result = run_command(f"{python_exe} -m pytest backend/tests/ -v", check=False)
    if result.returncode == 0:
        print("✅ All tests passed")
    else:
        print("⚠️ Some tests failed, but continuing...")

def start_application(python_exe):
    """Start the application."""
    print("Starting Code Morningstar...")
    print("Frontend: Open frontend/standalone.html in your browser")
    print("API Docs: http://localhost:8000/docs")
    print("Health Check: http://localhost:8000/llm/health")
    print("\nPress Ctrl+C to stop the server")
    
    try:
        run_command(f"{python_exe} backend/start.py", check=False)
    except KeyboardInterrupt:
        print("\n👋 Server stopped")

def main():
    """Main deployment function."""
    print("🌟 Code Morningstar Deployment Script")
    print("=" * 40)
    
    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    try:
        check_python_version()
        python_exe = setup_virtual_environment()
        install_dependencies(python_exe)
        setup_environment()
        run_tests(python_exe)
        start_application(python_exe)
    except KeyboardInterrupt:
        print("\n❌ Deployment interrupted")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Deployment failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
