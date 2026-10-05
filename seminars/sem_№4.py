from math import dist
#Есть 3 вида манипулятров переменными
# 1. Операторы
# 2. Методы
# 3. Функции
#

c = []
c.append('1') # метод
a = 1 + 2 # оператор
k = len(c) # функция

class vector:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def len_vector(self):
        return dist((0, 0), (self.x, self.y))
v = vector(4,3)
# v.x = 6
# v.y = 5
print(v.len_vector())

