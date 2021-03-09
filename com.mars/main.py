# 打印菱形
def printDiamond():
    x = 5
    a = " "
    b = "*"
    for i in range(1, x + 1):
        print((x - i) * a + i * b + (i - 1) * b + (x - i) * a)
    for i in range(1, x + 1):
        print(i * a + (x - i) * b + (x - i - 1) * b + i * a)


# 报数游戏
def cpp(x):
    print(x)


# 反转list
def reversedList():
    print(f'Reverse_Output:')
    letterList = ["aaa", "bbb", "ccc", "ddd", "eee", "fff"]
    print(f'ERROR:', letterList)
    for i in range(0, int(len(letterList) / 2)):
        letterList[i], letterList[-1 - i] = letterList[-1 - i], letterList[i]
    print("AFTER", letterList)


if __name__ == '__main__':
    # printDiamond()
    # cpp(8)
    reversedList()
