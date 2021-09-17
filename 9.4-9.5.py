# 练习9-4：就餐人数 在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant 的实例。打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。

class Restaurant():

	def __init__(self, restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f'店名：{self.restaurant_name}')
		print(f'烹调类型：{self.cuisine_type}')

	def open_restaurant(self):
		print(f'{self.restaurant_name}餐厅正在营业!')


	# 添加一个名为set_number_served() 的方法，让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
	def set_number_served(self):
		if self.number_served > 0:
			print(f'就餐过人数：{self.number_served}')
		else:
			print(f'无就餐人数')

    # 添加一个名为increment_number_served() 的方法，让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
	def increment_number_served(self,number):
		if number > 0:
			self.number_served += number
			print(f'期望接待就餐人数：{self.number_served}')
		else:
			print(f'无期望接待人数')

restaurant = Restaurant('河边烧烤','烧烤')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 10
restaurant.set_number_served()
restaurant.increment_number_served(30)



# 练习9-5：尝试登录次数 在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。编写一个名为increment_login_attempts()的方法，将属性login_attempts 的值加1。再编写一个名为reset_login_attempts()的方法，将属性login_attempts 的值重置为0。
# 根据User 类创建一个实例，再调用方法increment_login_attempts()多次。打印属性login_attempts的值，确认它被正确地递增。然后，调用方法reset_login_attempts()，并再次打印属性login_attempts 的值，确认它被重置为0。
class User():
	"""docstring for User"""
	def __init__(self, first_name,last_name,sex,hobby):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.hobby = hobby
		self.login_attempts = 0

	def describe_user(self):
		print(f'名：{self.first_name}')
		print(f'姓：{self.last_name}')
		print(f'性别：{self.sex}')
		print(f'爱好：{self.hobby}')

	def greet_user(self):
		print(f'Welcome {self.first_name}!')

	#编写一个名为increment_login_attempts()的方法，将属性login_attempts 的值加1
	def increment_login_attempts(self):
			self.login_attempts += 1
	
	# 编写一个名为reset_login_attempts()的方法，将属性login_attempts 的值重置为0
	def reset_login_attempts(self):
		self.login_attempts = 0


user = User('Jimmy','Green','man','swimming')

user.describe_user()
user.greet_user()

# 调用方法increment_login_attempts()
user.increment_login_attempts()
# 打印属性login_attempts的值
print(user.login_attempts)

# 调用方法reset_login_attempts()
user.reset_login_attempts()
# 将属性login_attempts 的值重置为0
print(user.login_attempts)

user1 = User('Taylor','Green','woman','music')

# 调用方法increment_login_attempts()多次
for i in range(1,5):
	user1.increment_login_attempts()
# 打印属性login_attempts的值，确认它被正确地递增
	print(f'调用第{user1.login_attempts}次！')

# 调用方法reset_login_attempts()
user1.reset_login_attempts()
# 打印属性login_attempts 的值，确认它被重置为0
print(f'重置为{user1.login_attempts}')


