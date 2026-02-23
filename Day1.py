
print("Welcome to my AI/ML QA journey 🚀")
print ("AI-ML QA Journey - Day 1")


name = "Noor"
field = "AI/ML Quality Assurance"
print ("My name is: " , name)
print ("I am interested in: " , field)


a = 10
b = 20

print ("The sum is: " ,a+b)
print ("The subtraction is: ", a-b)
print  ("The multiplication is: " ,a*b)
print ("The division is: " , a/b)

#Calculator by user input

num1= int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print ("The sum is: " ,num1+num2)
print ("The subtraction is: ", num1-num2)
print  ("The multiplication is: " ,num1*num2)
print ("The division is: " , num1/num2)
print ("The modulus is: " , num1%num2)
print ("The average is: " , (num1+num2)/2)
print ("The exponent is: " , num1**num2)


#is-else conditions:

#Write a Python code to accept marks of a student from 1-100 and display the grade according to the

marks = int(input("Enter marks of the student: "))
if marks >=91 and marks <=100:
    print ("Grade is A")
elif marks >=81 and marks <=90:
    print ("Grade is B")
elif marks >=71 and marks <=80:
    print ("Grade is C")
elif marks >=61 and marks <=70:
    print ("Grade is D")
elif marks >=50 and marks <=60:
    print ("Grade is E")
elif marks >=0 and marks <=49:
    print ("Grade is F")
else:
    print ("Invalid marks entered. Please enter marks between 0 and 100.")


#Basic Model Evaluation using variables and types

model_name = "Spam Detection Model"
version = "1.0"
accuracy = 0.92
total_predictions = 150
failed_predictions = 12


success_rate = ((total_predictions - failed_predictions) / total_predictions) * 100

print("Model Name:", model_name)
print("Version:", version)
print("Accuracy:", accuracy)
print("Total Predictions:", total_predictions)
print("Failed Predictions:", failed_predictions)
print("Success Rate:", success_rate, "%")











