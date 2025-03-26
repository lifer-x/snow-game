class Player:
    def __init__(self, charact: dict, used_type: str, counts: str, coins: str):
        self.charact = charact
        self.used_type = used_type
        self.count = int(counts)
        self.coins = int(coins)
        self.change_snow = 0
        self.update()

    def update(self):
        self.effect = self.charact[self.used_type]["effect"]
        self.next = self.charact[self.used_type]["next"]
        self.strength_per_item = self.charact[self.used_type]["strength"]
        self.cost = self.charact[self.used_type]["cost"]
        self.strength = self.strength_per_item * self.count
        self.boost_cost = self.charact[self.used_type]["boost"]

    def do(self):
        self.change_snow = self.effect * self.count
        self.coins += self.change_snow
        self.strength -= self.change_snow
        if self.strength == 0:
            self.count -= 1
        return self.change_snow

    def boost(self):
        if self.coins >= self.boost_cost:
            self.coins -= self.boost_cost
            self.used_type = self.next
            self.update()
            self.count = 1

    def buy(self):
        if self.coins >= self.cost:
            self.coins -= self.cost
            self.count += 1
            self.update()

    def bot(self):
        self.change_snow = 0
        if self.next != None:
            if self.coins < self.boost_cost:
                self.change_snow = self.do()
            else:
                self.boost()
        elif self.next == None:
            if self.coins < self.cost:
                self.change_snow = self.do()
            else:
                self.buy()
        return self.change_snow

    def isLive(self):
        if self.count <= 0:
            return False
        return True

    def ask(self, what_ask: str):
        if what_ask.lower() == "used_type":
            return str(self.used_type)
        elif what_ask.lower() == "effect":
            return str(self.effect)
        elif what_ask.lower() == "strength":
            return str(self.strength)
        elif what_ask.lower() == "coins":
            return str(self.coins)
        elif what_ask.lower() == "count":
            return str(self.count)
        elif what_ask.lower() == "cost":
            return str(self.cost)
        elif what_ask.lower() == "boost_cost":
            return str(self.boost_cost)
