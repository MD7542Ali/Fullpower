import time
import sys

def keep_workspace_active():
    """
    Keeps the terminal active by printing dots periodically.
    Runs for 24 hours.
    """
    duration = 24 * 60 * 60  # 24 hours in seconds
    interval = 5 * 60  # Print every 5 minutes (300 seconds)
    start_time = time.time()

    print("🚀 Keeping the workspace active for 24 hours...")

    while (time.time() - start_time) < duration:
        sys.stdout.write(".")  # Print a dot
        sys.stdout.flush()  # Ensure it's immediately displayed
        time.sleep(interval)

    print("\n✅ 24-hour keep-alive session completed.")

if __name__ == "__main__":  # ✅ Corrected syntax
    keep_workspace_active()
