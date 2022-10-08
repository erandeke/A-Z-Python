# Write a program to use UseDefinedExceptions


class InsufficientBalanceException(Exception):

    def __init__(self, amount, message):
        self.message = message;
        self.amount = amount;
        super().__init__(self.message);

    def __str__(self):
        return f'{self.amount}->{self.message}';


class Bank:

    def __init__(self, amount):
        self.amount = amount;

    def checkForBalance(self, amountForWithdrawal):
        if (amountForWithdrawal > self.amount):
            raise InsufficientBalanceException(amountForWithdrawal, "Insufficient funds in your account");
        else:
            print("success")


b = Bank(800);
amount = int(input("Enter the amount you wish to withdraw:"));
b.checkForBalance(amount);
