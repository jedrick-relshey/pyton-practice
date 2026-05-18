#part 3 Learning List & tuples
#List is a Read And Write Collection of Variables that may be used to sort certain data
from os import cpu_count

#courses = ["JEDJED", "RELSHEY", "MICLAT"]

#Reading Lists ITEMS is cna read a list by printing one of the items inside it by using an INDEX

#Example of Positive Index, Negative Index
#print(courses[-1])

#Reading Lists RANGE is you can read a list's range of items by specifying a range of index
#print(courses[0:2])

#Assigning List ITEMS, you can assign a list item by using an INDEX and Assignment OPERATOR "="
#courses[0] = "jed"
#print(courses)

#List LENGTH is you can check the number of items in a list by using the len() function
#print(len(courses))

#LIST COUNT, you can count how many times an item occurs in a list by ising the count() function.

#print(courses.count("JEDJED"))

#LIST ADD ITEMS by APPEND(), append() adds an item at the END OF THE LIST.

#courses.append("POGI")
#print(courses)

#List ADD ITEMS by INSERT(), insert() adds an item at the SPECIFIED INDEX.

#courses.insert(1,"POGI")
#print(courses)

#courses.remove("JEDJED")
#print(print(courses))

#List DELETING ITEMS by POP(), pop() deletes an item based on their index but if index is not specified it deletes the last item.
#courses.pop(0)
#print(courses)

#List DELETING ITEMS by DEL, del deletes an item based on their index but id index is not specified it deletes the whole list.
#del courses[1]
#print(courses)

#Clearing a List, clear() deletes all the value in a list.
#courses.clear()
#print(courses)

#Copying a List, copy() copies the whole list which can be assigned to a new list
#x = courses.copy()
#print(x)

#XOMBINING List BY ADDING, you can use "+" operator to combine lists.
#food = ["apple", "milk"]
#print(courses + food)

#COMBINING List BY EXTEND(), extend() combines lists byu appending the specified list to the end of the first list.
#food = ["apple", "milk"]
#courses.append(food)
#print(courses)

#REVERSE List Items, reverse() Reverses the order of the List's Items.
#courses.reverse()
#print(courses)

#SORT List Items, sort() Sort's list's Items by Alphabet or Value depending on the datatype
#alphabet = ["Z", "A", "B", "C", "D", "E", "F"]
#alphabet.sort(reverse=True)
#print(alphabet)

#NESTED Lists A lis inside a List also known as sublist.
#print(courses[3][0][1])

#Tuples a Read-ONLY Collection of variables that may be used to sort certain data.
#1 CAN be READ.
#2 CAN be COMBiNED.
#3 CAN be DELETED COMPLETELY
#4 CAN be ASSIGNED.
#5 CAB be DELETED ONE BY ONE.

#courses = ("JEDJED", "RELSHEY", "MICLAT")
#print(courses)

#CatinG TUPLES and LISTS. Conver List to Tuples

#courses = ("JEDJED", "RELSHEY", "MICLAT")
#courses = list(courses)
#print(courses)

#courses = ["JEDJED", "RELSHEY", "MICLAT"]
#courses = tuple(courses)
#print(courses)