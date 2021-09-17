# 练习8-12：三明治 编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
def  sandwichs(*foods):
		print(foods)

sandwichs('meat','egg','bread')


# 练习8-13：用户简介 复制前面的程序user_profile.py，在其中调用build_profile() 来创建有关你的简介。调用这个函数时，指定你的名和姓，以及三个描述你的键值对。
def buile_profile(first,last,**user_info):
	# dic1 = {}
	user_info['first_name'] = first
	user_info['last_name'] = last
	# for key,value in user_info.items():
	# 	dic1[key] = value
	# return dic1
	return user_info
user_profile = buile_profile('albert', 'einstein',
							location = 'princeton',
							field = 'physics',
							hobby = 'swimming')
print(user_profile)


# 练习8-14：汽车 编写一个函数，将一辆汽车的信息存储在字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。这样调用该函数：提供必不可少的信息，以及两个名称值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。
def make_car(producer,car_type,**car_msg):
	car_msg['producer'] = producer
	car_msg['type'] = car_type
	return car_msg

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
