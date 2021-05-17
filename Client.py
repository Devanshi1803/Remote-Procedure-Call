# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:34:02 2021

@author: devanshi
"""
import Pyro4

ns = Pyro4.locateNS()
uri = ns.lookup('URI')
proxy_obj = Pyro4.Proxy(uri)

print("1) Factorial of a number")
print("2) Power of two numbers")
print("3) Exit")
choice = int(input("Enter Choice: "))
while(1):
    if choice==1:
        num1=int(input("Enter number: "))
        print(proxy_obj.factorial(num1))
    elif choice==2:
        num1=int(input("Enter number1: "))
        num2=int(input("Enter number2: "))
        print(proxy_obj.power(num1,num2))
    elif choice==3:
        break
    else:
        print("Invalid Choice")
        choice = int(input("Enter Choice: "))
        continue
    choice = int(input("Enter Choice: "))