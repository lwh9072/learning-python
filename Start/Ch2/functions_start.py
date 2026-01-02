# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic 
# def hello_func():
#   print("hello world!")
#   name = input("What is your name? ")
#   print("Nice to meet you,", name)


# hello_func()

# function that takes parameters
# def hello_func(greeting):
#   print("hello world!")
#   name = input("What is your name? ")
#   print(greeting, name)

# hello_func("How are you")
# hello_func("SUP")

# function that returns a value
def cube(x):
  return x*x*x

# result = cube(3)
# print(cube(3))


# function with default value for an parameter
def hello_func(greeting, name=None):
  print("hello world!")
  if name == None:
    name = input("What is your name? ")
  print(greeting, name)

# hello_func("How are you", "Tina")
# hello_func("Sup")

# hello_func(name="Marco", greeting="Yo")

# function with variable number of parameters
def multi_add(*args, start):
  result = start
  for x in args:
    result = result + x
  return result

mylist = [1, 2, 3, 5.5]
print(multi_add(start=1000, *mylist))

