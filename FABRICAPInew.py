import subprocess

# Define the command to open the program. Here, I'm using 'notepad' as an example for Windows.
command = "notepad"

# Number of times to open the program
iterations = 10000

for i in range(iterations):
    subprocess.Popen(command)

print(f"Opened {command} {iterations} times.")
