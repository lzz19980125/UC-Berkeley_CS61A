class Account(object):
    interest = 0.02
    def __init__(self,account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self,amout):
        self.balance = self.balance+amout
        return self.balance
    def withdraw(self,amout):
        if amout>self.balance:
            return "Insufficient funds"
        self.balance = self.balance - amout
        return self.balance

a = Account("Jim")
print(a.balance)
print(a.holder)

b = Account('Jack')
b.balance = 200
print([acc.balance for acc in (a,b)])

print(a is a)
print(a is not b)

#通常，使用赋值将对象绑定到新名称并不会创建新的对象。
c =a
print(c is a)

tom_account = Account('Tom')
print(tom_account.deposit(100))
print(tom_account.withdraw(90))
print(tom_account.withdraw(90))
print(tom_account.holder)

#类的内建函数可以利用函数hasattr()查找某个类是否具有某个属性，并且可以利用函数getattr()查找某属性的值
print(getattr(tom_account,'balance'))
print(hasattr(tom_account,'holder'))

#作为类的属性，方法只是个函数，但是作为实例属性，它是绑定方法
print(type(Account.deposit))
print(type(tom_account.deposit))

#方法可以有以下两种方法调用：
print(Account.deposit(tom_account,1001))
print(tom_account.deposit(1000))

#类属性（也被叫做类变量或者静态变量）：
print(tom_account.interest)
print(a.interest)

#但是，对类属性的单一赋值语句会改变所有该类实例上的属性值。
Account.interest = 0.04
print(tom_account.interest)
print(a.interest)

#如果我们向账户实例的属性interest赋值，则会创建新的属性实例，其与现有的类属性具有相同名称
a.interest = 0.08
print(a.interest)
print(tom_account.interest)
print("********************")
Account.interest = 0.05
print(tom_account.interest)
print(a.interest)

print("********************")

#继承
class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self,amout):
        return Account.withdraw(self,amout+self.withdraw_charge)

checking = CheckingAccount('Sam')
print(checking.deposit(10))
print(checking.withdraw(5))
print(checking.interest)

#多重继承
class SavingAccount(Account):
    deposit_charge = 2
    def deposit(self,amout):
        return Account.deposit(self,amout - self.deposit_charge)

class AsSeenOnTVAccount(CheckingAccount,SavingAccount):
    def __init__(self,account_holder):
        self.holder = account_holder
        self.balance = 1

such_a_deal = AsSeenOnTVAccount('John')
print(such_a_deal.balance)
print(such_a_deal.deposit(20))
print(such_a_deal.withdraw(5))
print(such_a_deal.deposit_charge)
print(such_a_deal.withdraw_charge)

#python中可以用.mro()来查询继承查找的顺序
print("******************************")
print([c.__name__ for c in AsSeenOnTVAccount.mro()])












