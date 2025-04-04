import subprocess
import time

SCRIPT_NAME = "p.py"  # Your main script

def is_running():
    try:
        # Check if the script is running
        output = subprocess.check_output(f"pgrep -f {SCRIPT_NAME}", shell=True).decode()
        return bool(output.strip())
    except subprocess.CalledProcessError:
        return False

def run_script():
    print(f"🚀 Starting: {SCRIPT_NAME}")
    return subprocess.Popen(["python3", SCRIPT_NAME])

def monitor():
    print("🔁 Monitor started. Watching p.py 24/7...")
    process = run_script()

    while True:
        if process.poll() is not None:
            print("⚠️ p.py crashed or stopped. Restarting...")
            process = run_script()
        time.sleep(5)  # Check every 5 seconds

if name == "main":
    try:
        monitor()
    except KeyboardInterrupt:
        print("🛑 Monitor stopped manually.")
