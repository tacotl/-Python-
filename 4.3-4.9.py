# 练习4-3：数到20 使用一个for 循环打印数1～20（含）。
for i in range(1,21):
	print(i)

# 练习4-4：一百万 创建一个包含数1～1 000 000的列表，再使用一个for 循环将这些数打印出来。（如果输出的时间太长, 按Ctrl + C停止输出或关闭输出窗口。）
num = list(range(1,1000001))
for i in num:
	print(i)

# 练习4-5：一百万求和 创建一个包含数1～1 000 000的列表，再使用min() 和max() 核实该列表确实是从1开始到1000000结束的。另外，对这个列表调用函数sum() ，看看Python将一百万个数相加需要多长时间。
num = list(range(1,1000001))
print(min(num))
print(max(num))
print(sum(num))

# 练习4-6：奇数 通过给函数range() 指定第三个参数来创建一个列表，其中包含1～20的奇数，再使用一个for 循环将这些数打印出来。
odds = list(range(1,21,2))
for odd in odds:
	print(odd)

# 练习4-7：3的倍数 创建一个列表，其中包含3～30能被3整除的数，再使用一个for 循环将这个列表中的数打印出来。
# num = list(range(3,31,3))
for i in (list(range(3,31,3))):
	print(i)

# 练习4-8：立方 将同一个数乘三次称为立方 。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数（1～10）的立方，再使用一个for 循环将这些立方数打印出来。
numb = list(range(1,11))
for num in numb:
	nnn = num ** 3
	print(nnn)


# 练习4-9：立方解析 使用列表解析生成一个列表，其中包含前10个整数的立方
list1 = [num ** 3 for num in range(1,11)]
print(list1)