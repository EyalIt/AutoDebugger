import sys
import random

class StringParam:
    regex = "*"

    def __init__(self, regex):
        self.regex = regex

    def getRegex(self):
        return self.regex

    def setRegex(self, regex):
        self.regex = regex

    def generateParam(self):
        return random.randint(self.minValue, self.maxValue)
