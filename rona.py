import os
import time
import random

# List of example commands to simulate terminal activity
commands = [
    'echo "Keeping the workspace alive!"',
    'pwd',  # Print working directory
    'ls',   # List directory contents
    'top -n 1',  # Run a one-time top command
    'uptime',  # Show system uptime
    'df -h',  # Disk usage
    'free -m',  # Memory usage
]

# Function to run random command
def run_random_command():
    command = random.choice(commands)
    print(f"Running command: {command}")
    os.system(command)

# Keep the terminal alive with random commands every 60-120 seconds
while True:
    run_random_command()
    time.sleep(random.randint(60, 120))  # Sleep for a random period between 60 and 120 seconds
