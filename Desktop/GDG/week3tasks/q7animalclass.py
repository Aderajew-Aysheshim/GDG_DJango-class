class Animal:
  def make_sound(self):
      print("Some generic animal sound")
  
class Cat(Animal):
      def make_sound(self):
          print("Meow!")  
          
my_cat = Cat()
my_cat.make_sound()
my_animal = Animal()
my_animal.make_sound()