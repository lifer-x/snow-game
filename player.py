class Player:
    def __init__(self, charact: dict, used_type: str, counts: str, coins: str):
        self.charact = charact  # Словарь
        self.used_type = used_type  # Используемый инструмент
        self.count = int(counts)  # Число инструментов
        self.coins = int(coins)  # Число монет
        self.change_snow = 0  # Изменение снега
        self.update()

    def update(self):
        """
        Обновляет данные из словаря
        """
        self.effect = self.charact[self.used_type]["effect"]
        self.next = self.charact[self.used_type]["next"]
        self.strength_per_item = self.charact[self.used_type]["strength"]
        self.cost = self.charact[self.used_type]["cost"]
        self.strength = self.strength_per_item * self.count
        self.boost_cost = self.charact[self.used_type]["boost"]

    def do(self):
        """
        Действие для фарма монет
        """
        self.change_snow = self.effect * self.count
        self.coins += self.change_snow
        self.strength -= self.change_snow
        if self.strength == 0:  #
            self.count -= 1
        return self.change_snow

    def boost(self):
        """
        Меняет тип инструмента на более лучший
        """
        if self.coins >= self.boost_cost:  #
            self.coins -= self.boost_cost
            self.used_type = self.next
            self.update()
            self.count = 1

    def buy(self):
        """
        Покупка еще одного инструмента
        """
        if self.coins >= self.cost:  #
            self.coins -= self.cost
            self.count += 1
            self.update()

    def bot(self):
        """
        Одно срабатывание бота по принципу качаемся до максимума, потом закупается
        """
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

    def isLive(self) -> bool:
        """
        Проверка есть инструмент
        """
        if self.count <= 0:
            return False
        return True

    def ask(self, what_ask: str):
        """
        Запрос переменных класса
        """
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
