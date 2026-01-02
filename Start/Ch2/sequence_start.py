# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [1, 2, "three", False]

# to access a member of a sequence type, use []


# add a list to another list


# use slices to get parts of a sequence
# print(mylist[-4:-1:])

# you can use slices to reverse a sequence
# print(mylist[:3:-2])
clist = [9, mylist[::-1], 7]
print(clist[::-1])

# Tuples are like lists, but they are immutable


# Sets are also sequences, but they contain unique values

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(7 in clist)