import os
import time
import subprocess

BOT_SCRIPT = "p.py"

def restart_bot():
    while True:
        print("🚀 Starting bot...")
        process = subprocess.Popen(["python3", "p.py"])

        process.wait()  # Wait for bot to stop (e.g., after 6 hours)
        print("⚠️ Bot stopped! Restarting in 5 seconds...")
        time.sleep(5)

if __name__ == "__main__":
    restart_bot()