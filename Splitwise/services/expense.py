import uuid

class ExpenseService():
    def createExpense(self, paidBy, amount, splits, expenseType, expenseMetadata):
        switch(expenseType):
            case(EXACT):
                return exactExpense(amount, paidBy, splits, expenseMetadata)
            case(PERCENT):
                for split in splits:
                    percentSplit = split
                    split.setAmount((amount*percentSplit.getPercent())/100.0)

                return PercentExpense(paidBy, amount, splits, expenseMetadata)
            case(EQUAL):
                splitSize = len(splits)
                for split in splits:
                    splitAmount = (amount*100/splitSize) / 100.0
                    split.setAmount(splitAmount)

                splits[0].setAmount(splitAmount)
                return EqualExpense(paidBy, amount, splits, expenseMetadata)
