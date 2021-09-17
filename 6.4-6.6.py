# 练习6-4：词汇表2 现在你知道了如何遍历字典，可以整理为完成练习6-3而编写的代码，将其中的一系列函数调用print()替换为一个遍历字典中键和值的循环。确定该循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
vocabulary = {
	'app':'应用程序',
	'programm':'编程',
	'dynamic':'动态 ',
	'link':'链接',
	'library':'文字库',
	'key':'键名',
	'float':'浮点数',
	'int':'整数',
	'list':'列表',
	'string':'字符串'
}
for key1,value1 in vocabulary.items():
	print(f'{key1}:{value1}\n')

# 练习6-5：河流 创建一个字典，在其中存储三条重要河流及其流经的国家。例如，一个键值对可能是'nile': 'egypt'。
rivers = {
	'nile':'egypt',
	'yangtze':'china',
	'amazon':'braliz'
}

# 使用循环为每条河流打印一条消息，下面是一个例子。
# The Nile runs through Egypt.
for rname,country in rivers.items():
	print(f'The {rname.title()} runs through {country.title()} \n')

# 使用循环将该字典中每条河流的名字打印出来。
for rname in rivers.keys():
	print(rname.title())

# 使用循环将该字典包含的每个国家的名字打印出来。
for country in rivers.values():
	print(country.title())

# 练习6-6：调查 在6.3.1节编写的程序favorite_languages.py中执行以下操作。
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
people = ['sarah','phil','eva','taylor','marry','tom']
# 遍历这个人员名单。对于已参与调查的人，打印一条消息表示感谢；对于还未参与调查的人，打印一条消息邀请他参加。
for name in people:
	if name in favorite_languages.keys():
		print('Thank you')
	else:
		print('I want to invite you to come')
