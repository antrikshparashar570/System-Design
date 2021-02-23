class ExpenseManager:
    self.expenses = []
    self.balanceSheet = {}

    def addUser(self, user):
        self.balanceSheet[user.getId()] = {}

    def addExpense(self, paidBy, amount, splits, expenseType, expenseMetadata):
        expense = ExpenseService.createExpense(paidBy, amount, splits, expenseType, expenseMetadata)
        self.expenses.append(expense)
        for split in expense.getSplits():
            paidTo = split.getUser().getId
            balances = balanceSheet[paidBy]
            if paidTo not in balances:
                balances[paidTo] = 0
            balances[paidTo] = balances.get(paidTo) + split.getAmount()

            balances = balanceSheet[paidTo]
            if paidBy not in balances:
                balances[paidBy] = 0
            balances[paidBy] = balances.get(paidBy) - split.getAmount()

    def showBalance(self, userId):
        for userBalance in self.balanceSheet[userId]:
            print(userId, userBalance.key(), userBalance.val())