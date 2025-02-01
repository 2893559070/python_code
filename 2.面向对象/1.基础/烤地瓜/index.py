class Potato():
    def __init__(self):
        # 被考的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            self.cook_state = '考糊了'

    def add_condiments(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜的被烤过的时间是{self.cook_time}，状态是{self.cook_state}，调料有{self.condiments}'


digua1 = Potato()
digua1.cook(5)

digua1.add_condiments('辣椒')

print(digua1)

