from model.split import Split
from model.user import User
from abc import  ABC, abstractmethod


class PercentSplit(Split):
    def __init__(self, percent):
        super(user)
        self.percent = percent

    def getPercent(self):
        return self.percent

    def setPercent(self, percent):
        self.percent = percent
