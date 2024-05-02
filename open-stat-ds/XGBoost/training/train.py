#!/usr/bin/env python3
import subprocess

# List of Python scripts to run
scripts = ["squat.py", "bench.py", "deadlift.py", "total.py"]

# Run each script in a new terminal
for script in scripts:
    subprocess.Popen(["gnome-terminal", "--", "python3", script])
