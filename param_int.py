import sys
import random
from param import Param

class IntParam(Param):
    def __init__(self, symbol):
        self.symbol = symbol
        self.minValue = -sys.maxint - 1
        self.maxValue = sys.maxint

    def getSymbol(self):
        return self.symbol

    def getMinValue(self):
        return self.minValue

    def setMinValue(self, minValue):
        self.minValue = minValue

    def getMaxValue(self):
        return self.maxValue

    def setMaxValue(self, maxValue):
        self.maxValue = maxValue

    def generateParam(self):
        return random.randint(self.minValue, self.maxValue)
