# 练习8-3：T恤 编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
# 使用位置实参调用该函数来制作一件T恤，再使用关键字实参来调用这个函数。
def make_shirt(size,sample):
	print(f'The shirt size is {size} and type is {sample}')
make_shirt("M","YYDS")


# 练习8-4：大号T恤 修改函数make_shirt() ，使其在默认情况下制作一件印有“I love Python”字样的大号T恤。调用这个函数来制作：一件印有默认字样的大号T恤，一件印有默认字样的中号T恤，以及一件印有其他字样的T恤（尺码无关紧要）。
def make_shirt(size1 = 'L',sample1 = 'I love Python'):
	print(f'The shirt size is {size1} and type is {sample1}')
make_shirt()
make_shirt(size1 = 'M')
make_shirt(sample1 = 'Hello')


# 练习8-5：城市 编写一个名为describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，下面是一个例子。
# Reykjavik is in Iceland.
# 给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
def describe_city(city,country = 'Japan'):
	print(f'{city} is in {country}')
describe_city(city = 'Tokyo')
describe_city(city = 'NewYork',country = 'Amercia')
describe_city(city = 'Osaka')


