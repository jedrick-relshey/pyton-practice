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

#
# if not age >= 18:
#     print("Sorry, you are under 18.")
# else:
#     print("Legal age.")

# notebook = False
# ballpen = True
# ruler = False
#
# if notebook or ballpen or ruler:
#     print("Pasok kana")
# else:
#     print("Bawal")

# age = int(input("Enter your Age: "))
# height = int(input("Enter your Height: "))
#
# if age >= 18 and height >= 176:
#     print("Tall and Legal Age")
# elif age >= 18 and height >= 150:
#     print("Average ang Legal Age")
# elif age >= 18:
#     print("Not enough height to age")
# else:
#     print("Too Young")

# bag = ["Wallet", "ballpen", "computer"]
#
# if "gun" in bag or "ballpen" in bag:
#     print("huli")
# else:
#     print("PAsok")

# gradeOne = float(input("Math: "))
# gradeTwo = float(input("Programming: "))
# gradeThree = float(input("Science: "))
#
# average = (gradeOne + gradeTwo + gradeThree ) / 3
#
# print("The Average is: " + str(average))
#
# if average > 100 or average <= 50:
#     print("Invalid grade")
# elif average >= 98:
#     print("With Highest Honor")
# elif average >= 95:
#     print("With High Honor")
# elif average >= 90:
#     print("With Honor")
# elif average >= 75:
#     print("Passed")
# elif average >= 51:
#     print("Failed")
# else:
#     print("Whats that?")

# age = 12
#
# while age < 18:
#     print("Still Young : " + str(age))
#     age = age + 1
# else:
#     print("Legal Age : " + str(age))

# studentID = [20000123,20000124,20000125,20000126,]
# i = 0
#
# while i < len(studentID):
#     print(studentID[i])
#     i = i + 1

# print("Crush ka ba? ")
#
# while True:
#     answer = input("Answer : ")
#     if answer == "hindi":
#         print("Aray ko!")
#         break
#     else:
#         print("Wee")

numbers = [1,2,3,4,5,6,7,8,9,10]

i = 0

while i < len(numbers):
    if(numbers[i] % 2 == 0):
        print("Even Number : " + str(numbers[i]))
    else:
        print("Odd Number  : " + str(numbers[i]))
    i = i + 1