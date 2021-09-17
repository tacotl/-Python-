# 练习4-10：切片 选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
pets = ['cat','dog','fish','horse','sheep']

# 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
print('The first three items in the list are:')
print(pets[:3])

# 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表的中间三个元素。
print('Three items from the middle of the list are:')
print(pets[1:4])

# 打印消息“The last three items in the list are:”，再使用切片来打印列表的末尾三个元素。
print('The last three items in the list are:')
print(pets[-3:])

# 练习4-11：你的比萨，我的比萨 在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其赋给变量friend_pizzas ，再完成如下任务。
my_pizzas = ['a','b','c']
friend_pizzas = my_pizzas[:]

# 在原来的比萨列表中添加一种比萨。
my_pizzas.append('e')
# 在列表friend_pizzas 中添加另一种比萨。
friend_pizzas.append('g')

# 核实有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for 循环来打印第一个列表；打印消息“My friend's favorite pizzas are:”，再使用一个for循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
print('My favorite pizzas are:')
for my_pizza in my_pizzas:
	print(my_pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)

# 练习4-12：使用多个循环 在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for 循环来打印列表。请选择一个版本的foods.py，在其中编写两个for 循环，将各个食品列表打印出来。
my_foods = ['pizza','falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
for my_food in my_foods:
	print(my_food)
friend_foods.append('ice cream')
for friend_food in friend_foods:
	print(friend_food)