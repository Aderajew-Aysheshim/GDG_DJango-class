
def log_user_activity(filename, activity):
   with open(filename, "w") as file:
      file.write(activity)


   with open(filename, "r") as file:
      print(file.read())

