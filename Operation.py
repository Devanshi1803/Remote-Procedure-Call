# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:24:45 2021

@author: devanshi
"""
import Pyro4
from OperationInterface import Abstract_Op
@Pyro4.expose
class Op(Abstract_Op):
    def factorial(self, num):
        if num<0:
            return "Sorry, factorial does not exist for negative numbers"
        elif num == 0 or num == 1:
            return 1
        return num * self.factorial(num-1)
    
    def power(self, num1, num2):
        return num1**num2
    

    