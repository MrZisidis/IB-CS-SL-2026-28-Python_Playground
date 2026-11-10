#import libraries
import time

#define functions
def welcome():
    print("This is my very own function!")

def welcome2():
    print("this is a second function")
    name = input("What is your name?")
    print ("hello"+name)

def welcome3(name): #parameter
    print("This is my 3rd function")
    print("Hello", name, "and have a nice day!")

def addition(number1, number2):
    print(number1+number2)
#main code
# welcome()
# welcome2()
# welcome3("Tom") #argument
# welcome3("John")
# welcome3("Mary")

addition(3,4)
addition(5,6)