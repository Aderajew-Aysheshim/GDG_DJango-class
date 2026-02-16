import json #

# Create a Python dictionary representing a user
user_dict = {
    "username": "johndoe",
    "email": "john@example.com",
    "active_status": True
} #

# Convert this dictionary into a JSON string
json_output = json.dumps(user_dict, indent=4) #

print(json_output)
