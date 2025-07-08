#!/usr/bin/env python3
"""
Setup and run script for AI Helper Medical Consultation application
"""

import sys
import os
import subprocess

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} detected")
    return True

def run_tests():
    """Run the test suite."""
    print("🧪 Running tests...")
    try:
        result = subprocess.run([sys.executable, "test_ai_helper.py"], 
                              capture_output=True, text=True, cwd=os.path.dirname(__file__))
        if result.returncode == 0:
            print("✅ All tests passed!")
            return True
        else:
            print("❌ Tests failed:")
            print(result.stdout)
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False

def run_application():
    """Run the main application."""
    print("🚀 Starting AI Helper...")
    try:
        subprocess.run([sys.executable, "ai_helper.py"], cwd=os.path.dirname(__file__))
    except KeyboardInterrupt:
        print("\n👋 Thanks for using AI Helper!")
    except Exception as e:
        print(f"❌ Error running application: {e}")

def main():
    """Main setup and run function."""
    print("🏥 AI Helper for Medical Consultations - Setup")
    print("=" * 50)
    
    if not check_python_version():
        sys.exit(1)
    
    # Ask user what they want to do
    while True:
        print("\nWhat would you like to do?")
        print("1. Run tests")
        print("2. Start application")
        print("3. Run tests and start application")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            run_tests()
        elif choice == "2":
            run_application()
            break
        elif choice == "3":
            if run_tests():
                run_application()
            break
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()