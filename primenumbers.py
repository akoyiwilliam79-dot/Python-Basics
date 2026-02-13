#write a program to check whether the number is prime
#a prime number is greater than 1 and only has two divisors 1 and itself

num = int(input("Enter a number: "))

if num <= 1 :
     print("Not a prime Number")
else:
   for i in range(2,num):
       if num % i == 0:
        print("Not a prime Number")
        break
   else:
         print(" a prime Number")














