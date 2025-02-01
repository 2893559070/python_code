# 列表推导
list1 = []
for i in range(10):
    list1.append(i)
print(list1)

list2 = [i for i in range(0, 10, 2)]
print(list2)

list3 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list3)

# 字典推导
dict1 = {i: i**2 for i in range(1, 5)}
print(dict1)  # {1: 1, 2: 4, 3: 9, 4: 16}

counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 需求：提取上述电脑数量大于等于200的字典数据
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)  # {'MBP': 268, 'DELL': 201}

# 集合推导式
list4 = [1, 1, 2]
set1 = {i ** 2 for i in list1}
print(set1)  # {1, 4}