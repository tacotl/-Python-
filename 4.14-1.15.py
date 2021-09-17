# 练习5-3：外星人颜色 假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color的变量，并将其赋值为'green'、'yellow' 或'red' 。
# 编写一条if 语句，检查外星人是否是绿色的。如果是，就打印一条消息，指出玩家获得了5分。
alien_color = 'green'
if alien_color == 'green':
	print('u get 5 points')
# 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
alien_color = 'yellow'
if alien_color == 'green':
	print('u get 5 points too')


# 练习5-4：外星人颜色2 像练习5-3那样设置外星人的颜色，并编写一个if-else 结构。
alien_color = 'red'
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5分。
if alien_color == 'yellow':
	print('u get 5 points')
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10分。
else:
	print('u get 10 points')
# 编写这个程序的两个版本，在一个版本中执行if 代码块，在另一个版本中执行else 代码块。


# 练习5-5：外星人颜色3 将练习5-4中的if-else 结构改为if-elif-else 结构。
alien_color = 'yellow'
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了5分。
if alien_color == 'green':
	print('u get 5 points')
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了10分。
elif alien_color == 'yellow':
	print('u get 10 points')
# 如果外星人是红色的，就打印一条消息，指出玩家获得了15分。
else:
	print('u get 15 points')
# 编写这个程序的三个版本，分别在外星人为绿色、黄色和红色时打印一条消息。


# 练习5-6：人生的不同阶段 设置变量age的值，再编写一个if-elif-else结构，根据age的值判断一个人处于人生的哪个阶段。
age = 19
# 如果年龄小于2岁，就打印一条消息，指出这个人是婴儿。
if age < 2:
	print('baby')
# 如果年龄为2（含）～4岁，就打印一条消息，指出这个人是幼儿。
elif age < 4:
	print('infant')
# 如果年龄为4（含）～13岁，就打印一条消息，指出这个人是儿童。
elif age < 13:
	print('child')
# 如果年龄为13（含）～20岁，就打印一条消息，指出这个人是青少年。
elif age < 20:
	print('teenager')
# 如果年龄为20（含）～65岁，就打印一条消息，指出这个人是成年人。
elif age < 65:
	print('adult')
# 如果年龄超过65岁（含），就打印一条消息，指出这个人是老年人。
else:
	print('elder')


# 练习5-7：喜欢的水果 创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if 语句,检查列表中是否包含特定的水果。
# 将该列表命名为favorite_fruits ，并在其中包含三种水果。
favorite_fruits = ['apple','bananas','orange','lemon','melon']
# 编写5条if 语句，每条都检查某种水果是否包含在列表中。如果是，就打印一条消息，下面是一个例子。
# You really like bananas!
if 'apple' in favorite_fruits:
	print('You really like apple!')
if 'bananas' in favorite_fruits:
	print('You really like bananas!')
if 'orange' in favorite_fruits:
	print('You really like orange!')
if 'lemon' in favorite_fruits:
	print('You really like lemon!')
if 'melon' in favorite_fruits:
	print('You really like melon!')





