
# Step 1: Write to file
def log_user_activity(filename, activity):
     with open(filename, "w") as file:
        file.write(activity)

    # Step 2: Read the log history
     with open("log.txt",  "r") as file:
        print(file.read())

log_user_activity("log.txt", "User logged in at 10:00 AM\n")