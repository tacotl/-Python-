"""
嘉宾名单 如果你可以邀请任何人一起共进晚餐
（无论是在世的还是故去的），你会邀请哪些人？请创建一个
列表，其中包含至少三个你想邀请的人，然后使用这个列表打
印消息，邀请这些人来与你共进晚餐。
"""
list1 = ['llf','fq','wyf']
for member in list1:
	print('邀请成员有：',member)


"""
修改嘉宾名单 你刚得知有位嘉宾无法赴约，因此
需要另外邀请一位嘉宾。
"""
# 以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
print('llf因行程原因无法赴约')

# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
list1[0] = 'chy'

# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
for member1 in list1:
	print('邀请成员变更为：',member1)

"""
添加嘉宾 你刚找到了一个更大的餐桌，可容纳更
多的嘉宾。请想想你还想邀请哪三位嘉宾。
"""
# 以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。
print('I find larger table,and I will invite other 3 people to come.')

# 使用insert() 将一位新嘉宾添加到名单开头。
list1.insert(0,'mh')

# 使用insert() 将另一位新嘉宾添加到名单中间。
list1.insert(2,'zqy')

# 使用append() 将最后一位新嘉宾添加到名单末尾。
list1.append('zr')

# 打印一系列消息，向名单中的每位嘉宾发出邀请。
print(list1)
for member2 in list1:
	print('更新后邀请成员：',member2)


"""
缩减名单 你刚得知新购买的餐桌无法及时送达，
因此只能邀请两位嘉宾。
"""
# 以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
print('Sorry everyone,meeting with an accident has happen,I just to invite 2 member to come')

# 使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
while len(list1) > 2:
	print(list1.pop() + '已被弹出')

# 对于余下两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
for mem in list1:
	print(mem + '您仍在受邀之列')

# 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
del list1[0]
del list1[0]
print('empty list1')

