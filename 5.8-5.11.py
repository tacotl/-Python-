# 练习5-8：以特殊方式跟管理员打招呼 创建一个至少包含5个用户名的列表，且其中一个用户名为'admin' 。想象你要编写代码，在每位用户登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。
# 如果用户名为'admin' ，就打印一条特殊的问候消息，如
# 下所示。
# Hello admin, would you like to see a status report?
users = ['admin','taylor','grey','marry','lisa']
for user in users:
	if user == 'admin':
		print('Hello admin, would you like to see a status report?')
	else:
	# 否则，打印一条普通的问候消息，如下所示。
	# Hello Jaden, thank you for logging in again.
		print(f'Hello {user},thank you for logging in again.' )

# 练习5-9：处理没有用户的情形 在为完成练习5-8编写的程序中，添加一条if 语句，检查用户名列表是否为空。
# 如果为空，就打印如下消息。
# We need to find some users!
# 删除列表中的所有用户名，确定将打印正确的消息。
users = []
if users:
	for user in users:
		if user == 'admin':
			print('Hello admin')
		else:
			print(f'having user {user}')
else:
	print('We need to find some users!')

# 练习5-10：检查用户名 按下面的说明编写一个程序，模拟网站如何确保每位用户的用户名都独一无二。
# 创建一个至少包含5个用户名的列表，并将其命名为current_users 。
current_users = ['llf','fq','wyf','chy','zqy']
# 再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users 中。
new_users = ['lqq','mh','sxr','Llf','tlj']
# 遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。如果是，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
for new_user in users:
	if new_user in current_users:
		print('please input other user')
	else:
		print('user is not be use')

# 确保比较时不区分大小写。换句话说，如果用户名'John' 已被使用，应拒绝用户名'JOHN'。（为此，需要创建列表current_users的副本，其中包含当前所有用户名的小写版本。）
current_users = ['LLF','fq','WYF','chy','mh']
new_users = ['llf','FQ','wyf','CHY','MH']
for new_user in new_users:
		if new_user.lower() in current_users:
			print('Sorry,this name has been used')
		else:
			print('Succeed')

# 练习5-11：序数 序数表示位置，如1st和2nd。序数大多以th结尾，只有1、2和3例外。
# 在一个列表中存储数字1～9。
nums = [1,2,3,4,5,6,7,8,9]
# 遍历这个列表。
for num in nums:
	# 在循环中使用一个if-elif-else 结构，以打印每个数字对应的序数。输出内容应为"1st 2nd 3rd 4th 5th 6th 7th 8th 9th" ，但每个序数都独占一行。
	if num == 1:
		print(f'{num}st')
	elif num == 2:
		print(f'{num}nd')
	elif num == 3:
		print(f'{num}rd')
	else:
		print(f'{num}th')
