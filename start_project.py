#!/usr/bin/env python3

import subprocess
import signal
import os
from time import sleep

# Define the paths relative to the current script location
base_directory = os.path.dirname(os.path.abspath(__file__))
django_directory = os.path.join(base_directory, "project")
frontend_directory = os.path.join(base_directory, "project", "frontend")

# Start the Django server
django_process = subprocess.Popen(
    ["python3", "manage.py", "runserver", "8080"],
    cwd=django_directory,
    preexec_fn=os.setsid
)

print(f"Started Django server with PID {django_process.pid}")

# Install npm dependencies for the frontend if node_modules directory doesn't exist
node_modules_path = os.path.join(frontend_directory, "node_modules")
if not os.path.exists(node_modules_path):
    print("Installing npm dependencies for the frontend...")
    subprocess.call(
        ["npm", "install"],
        cwd=frontend_directory
    )

# Start the React development server
frontend_process = subprocess.Popen(
    ["npm", "start"],
    cwd=frontend_directory,
    preexec_fn=os.setsid
)

print(f"Started React server with PID {frontend_process.pid}")

try:
    # Wait for the servers to run
    while True:
        sleep(1)
except KeyboardInterrupt:
    # Handle Ctrl-C to stop the servers
    print("\nStopping servers...")

    # Send SIGTERM signal to the process groups
    os.killpg(os.getpgid(django_process.pid), signal.SIGTERM)
    os.killpg(os.getpgid(frontend_process.pid), signal.SIGTERM)

    # Wait for the processes to stop
    django_process.wait()
    frontend_process.wait()

    print("Servers stopped.")
