# 练习8-9：消息 创建一个列表，其中包含一系列简短的文本消息。将该列表传递给一个名为show_messages() 的函数，这个函数会打印列表中的每条文本消息。
def show_messages(text):
	for a in text:
		msg = f'{a} is a message!'
		print(msg)
text1 = ['aaa','bbb','ccc']
print_message = show_messages(text1)

# 练习8-10：发送消息 在你为完成练习8-9而编写的程序中，编写一个名为send_messages()的函数，将每条消息都打印出来并移到一个名为sent_messages 的列表中。调用函数send_messages()，再将两个列表都打印出来，确认正确地移动了消息。
def show_messages(show_msg):
	for msg in show_msg:
		print(msg)

def send_messages(show_msg,send_msg):
	while show_msg:
		current_msg = show_msg.pop()
		print(f'Sent_messages:{current_msg}')
		send_msg.append(current_msg)

show_msg = ['abc','cba','nba']
send_msg = []

show_messages(show_msg)
send_messages(show_msg,send_msg)

# 练习8-11：消息归档 修改你为完成练习8-10而编写的程序，在调用函数send_messages() 时，向它传递消息列表的副本。调用函数send_messages()后，将两个列表都打印出来，确认保留了原始列表中的消息。
def show_messages(show_msg):
	for msg in show_msg:
		print(msg)

def send_messages(show_msg,send_msg):
	while show_msg:
		current_msg = show_msg.pop()
		print(f'Sent_messages:{current_msg}')
		send_msg.append(current_msg)

show_msg = ['llf','fq','chy']
send_msg = []

show_messages(show_msg)
send_messages(show_msg[:],send_msg)





