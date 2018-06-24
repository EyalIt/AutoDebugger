import sys
import random

class IntParam:
    symbol = ''
    minValue = -sys.maxint - 1
    maxValue = sys.maxint

    def __init__(self, symbol, minValue, maxValue):
        self.symbol = symbol
        self.minValue = minValue
        self.maxValue = maxValue

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
