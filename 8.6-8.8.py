# 练习8-6：城市名 编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面的字符串：
# "Santiago, Chile"
# 至少使用三个城市国家对来调用这个函数，并打印它返回的值。
def city_country(city,country):
	all = f'{city},{country}'
	return all.title()
print(city_country('tokyo','japan'))
print(city_country('santiago','chile'))
c1 = city_country('beijing','china')
print(c1)

# 练习8-7：专辑 编写一个名为make_album() 的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给函数make_album() 添加一个默认值为None 的可选形参，以便存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将该值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
def make_album(singer,album,song= ""):
	# 它创建一个描述音乐专辑的字典
	album1 = {'singer':singer,
			 'album':album,
	}
	if song:
		# 放进album1列表中
		album1['song'] = song
	return album1
a1 = make_album('Taylor','22','22')
a2 = make_album('keyakizaka','silentmajority')
a3 = make_album('arashi','夏疾风')
print(a1)
print(a2)
print(a3)

# 练习8-8：用户的专辑 在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入专辑的歌手和名称。获取这些信息后，使用它们来调用函数make_album() 并将创建的字典印出来。在这个while 循环中，务必提供退出途径。
while True:
	singer = input('please input singer:')
	album = input('please input album:')
	# 创建的字典印出来
	album2 = {singer,album}
	print(album2)
	problem = input('Do u want to quit?')
	if problem == 'Y':
		break


