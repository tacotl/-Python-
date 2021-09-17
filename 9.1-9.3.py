# 练习9-1：餐馆 创建一个名为Restaurant 的类，为其方法__init__() 设置属性restaurant_name 和cuisine_type。创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性,再调用前述两个方法。
class Restaurant():

	def __init__(self, restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f'店名：{self.restaurant_name}')
		print(f'烹调类型：{self.cuisine_type}')

	def open_restaurant(self):
		print(f'{self.restaurant_name}餐厅正在营业!')

restaurant = Restaurant('河边烧烤','烧烤')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 练习9-2：三家餐馆 根据为完成练习9-1而编写的类创建三个实例，并对每个实例调用方法describe_restaurant() 。
mc_restaurant = Restaurant("McDonald's",'fastfood')
kfc_restaurant = Restaurant('KFC','fastfood')
pizzhub_restaurant = Restaurant('Pizza Hub','pizza')

mc_restaurant.describe_restaurant()
kfc_restaurant.describe_restaurant()
pizzhub_restaurant.describe_restaurant()

# 练习9-3：用户 创建一个名为User 的类，其中包含属性first_name 和last_name ，以及用户简介通常会存储的其他几个属性。在类User 中定义一个名为describe_user()的方法，用于打印用户信息摘要。再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
class User():
	"""docstring for User"""
	def __init__(self, first_name,last_name,sex,hobby):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.hobby = hobby

	def describe_user(self):
		print(f'名：{self.first_name}')
		print(f'姓：{self.last_name}')
		print(f'性别：{self.sex}')
		print(f'爱好：{self.hobby}')

	def greet_user(self):
		print(f'Welcome {self.first_name}!')

user1 = User('Jimmy','Green','man','swimming')
user2 = User('Taylor','Swift','woman','music')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

		



