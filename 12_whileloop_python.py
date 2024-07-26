print("这是一个求平均值的程序！")
one = 0
two = 0
user_num = input("请输入一个数（等待数字输入完成后)用q终止程序:")
while user_num != "q":
    num = float(user_num)
    one += num
    two += 1
    user_num = input("请输入一个数（等待数字输入完成后)用q终止程序:")
if two == 0:
    result = 0
else:
    result = one / two
    print("平均值为:" + str(result))
