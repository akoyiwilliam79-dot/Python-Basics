from variables import firstname

age = 19 #age is an Integer
temperature = 36.75 #float
greeting = "Hello" #string
ismarried = True #boolian

print(greeting)
print("Are you",age,"years old?")
print("The body temperature of the patient is",temperature,"degrees celcius")
print(greeting,"william")
print("Are you in a relationship?",ismarried)


#Data structures - multiple values stored in a single variable
cars = ["bmw", "toyota", "honda", "mercedes", "G-Wagon"]#list - is ordered and changable
fruits = ("apple", "banana", "orange", "mango") #Tuple - is ordered and unchangeable
countries = {"Italy","Spain","Kenya","Japan"} #Set - unordered and unchangable
student ={
    "firstname" : "William Akoyi",
    "Age" : 19,
    "Course" : "MIT",
    "Gender" : "Male",
}#dictionary

print(cars)
print(fruits)
print(countries)
print(student)
print(student["firstname"])

#Typecasting



