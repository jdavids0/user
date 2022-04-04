class User:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0
    
    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawal(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money (self, other_user, amount):
        self.amount -= amount
        other_user.amount +=amount
        self.display_user_balance()
        other_user.display_user_balance()

josh = User("Josh")
logan = User("Logan")
alex = User("Alex")

josh.make_deposit(200)
josh.make_deposit(400)
josh.make_deposit (50)
josh.make_withdrawal(200)
josh.display_user_balance()

logan.make_deposit(1000)
logan.make_deposit(200)
logan.make_withdrawal(150)
logan.make_withdrawal(500)
logan.display_user_balance()

alex.make_deposit(150)
alex.make_withdrawal(40)
alex.make_withdrawal(70)
alex.make_withdrawal(30)
alex.display_user_balance()

josh.transfer_money(alex, 50)