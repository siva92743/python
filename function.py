#Calling a Function
def my_function():
  print("Hello")

my_function()

#Arguments
def my_function(fname):
  print(fname + " Pass")

my_function("firos")
my_function("tintu")
my_function("mini")

#Number of Arguments
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Hello", "World")

#Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[0])

my_function("abi", "bilal", "charles")

#Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "abi", child2 = "bilal", child3 = "charles")

#Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "abi", lname = "bilal")

#Default Parameter Value
def my_function(country = "India"):
    print("I am from " + country)

my_function()

#Passing a List as an Argument
def my_function(fruits):
    for x in fruits:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Return Values
def my_function(x):
    return 5 * x

print(my_function(3))