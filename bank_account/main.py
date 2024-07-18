class BankAccount:
    def __init__(self, number, holder, balance):
        self.number = number
        self.holder = holder
        self.balance = balance

    def __str__(self):
        return f"BankAccount({self.number}, {self.holder}, {self.balance})"
    
    def __add__(self, other):
        if isinstance(other, Check):
            if other.number == self.number:
                return BankAccount(self.number, self.holder, self.balance + other.amount)
            else:
                raise ValueError("Mismatched account number and check number")
        elif isinstance(other, (int, float)):
            return BankAccount(self.number, self.holder, self.balance + other)
        else:
            raise ValueError(f"Cannot add {other} to this bank account balance")
        
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            if self.balance < other:
                raise ValueError("Amount exceeds the balance limit")
            else:
                print(self.balance, other)
                return BankAccount(self.number, self.holder, self.balance - other)
        else:
            raise ValueError(f"Cannot subtract {other} to this bank account balance")
        
class Check:
    def __init__(self, number, amount):
        self.number = number
        self.amount = amount

ba1 = BankAccount(123, "Alex", 50)
print(ba1)
ba1 = ba1 + 20
print(ba1)
ba1 = ba1 - 20
print(ba1)
#ba1 = ba1 - 60
#print(ba1)
ch1 = Check(123, 100)
ba1 = ba1 + ch1

ch2 = Check(999, 200)
ba1 = ba1 + ch2