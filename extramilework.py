#in a footbal match if a player does a mistake is considered serious by the rules of the game he or she is given a red card ptherwise a yellow card.

mistake = input("Enter the mistake :")

if mistake == "serious":
   print("Give a red card")
else:
   print("Give a yellow card")


#in an olympics track event medals are awarded only to the first three athletes as follows:
#position 1:Gold medal
#position 2: silver medal
#position 2: Bronze medal

position =int(input("Enter the position :"))


if position == 1:
   print("Award Gold Medal")
elif position == 2:
    print("Award Silver Medal")
elif position == 3:
     print("Award Bronze Medal")
else:
     print("No Award")



#write a program that will prompt the user to enter two numbers x and y
#Divide x by y. if the value of y is zero an error message should be displyed.

x = int(input("Enter the number :"))
y = int(input("Enter the number :"))

if x/y == 0:
  print("Error division by zero")
else:
    print("Error message")
















