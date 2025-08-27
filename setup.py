#!/usr/bin/env python3
"""
Complete setup script for TEDx TrendSpotter embedding system.
This script handles the full initialization process.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"🚀 {title}")
    print('='*60)


def run_command(command, description, check=True):
    """Run a command and handle errors"""
    print(f"\n📋 {description}")
    print(f"Running: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=check, 
                              capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def check_python_requirements():
    """Check if Python and pip are available"""
    print_header("Checking Python Environment")
    
    # Check Python version
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major != 3 or version.minor < 8:
        print("❌ Python 3.8+ is required")
        return False
    
    print("✅ Python version is compatible")
    
    # Check pip
    try:
        import pip
        print("✅ pip is available")
        return True
    except ImportError:
        print("❌ pip is not available")
        return False


def setup_environment():
    """Setup environment file"""
    print_header("Setting up Environment Configuration")
    
    env_example = ".env.example"
    env_file = ".env"
    
    if not os.path.exists(env_example):
        print("❌ .env.example not found")
        return False
    
    if not os.path.exists(env_file):
        print(f"📋 Copying {env_example} to {env_file}")
        shutil.copy(env_example, env_file)
        print("✅ Environment file created")
    else:
        print("✅ Environment file already exists")
    
    return True


def create_directories():
    """Create necessary directories"""
    print_header("Creating Directory Structure")
    
    directories = [
        "data/embeddings",
        "data/processed", 
        "data/raw",
        "data/models",
        "logs"
    ]
    
    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"✅ Created/verified: {directory}")
        except Exception as e:
            print(f"❌ Failed to create {directory}: {e}")
            return False
    
    return True


def install_dependencies():
    """Install Python dependencies"""
    print_header("Installing Dependencies")
    
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found")
        return False
    
    # Try to install dependencies
    commands = [
        "pip install --upgrade pip",
        "pip install -r requirements.txt"
    ]
    
    for command in commands:
        success = run_command(command, f"Installing dependencies", check=False)
        if not success:
            print("⚠️  Some dependencies may not have installed correctly")
            print("   This might be due to network issues or missing system libraries")
            print("   You can try installing manually later")
    
    return True


def download_models():
    """Download and setup models"""
    print_header("Setting up Models")
    
    script_path = "scripts/setup_local_models.py"
    
    if not os.path.exists(script_path):
        print(f"❌ {script_path} not found")
        return False
    
    print("📋 Downloading embedding and text generation models...")
    print("   This may take several minutes depending on your internet connection")
    
    success = run_command(f"python {script_path}", "Downloading models", check=False)
    
    if success:
        print("✅ Models downloaded successfully")
    else:
        print("⚠️  Model download may have failed")
        print("   You can try running this step manually later:")
        print(f"   python {script_path}")
    
    return True


def verify_setup():
    """Verify the setup is working"""
    print_header("Verifying Setup")
    
    verification_script = "verify_setup.py"
    
    if os.path.exists(verification_script):
        success = run_command(f"python {verification_script}", "Running verification", check=False)
        return success
    else:
        print("⚠️  Verification script not found, skipping verification")
        return True


def main():
    """Run the complete setup process"""
    print("🏗️  TEDx TrendSpotter - Complete Setup")
    print("     Embedding System Initialization")
    print("="*60)
    
    setup_steps = [
        ("Python Environment Check", check_python_requirements),
        ("Environment Configuration", setup_environment),
        ("Directory Structure", create_directories),
        ("Dependency Installation", install_dependencies),
        ("Model Download", download_models),
        ("Setup Verification", verify_setup)
    ]
    
    results = []
    
    for step_name, step_func in setup_steps:
        try:
            result = step_func()
            results.append((step_name, result))
            
            if not result:
                print(f"\n⚠️  {step_name} encountered issues but continuing...")
        except Exception as e:
            print(f"\n❌ {step_name} failed with exception: {e}")
            results.append((step_name, False))
    
    # Final summary
    print_header("Setup Summary")
    
    all_passed = True
    for step_name, result in results:
        status = "✅ COMPLETED" if result else "⚠️  ISSUES"
        print(f"{step_name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "="*60)
    
    if all_passed:
        print("🎉 Setup completed successfully!")
        print("\n📋 Next steps:")
        print("1. Collect TEDx data: python scripts/data_collection.py")
        print("2. Initialize database: python scripts/initialize_database.py")
        print("3. Launch application: streamlit run streamlit_app/app.py")
    else:
        print("⚠️  Setup completed with some issues.")
        print("\n📋 You may need to:")
        print("1. Install missing dependencies manually")
        print("2. Check internet connection for model downloads")
        print("3. Review error messages above")
        print("\n   Run 'python verify_setup.py' to check what's working")
    
    print("\n🔧 Manual troubleshooting:")
    print("   - Review the setup steps that had issues")
    print("   - Check system requirements (Python 3.8+, 4GB+ RAM)")
    print("   - Ensure internet connection for downloads")
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())