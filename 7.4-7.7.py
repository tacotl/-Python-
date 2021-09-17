# 练习7-4：比萨配料 编写一个循环，提示用户输入一系列比萨配料，并在用户输入'quit' 时结束循环。每当用户输入一种配料后，都打印一条消息，指出我们会在比萨中添加这种配料。
prompt = 'Enter u want to use the batching:'
message = ''
while message != 'quit':
	message = input(prompt)
	prompt(message)


# 练习7-5：电影票 有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3～12岁的观众收费10美元；超过12岁的观众收费15美元。请编写一个循环,在其中询问用户的年龄，并指出其票价。
prompt = 'How old are u'
while True:
	age = input(prompt)
	if age < 3:
		print('free')
	elif age >= 3 and age <=12:
		print('$10')
	else:
		print('$15')


# 练习7-6：三种出路 以不同的方式完成练习7-4或练习7-5，在程序中采取如下做法。
# 在while 循环中使用条件测试来结束循环。
# 使用变量active 来控制循环结束的时机。
# 使用break 语句在用户输入'quit' 时退出循环。
prompt = 'Enter u want to use the batching'
active = input(prompt)
while True:
	if active == 'quit':
		break
	else:
		print(active)



# 练习7-7：无限循环 编写一个没完没了的循环，并运行它（要结束该循环，可按Ctrl + C，也可关闭显示输出的窗口）。
while True:
	print('good')