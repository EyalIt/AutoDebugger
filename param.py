from abc import ABCMeta, abstractmethod

class Param:
    __metaclass__ = ABCMeta

    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def generateParam(self):
        pass
