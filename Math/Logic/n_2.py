#  Проверить соблюдаются ли приоритеты логических операций (~, &, |, ^) в питоне.


var1 = ~(3 & 9) | 8 ^ 1  # -1/(-11/9)
var2 = 4 & 9 | 1 ^ 0  # 1
var3 = 3 | 2 ^ 0 ^ 7 & ~ 2  # 7/(-3)
var4 = 1 ^ 9 ^ 2 | 3 & 8  # 10
var5 = 7 & -3  # 5 (1/-3)?


results = [9, 1, -3, 10, -3]


if __name__ == '__main__':
    for i in range(1, 6):
        name = eval('var' + str(i))

        print(name, name == results[i - 1])
