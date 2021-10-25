#variables
students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"
print(students_count)
print(rating, is_published, course_name)
print("." * 10)


#Strings
course = "python Programming"
print(len(course))
print(course[0]) # first letter
print(course[-1]) # last letter 
print(course[0:3]) # first row third column 
print(course[0:]) # first row entire column
print(course[:3]) # entire row first 3 columns
print("." * 10)

#Escape Sequences \ used to enforce special characters
course = "Python \"Programming"
print(course)

course = "Python \'Programming"
print(course)

course = "Python \\Programming"
print(course)
print("." * 10)

#Formatted Strings: lets you use python expressions inside strings constants
first = "Sean"
last = "Humpherys"
full = f"{len(first)} {2 + 2}" 
print(full)
print(f"{first} {last}")
print("." * 10)

# string Methods
print("Chapter 2.6 String Methods")
course = "python programming"
print(course.upper())
print(course.lower())
print(course.title()) # capitalizes first later of every word
print(course.rstrip())#3 used to trim white spaces before and at end of string 
print(course.lstrip())
print(course.find("Pro")) # used to find the index of the value passed . -1 means string was not found
print(course.replace("p","j")) #used to replace character or sequesnce of character 
print("pro" in course) # check for existence of character using the in - boolean
print("swift" not in course) # check for value not existence in string 
print("." * 10)

# Numbers
print("Chapter 2.7 Numbers")
x = 1 
x = 1.1 #float with decimal
print(10 +3)
print(10 -3)
print(10 * 3)
print(10 /3)
print(10//3)
print(10 % 3) #modulos the remindar of division
print(10 ** 3) # ** to the power of 

x = 10
x = x+3
print(x)
x = 10
x +=3 #augumented operator to add
print(x)

z = 30
z *=3
print(z)


print("Chapter 2.8 Working with Number")
import math

print(round(2.9))
print(abs(-2.0))
print(math.ceil(2.2)) # get the ceiling of a number up 1 =3 
print("." * 10)


x = input("Enter a value for x:")
y = int(x) + 1
print(f"x: {x}, y: {y}")
print("." * 10)

rate = input("Enter interest rate e.g. 0.5: ")
rate = float(rate) # reusing variable 
# three different ways to output a number variable with text
print(f"Borrower does not qualify at {rate}") # string intterpolation 
print(f"Borrower does not quallity at", rate)
print("Borrow does not qualify at " + str(rate)) # convert to string
print()


# displaying decimals 
grams= 15.125
print(f"Weight is {grams}") #no formatting
print(f"Weight is {grams:.2f}") #2 decimals, f means float
print(f"Weight is {grams:.4f}") #4 decimals
print(f"Weight is {grams:.0f}") # 0 decimals 
#Extra. This website gives more options for formatting numbers when displaying numbers with strings https://thepythonguru.com/python-string-formatting/ 

#Task G
card_number = "XXX8974"
date = "9\\7\\2020"
cookies_cost = 3.15
chips_cost = 4.58
salsa_cost = 5.1
total_cost = (cookies_cost +  chips_cost + salsa_cost)
print("*" * 15)
print("Receipt")
print(f"Date: {date}")
print(f"cookies $ {cookies_cost}")
print(f"chips $ {chips_cost}")
print(f"salsa $ {salsa_cost}")
print(f"Total: $ {total_cost}")
print("*" * 15)
