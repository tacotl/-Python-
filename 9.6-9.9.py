# 练习9-6：冰激凌小店 冰激凌小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承为完成练习9-1或练习9-4而编写的Restaurant 类。这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。添加一个名为flavors的属性，用于存储一个由各种口味的冰激凌组成的列表。编写一个显示这些冰激凌的方法。创建一个IceCreamStand 实例，并调用这个方法。
class Restaurant():

	def __init__(self, restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f'店名：{self.restaurant_name}')
		print(f'烹调类型：{self.cuisine_type}')

	def open_restaurant(self):
		print(f'{self.restaurant_name}餐厅正在营业!')

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name,cuisine_type,flavors=[]):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = flavors

	# 显示这些冰激凌的方法
	def describe_flavors(self):
		print(f'喜欢的冰淇淋：{self.flavors}')

icecream = IceCreamStand('河边冰淇淋屋','甜品',['巧克力','香草','奶茶'])
icecream.describe_flavors()


# 练习9-7：管理员 管理员是一种特殊的用户。编写一个名为Admin的类，让它继承为完成练习9-3或练习9-5而编写的User类。添加一个名为privileges的属性，用于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user"等）组成的列表。编写一个名为show_privileges()的方法，显示管理员的权限。创建一个Admin 实例，并调用这个方法。
class User():
	def __init__(self, first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print(f'名：{self.first_name}')
		print(f'姓：{self.last_name}')

	def greet_user(self):
		print(f'Welcome {self.first_name}!')

class Admin(User):
	def __init__(self, first_name,last_name,privilege=[]):
		super().__init__(first_name,last_name)
		self.privileges = privilege

	# 编写show_privileges()，显示管理员的权限
	def show_privileges(self):
		print(f'Admin:{str(self.privileges)}')

admin = Admin('Jimmy','Green',["can add post" ,"can delete post" "can ban user"])
admin.show_privileges()


# 练习9-8：权限 编写一个名为Privileges 的类，它只有一个属性privileges ，其中存储了练习9-7所述的字符串列表。将方法show_privileges()移到这个类中。在Admin 类中，将一个Privileges实例用作其属性。创建一个Admin 实例，并使用方法show_privileges() 来显示其权限。
class User():
	def __init__(self, first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print(f'名：{self.first_name}')
		print(f'姓：{self.last_name}')

	def greet_user(self):
		print(f'Welcome {self.first_name}!')

class Privileges():
	def __init__(self,privilege=["can add post" ,"can delete post" "can ban user"]):
		self.privileges = privilege

	def show_privileges(self):
		print(f'Admin:{str(self.privileges)}')

class Admin(User):
	def __init__(self, first_name,last_name):
		super().__init__(first_name,last_name)
		self.privileges = Privileges()

admin = Admin('Jimmy','Green',)
admin.privileges.show_privileges()

# 练习9-9：电瓶升级 在本节最后一个electric_car.py版本中，给Battery 类添加一个名为upgrade_battery() 的方法。该方法检查电瓶容量，如果不是100，就将其设置为100。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，然后对电瓶进行升级，并再次调用get_range()。你将看到这辆汽车的续航里程增加了。
class Car():
	# 一次模拟汽车的简单尝试。
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	
	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")
	
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	
	def increment_odometer(self, miles):
		self.odometer_reading += miles

class Battery():
	# 一次模拟电动汽车电瓶的简单尝试。
	def __init__(self, battery_size=75):
		# 初始化电瓶的属性。
		self.battery_size = battery_size

	def describe_battery(self):
		# 打印一条描述电瓶容量的消息。
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
	# 打印一条消息，指出电瓶的续航里程。
		if self.battery_size == 75:
			range = 260
		# 判断battery_size是否为100
		elif self.battery_size == 100:
			range = 315
		msg = str(range)
		print(f'续航里程：{msg}') 

	def upgrade_battery(self):
		if self.battery_size != 100:
			# 将100赋值给battery_size
			self.battery_size =100

class ElectricCar(Car):
	"""电动汽车的独特之处。"""
	def __init__(self, make, model, year):
	
	# 初始化父类的属性。
	# 再初始化电动汽车特有的属性。
	
		super().__init__(make, model, year)
		self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
# print('升级后' + str(my_tesla.battery.get_range()))


