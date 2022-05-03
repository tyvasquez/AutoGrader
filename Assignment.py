#This is the student's assignment. They are given 3 questions which
# they must complete by the guidelines set in the instructions

#Question one:
#Create a function called max which takes a given array [1,8,3] and
# returns the maximum value in that array
import numpy as np

def max(a):
    array = np.array(a)
    max = np.max(array)
    return max
a = [1,8,3]
max(a)

#Question two:
#Create a function called length that returns the
# length of the string 'Hello World'

def length(a):
    length  = (len(a))
    return length

a = 'hello world'
length(a)

#Question 3:
#Write a recursive fuction called palindrome that gets the
# string 'racecar' and returns 'True' if it is a palindrome and False otherwise
#A palindrome is a string that reads the
# same forward as backward, e.g., level , radar ,racecar

def palindrome(a):
    length = len(a)
    if length <2:
        return True
    elif a[0] == a[length-1]:
        return palindrome(a[1:length-1])
    else:
        return False
a = 'racecar'
palindrome(a)
#Question4
# Write a function that gets an 1-D array a and a number v, and returns the closest value
# in the array to v. For example, if a = [10, 3, 7, 8, 15] and v = 4, then the function should
# return 3. Hint: use the function np.argmin().

import numpy as np
def closest(b,v):
    array = np.array(b)
    x = np.abs(array-v).argmin()
    return (array[x])
b = [10,3,7,8,15]
v =4
x = closest(b,v)