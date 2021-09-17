# 使用sorted() 按字母顺序打印这个列表，同时不要修改它。
travel = ['chongqin','shanghai','beijing','xiamen','lhasa']
print(sorted(travel))

# 再次打印该列表，核实排列顺序未变。
print(travel)

# 使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print(sorted(travel,reverse=True))

# 再次打印该列表，核实排列顺序未变。
print(travel)

# 使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
travel.reverse()
print(travel)

# 使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
travel.reverse()
print(travel)

# 使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
travel.sort()
print(travel)

# 使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
travel.sort(reverse=True)
print(travel)