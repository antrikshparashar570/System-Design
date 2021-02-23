from model.split import Split
from model.user import User
from abc import  ABC, abstractmethod


class EqualSplit(Split):
    def __init__(self):
        super(user)


    def createExpense(self, paidBy, amount, splits):
        splitAmount = amount/len(splits)
        for split in splits:
            if split is paidBy:
                split.setAmount(split.getAmount + splitAmount)
            else:
                split.setAmount(split.getAmount - splitAmount)

