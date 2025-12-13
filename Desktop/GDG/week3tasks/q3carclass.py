class Car:
  def __init__(self,make):
      self.make = make
      
my_car = Car("Toyota")

def get_make(car):
    return car.make
print(my_car.make)
print(get_make(my_car))

      
  