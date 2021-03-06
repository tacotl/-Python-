# 练习6-1：人使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键first_name、last_name 、age 和city 。将存储在该字典中的每项信息都打印出来。
human = {
	'first_name':'Fly',
	'last_name':'Swift',
	'age':26,
	'city':'Dazhou'
}
print(human)

# 练习6-2：喜欢的数 使用一个字典来存储一些人喜欢的数。请想出5个人的名字，并将这些名字用作字典中的键；找出每个人喜欢的一个数，并将这些数作为值存储在字典中。打印每个人的名字和喜欢的数。为了让这个程序更有趣，通过询问朋友确保数据是真实的。
number = {
	'llf':1,
	'fq':2,
	'mh':7,
	'chy':5,
	'yrx':8
}
i = number['fq']
print("fq's favorite number " + str(i))

# 练习6-3：词汇表 Python字典可用于模拟现实生活中的字典。为避免混淆，我们将后者称为词汇表。
# 想出你在前面学过的5个编程术语，将其用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
vocabulary = {
	'app':'应用程序',
	'programm':'编程',
	'dynamic':'动态 ',
	'link':'链接',
	'library':'文字库'
}
# 以整洁的方式打印每个术语及其含义。为此，可先打印术语，在它后面加上一个冒号，再打印其含义；也可在一行打印术语，再使用换行符（\n）插入一个空行，然后在下一行以缩进的方式打印其含义
print('app' + ':' + vocabulary['app'] + '\n')
print('programm' + ':' + vocabulary['programm'] + '\n')
print('dynamic' + ':' + vocabulary['dynamic'] + '\n')
print('link' + ':' + vocabulary['link'] + '\n')
print('library' + ':' + vocabulary['library'] + '\n')
