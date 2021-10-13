class Mint:
    current_year = 2020
    def __init__(self):
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"
        kind.year = self.year
        return kind(kind.year)

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = self.current_year
        return self.year

class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        return self.cents + (Mint.current_year-self.year- 50)

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10

print(Mint().create(Dime).worth())