#LOOP IN PYTHON
#largest_number = -999999999
#number = int(input("Enter a number: "))
#while number != -1:
    #if number > largest_number:
        #largest_number = number
    #number = int(input("Enter a number: "))
#print("The largest number is: ", largest_number)
from operator import truediv

#odd_number = 0
#even_number = 0
#number = int(input("Enter a number or type 0 to stop: "))
#while number != 0:
    #if number % 2 == 0:
        #odd_number += 1
    #else:
        #even_number += 1
    #number = int(input("Enter a number or type 0 to stop: "))
#print("Odd numbers count: ", odd_number)
#print("Even numbers count: ", even_number)

#counter = 5
#while counter != 0:
    #print("Inside The loop: ", counter)
    #counter -= 1
#print("Outside The loop: ", counter)

#secret_number = 777
#print(
#"""+================================+
#| Welcome to my game, muggle!    |
#| Enter an integer number        |
#| and guess what number I've     |
#| picked for you.                |
#| So, what is the secret number? |
#+================================+""")
#number = int(input("Enter an number: "))
#while number != secret_number:
    #print("Ha ha! You're stuck in my loop!")
    #number = int(input("Enter the secret number: "))
#print(secret_number)
#print("Well done!")

print("Crush ka ba ng Crush mo?")
while True:
    answer = input("Answer : ")
    if answer == "hindi":
        print("Aray ko po!")
        break
    else:
        print("Wee?")