#This script will introduce us to the basics of using Python

#Imports
import math

#Variables
initial_integer = 1
initial_float = 1.0
cast_int_to_float = float(initial_integer)
cast_float_to_string = str(initial_float)

#Functions
y = lambda x: math.sin(x)

def sin(x):
    return math.sin(x)

def sin(x):
    return sin(x)

#Printing
print("Hello world!")
name = "Your Name"
print(f"Hello my name is {name}")


#Conditions
if type(initial_integer) == type(cast_int_to_float):
    print("It's the same!")
else:
    print("It's different!")

truth = "It's the same!" if type(initial_integer) == type(cast_int_to_float) else "It's different!"

print(truth)

#Equality vs Identity
string_one = "test"
string_two = "test"

print(string_one is string_two)
print(string_one == string_two)

string_two = string_one

print(string_one is string_two)
print(string_one == string_two)

#For loops
number_list_one = range(10)
number_list_two = range(10) + 1

for number in number_list_one:
    print(number)

for i,number in enumerate(number_list_one):
    print(i + ',' + number)

for number_one, number_two in zip(number_list_one,number_list_two):
    print(number_one + ',' + number_two)

#Iterators
fruits = ("apple", "banana", "cherry")
it = iter(fruits)
print(next(it))

#Classes
class MyString():
    def __init__(self,string):
        self.string = string
    def print_string(self):
        print(self.string)

my_string = MyString("hello")
my_string.print_string()

#Lists, Dictionaries, Sets, and Tuples

my_list = [1,2,3,4]
print(my_list)

my_dictionary = {'hi':1,'hello':2,'hey':3}
print(my_dictionary.keys())
print(my_dictionary.values())

my_tuple = ('hi','hello','hey')
print(my_tuple)

my_set = set()
my_set.add("Hi")
my_set.add(1)
my_set.add(40151)
print(my_set)