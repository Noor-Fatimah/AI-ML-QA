#Task Loop print numbers and squares of list 5 nummbers 

#for syntax: for item in squence (for loop is used to iterate over a sequence)

list = [2,3,4,5,6,7]
for i in list:
    print(i)
for i in range(2,8):
    print(i*i)



#Task while loop to print numbers from 1 to 5 while loop syntax: while condition (while loop is used to execute a block of code as long as the condition is true)
i = 1
while i<=5:
    print(i)
    i += 1

#Dictionary: A dictionary is a collection of key-value pairs. It is an unordered, mutable, and indexed data structure in Python. Dictionaries are defined using curly braces {} and consist of key-value pairs separated by a colon (:). Each key must be unique within the dictionary.

student = {
    "name" : "Noor",
    "age" : 20,
    "course" : "AI/ML",
    "grade" : "A"

}
print (student)


#Functions:

#Q: Enter a number and print its square using a function.

num = int(input("Enter a number: "))
def sq(num):
    return num*num
result = sq(num)
print("The square of the number is: " , result)


#Q: Create a function that: Takes 2 numbers and Returns their sum

def sum (a,b):
    return a + b
result = sum(5,4)
print("The sum of 2 numbers is: " , result)


#function that: Takes marks

# If marks >= 50 → return "Pass"

# Else → return "Fail"

num = int(input("Enter a number: "))
def marks(num):
    if num >= 50:
        print("Yeah You Pass :)")
    else:
        print("You Fail :(")

marks(num);


#First Create a list of model predictions then Create a function: If prediction >= 0.5 → "Positive"  Else → "Negative"

predictions = [0.9, 0.4, 0.7, 0.2, 0.95]

def model(predictions):
    for i in predictions:
        if i >= 0.5:
            print("Positive")
        else:
            print("Negative")

model(predictions);










