class Dog:

#init is a function used in class to store variables as parameters
#self is a key word in python used to point objects
   def __init__(self,breed,age,color):
     self.breed = breed
     self.age = age
     self.color = color

   def speak(self):
      print("dog is barking")

dog1 = Dog("German Shephard",5,"brown")
print(dog1.breed,dog1.age,dog1.color)
dog2 = Dog("Chiwawa",3,"black")
print(dog2.breed,dog2.age,dog2.color)
dog3 = Dog("Siberian Husky",5,"white")
print(dog3.breed,dog3.age,dog3.color)












