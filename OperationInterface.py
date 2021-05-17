# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:49:06 2021

@author: devanshi
"""

import Pyro4
from abc import ABC, abstractmethod
@Pyro4.expose  #to mark it availbale for remote access
class Abstract_Op(ABC):
    @abstractmethod
    def factorial(self, num):
        pass
    @abstractmethod
    def power(self, num1, num2):
        pass