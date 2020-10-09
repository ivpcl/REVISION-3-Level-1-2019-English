# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 09:43:08 2018

@author: Marios Pattichis
"""


from random import *
secret_number = randint(1, 10) # generates the numbers ???

print("I have generated a secret integer between 1 and 10")
print("Can you guess it?")
number = int(input("Enter your guess "))
if (secret_number > number):
    print("Your guess is low") 
elif (secret_number < number):
    print("Your guess is high") 
else:
    print("Your guess is correct :-) ")
    
while (number != secret_number):    
    number = int(input("Enter your guess "))
    if (secret_number > number):
        print("Your guess is low")         
    elif (secret_number < number):
        print("Your guess is high") 
    else:
        print("Your guess is correct :-) ")


