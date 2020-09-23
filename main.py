# 打印菱形
def printDiamond():
    x = 5
    a = " "
    b = "*"
    for i in range(1, x + 1):
        print((x - i) * a + i * b + (i - 1) * b + (x - i) * a)
    for i in range(1, x + 1):
        print(i * a + (x - i) * b + (x - i - 1) * b + i * a)



def cpp(x):
	l = []
	count = 0  #报数
	drop = 0
	for i in range(1,x+1):
		l.append(i)
	print(l)
	while (len(l)-drop) > 1:
		count
		drop
		for i in range(0,len(l)):
			if(l[i] != 0):#被删除的不报数
				count += 1
				if(count > 3):
					count = 1 #1-3报数
				print('%d号报数：%d' % (l[i],count))
				if(count == 3):
					print('要删除的号码：%d' % l[i])
					l[i] = 0
					drop += 1
	print (l)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ##printDiamond()
    cpp(8)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
