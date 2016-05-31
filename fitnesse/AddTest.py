#-*- coding: utf-8 -*-
from fit.ActionFixture import ActionFixture

class AddTest(ActionFixture):
    _typeDict = {
        "firstPart":"Int",
        "secondPart":"Int",
        "join":"String",
        "together":"Int",
    }
    def __init__(self):
        self.firstPart  = 0
        self.secondPart = 0
        self.result = 0

    def firstPart(self, firstPart):
        self.firstPart = firstPart

    def secondPart(self, secondPart):
        self.secondPart = secondPart

    def join(self):
        self.result = self.firstPart + self.secondPart

    def together(self):
        return self.result
