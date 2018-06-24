import sys
import random
from param import Param

class StringParam(Param):
    def __init__(self, symbol):
        self.symbol = symbol

    def getRegex(self):
        return self.regex

    def setRegex(self, regex):
        self.regex = regex

    def generateParam(self):
        return ""
