# 家具类
class Furniture():
    def __init__(self, name, area):
        # 家具名字
        self.name = name
        # 家具占地面积
        self.area = area

# 房屋类
class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def __str__(self):
        return f'房子坐落于{self.address}, 占地面积{self.area}, 剩余面积{self.free_area}, 家具有{self.furniture}'

    def add_furniture(self, item):
        """容纳家具"""
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            # 家具搬入后，房屋剩余面积 = 之前剩余面积 - 该家具面积
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积不足，无法容纳')

home = Home('北京', 100)

furniture1 = Furniture('冰箱', 5)
home.add_furniture(furniture1)

print(home.__str__())

