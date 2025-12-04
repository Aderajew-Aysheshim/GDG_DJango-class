# Step 1: Write to file
with open("log.txt", "a") as file:
    file.write("User logged in\n")

# Step 2: Read the log history
with open("log.txt", "r") as file:
    print(file.read())
