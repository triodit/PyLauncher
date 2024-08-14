import os
import subprocess
import sys

# Version number
VERSION = "1_0_0"

def find_and_launch_main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Look for main.py in the same directory
    main_file = os.path.join(script_dir, "main.py")
    
    if os.path.isfile(main_file):
        try:
            # Launch main.py without creating a new terminal window
            subprocess.run(
                [sys.executable, main_file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        except Exception as e:
            print(f"Error launching main.py: {e}")
    else:
        print("main.py not found.")

if __name__ == "__main__":
    find_and_launch_main()
