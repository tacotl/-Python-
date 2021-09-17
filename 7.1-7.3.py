# 练习7-1：汽车租赁 编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，下面是一个例子。
# Let me see if I can find you a Subaru.
car = input('What car would you want to find?')
print(f'Let me see if I can find you a {car}.')

# 练习7-2：餐馆订位 编写一个程序，询问用户有多少人用餐。如果超过8位，就打印一条消息，指出没有空桌；否则指出有空桌。
answer = input('How many people would come to eat?')
answer = int(answer)
if answer > 8:
	print('Sorry')
else:
	print('Welcome,your seat is here')

# 练习7-3：10的整数倍 让用户输入一个数，并指出该数是否是10的整数倍。
num = input('Please input number:')
if num % 10 == 0:
	print('yes')
else:
	print('no')