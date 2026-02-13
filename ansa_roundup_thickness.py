#set
# A set in Python is an unordered collection of unique items.
# Sets do not allow duplicate values, and their elements are not stored in any particular order.
# You create a set using curly braces {} or the set() function.
# ets are useful for storing unique values and performing set operations like union, intersection, and difference.


my_set = {1, 2, 4, 5, 4, 1, "apple"}
print(my_set)
my_set.add("mango")
print(my_set)
my_set.remove(4)
print(my_set)

#list
# if you want add any item to list use append function
# list is changable ,ordered and duplicates are allowwed.
# square brackets will reprsent the lists.
#A list in Python is an ordered, mutable collection of items. You can add, remove, or change elements in a list.
 # Lists are created using square brackets [].
items = []
items.append(100)
items.append("apples")
items.append("banana")
print(items)
# if you want replce the diffrent item from your list you mention the place which should be replaced with item name.
items[0] = "mango"
print(items)
# list is changable ,ordered and duplicates are allowwed.
items.append("guha")
print(items)
print(len(items))
# if we want delete the item  from the list we will use function""pop"""
items.pop(0)
items.pop(1)
print(items)
# if you identify the length of the list use "len" function(length)
print(len(items))




#tupple
# A tuple in Python is an ordered, immutable collection of items. You create a tuple using parentheses ().
# Once created, you cannot change its elements.

my_tupple = (1, 5.9, 0, 2.2,1,1, "apple")
my_tupple.add(5)
print(my_tupple)

#INTERPRETER AND COMPILER
#The main difference between an interpreter and a compiler is how they execute code:
#Interpreter: Translates and executes code line by line. If there is an error, it stops at that line. 
# #Example: Python uses an interpreter.
#Compiler: Translates the entire code into machine language at once, creating an executable file. Errors are shown after the whole code is checked. 
#Example: C and C++ use compilers.
#In summary:
#- Interpreter: Executes code line by line, no separate output file.
# Compiler: Converts whole code to an executable file before running.

#nterpreter examples:
#Python (runs code line by line)
#avaScript (in browsers)
#Ruby

#Compiler examples:
#C (code is compiled to an executable before running)C++
#Java (Java code is compiled to bytecode, then run by the Java Virtual Machine)
