# 练习6-7：人们 在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people 的列表中。遍历这个列表，将其中每个人的所有信息都打印出来。
human1 = {
	'first_name':'Fly',
	'last_name':'Swift',
	'age':26,
	'city':'Dazhou'
}

human2 = {
	'first_name':'Taylor',
	'last_name':'Swift',
	'age':32,
	'city':'NewYork'
}

human3 = {
	'first_name':'Taylor',
	'last_name':'Tom',
	'age':28,
	'city':'Sydney'
}

people = [human1,human2,human3]

for hum in people:
	print(hum)

# 练习6-8：宠物 创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets的列表中，再遍历该列表，并将有关每个宠物的所有信息都打印出来。
pet_1 = {
	'type':'dog',
	'name':'Taylor'
}

pet_2 = {
	'type':'cat',
	'name':'Marry'
}

pet_3 = {
	'type':'fish',
	'name':'Lily'
}
pets = [pet_1,pet_2,pet_3]
for pet in pets:
	print(pet)

# 练习6-9：喜欢的地方 创建一个名为favorite_places 的字典。在这个字典中，将三个人的名字用作键，并存储每个人喜欢的1～3个地方。为了让这个练习更有趣些，可以让一些朋友说出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
favorite_plages = {
	'Kelly':['London','NewYork'],
	'Alex':['Tokyo','Osaka'],
	'Echo': ['Prague']
}
for name,cities in favorite_plages.items():
	print(f'name:{name}')
	for city in cities:
		print(f'city:{city}')

# 练习6-10：喜欢的数2 修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数，然后将每个人的名字及其喜欢的数打印出来。
number = {
	'llf':[1,8],
	'fq':[2,4],
	'mh':[7,6,13,2],
	'chy':[5,1],
	'yrx':[8,5]
}
for name,nums in number.items():
	print(f'name:{name}')
	for num in nums:
		print(f'favourite number:{num}')

# 练习6-11：城市 创建一个名为cities 的字典，将三个城市名用作键。对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。在表示每座城市的字典中，应包含country 、population和fact等键。将每座城市的名字以及有关信息都打印出来。
cities = {
	'London' : {
		'country':'British',
		'population':'860w',
		'fact':'capical'
	},
	'Paris' : {
		'country':'France',
		'population':'221w',
		'fact':'capical'
	},
	'Prague' : {
		'country':'Czech',
		'population':'117w',
		'fact':'capical'
	}
}
for city,city_info in cities.items():
	print(f'city:{city}')
	print(f'country:{city_info["country"]}')
	print(f'population:{city_info["population"]}')
	print(f'fact:{city_info["fact"]}\n')
