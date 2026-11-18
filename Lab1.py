
# Create a sample log file
with open("log.txt", "w") as file:
    file.write("INFO: Program started\n")
    file.write("ERROR: File not found\n")
    file.write("INFO: Program running\n")
    file.write("WARNING: Low memory\n")

# Read the log file
with open("log.txt", "r") as file:
    print("Log File Contents:\n")
    for line in file:
        print(line.strip())
