#使用for循环语句求出1到100的和
#定义一个变量
#range表示整数序列
num = 0
for i in range(1,101):
    num = num + i
print("1到100的和为:"+str(num))

#使用for 循环找出体温不正常的人
# warm_num = [36.0,36.6,27.0,37.8,38.2]
# for warm in warm_num:
#     if warm >= 38:
#         print(warm)
#         print("体温异常")
warm_num = {"张三":36.0,"李四":36.8,"王五":37.8,"刘六":38.2}
for id,warm in warm_num.items():
    if warm >= 37.6:
        print("体温异常的是:"+ id)