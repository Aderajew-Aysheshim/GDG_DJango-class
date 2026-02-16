import json
from abc import ABC, abstractmethod

class Notification(ABC): #
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification): #
    def send(self, message):
        return f"Sending Email: {message}"

class SMSNotification(Notification): #
    def send(self, message):
        return f"Sending SMS: {message}"

json_data = """
[
{"type": "email"},
{"type": "sms"}
]
""" #

data_list = json.loads(json_data)
notifications = []

# Use the JSON data to decide which object to create
for item in data_list:
    if item["type"] == "email":
        notifications.append(EmailNotification())
    elif item["type"] == "sms":
        notifications.append(SMSNotification())

# Call the same method using polymorphism
for notification in notifications:
    print(notification.send("Workout completion notice"))
