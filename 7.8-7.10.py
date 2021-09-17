# 练习7-8：熟食店 创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字，再创建一个名为finished_sandwiches 的空列表。遍历列表sandwich_orders ，对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich ，并将其移到列表finished_sandwiches中。所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['Francesinha','Cachopo','Mollete']
finished_sandwiches = []
while sandwich_orders:
	sandwich_orders1 = sandwich_orders.pop()
	print(f'I made your {sandwich_orders1} sandwich')
	finished_sandwiches.append(sandwich_orders1)

for so in finished_sandwiches:
	print(f'{so} is finish!')

# 练习7-9：五香烟熏牛肉卖完了 使用为完成练习7-8而创建的列表sandwich_orders ，并确保'pastrami' 在其中至少出现了三次。在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉（pastrami）卖完了；再使用一个while循环将列表sandwich_orders 中的'pastrami' 都删除。确认最终的列表finished_sandwiches 未包含'pastrami' 。
sandwich_orders = ['pastrami','Francesinha','pastrami','Cachopo','pastrami']
while 'pastrami' in sandwich_orders:
	 sandwich_orders.remove('pastrami')
print('Pastrami is sold out!')
print(sandwich_orders)
	

# 练习7-10：梦想的度假胜地 编写一个程序，调查用户梦想的度假胜地。使用类似于下面的提示，并编写一个打印调查结果的代码块。
# If you could visit one place in the world, where would you go?
responses = {}
while True:
	name = input("What is your name?")
	response = input('If you could visit one place in the world, where would you go?')
	responses[name] = response
	repeat = input('Would you like to let another person respond?(yes/no)')
	if response == 'no':
		False
for name,response in responses.items():
	print(f'{name} want to go {response}.')
