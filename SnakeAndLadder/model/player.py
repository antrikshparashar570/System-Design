import uuid

class Player:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name

    def getId(self):
        return self.id

    def getName(self):
        return self.name

"""
p = Player("antriksh")
print(type(p.getId()))
"""