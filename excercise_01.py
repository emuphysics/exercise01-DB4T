##LESSON 1 BASIC
## A First Program
print("Hello world!")
nSecondsInDay= 24 * 60 * 60
print(nSecondsInDay)
nSecondsInYear =nSecondsInDay * 365.25
print(nSecondsInDay)

## Math operators
a= 2+3 # Addition
print(a)
s=25-10 # Subtraction
print(s)
d=5*7 # Multiplication
print(d)
e=35/7 # Division
print(e)
f=5**7 # Exponent
print(f)
D=76%7 # Modulus
print(D)

# ## Math module
import math
print(math.sin(3))
print(math.cos(10))
print(math.sqrt(2))
print(math.pi)
#
##Variables
temp_celsius = 10.0
print(temp_celsius)
print("Temp Fahrenheight: ",5/9 * (temp_celsius - 32))
temp_celsius = 15.0 #Updating Variables
print("The temperature has changed to", temp_celsius,"deg C")
print("Temp Fahrenheight: ",5/9 * (temp_celsius - 32))

##Data Type
a = 7 #Integer
print("Type of a: ", type(a))

b = 9.1 #Real Number
print("\nType of b: ", type(b))

c = 3 + 7j #Complex Number
print("\nType of c: ", type(c))

d='Suman' #Character string
print("\nType of d: ", type(d))

e=True or False #Boolean
print("\nType of e: ", type(e))
#
#
##Input
username=input('Type your Name  :  ')
print(username)
print(username.upper())
print(username.lower())
print(len(username))





#######GitHUB PROBLEM
##Problem 1
major = "Artificial Intelligence"
tacosRating = 8
sleepRating = 10
print(major)
print(tacosRating)
print(sleepRating)

##Problem 2
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name  + " " +  last_name
print(full_name)

##Problem 3
#1
major = "Artificial Intelligence"
tacosRating = 8
sleepRating = 10
print("major:", type(major))
print("tacosRating:", type(tacosRating))
print("sleepRating:", type(sleepRating))

#2
tacosRating = 8
sleepRating = 10
average_rating = (tacosRating + sleepRating) / 2
print("The average rating is:", average_rating)

#3
first_name = "Suman"
last_name = "Roy"
tacosRating = 8
sleepRating = 10
print("My name is", first_name, "and I give tacos a score of", tacosRating, "out of 10!")
print("I am", first_name, last_name, "and my sleeping enjoyment rating is", sleepRating, "/ 10!")
print("Based on the factors above, my happiness rating is", average_rating, "out of 10, or", average_rating * 10, "%!")
