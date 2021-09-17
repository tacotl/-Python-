# 姓名 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名打印出来。
names = ['hhh','aaa','bbb']
for name in names:
	print(name)

# 问候语 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
for name in names:
	print(name +',Hi')

# 自己的列表 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，下面是一个例子。
# I would like to own a Honda motorcycle
cars = ['metor','bus']
for car in cars:
	print('I would like to own a ' + car)