#-*- coding: utf-8 -*-
from fit.ColumnFixture import ColumnFixture

class HelloFit(ColumnFixture):
    _typeDict = {
    "description":"String",
    "num1":"Int",
    "num2":"Int",
    "result":"Int"
    }
    def _init_(self):
        ColumnFixture.__init__(self)
        self.descrip=''
        self.num1=''
        self.num2=''
    def result(self):
        add=self.num1+self.num2
        return add
