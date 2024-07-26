#('键盘'，'键帽'，'鼠标'，'电竞椅'，'显示器'）
shopping_list =[]
#在表中插入数据
shopping_list.append("键盘")
shopping_list.append("键帽")
shopping_list.append("鼠标")
shopping_list.append("电竞椅")
shopping_list.append("显示器")
#删除表中数据
shopping_list.remove("显示器")
#用索引查看字符长度
print(len(shopping_list))
#选定一个字符数显示其内容
print(shopping_list)
print(shopping_list[1])
#从数组中选出最大最小数并排序
price =[]
price.append(599)
price.append(12)
price.append(388)
price.append(233)
maxprice=max(price)
minprice=min(price)
sortedprice=sorted(price)
print(max(price))
print(min(price))
print(sorted(price))