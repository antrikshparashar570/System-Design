import uuid

class User:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.amount = 0

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getAmount(self):
        return  self.amount

    def setAmount(self, amount):
        self.amount = amount

