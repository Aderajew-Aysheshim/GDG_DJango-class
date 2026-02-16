class Teacher:
    def work(self):
        print("Teacher is teaching.")

class Doctor:
    def work(self):
        print("Doctor is healing people.")

# Use polymorphism through a loop (duck typing)
people = [Teacher(), Doctor()]
for person in people:
    person.work()
