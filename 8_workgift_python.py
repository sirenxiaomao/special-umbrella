house_work =int(input("这个月做的家务次数:"))
home_work =int(input("这个月的家庭作业完成次数:"))
school_late =int(input("这个月上学迟到次数:"))
if (house_work >= 10 and home_work >=15 and not school_late >0 ):
    print("获得一个swich!")
else:
    print("获得一顿七匹狼套餐!")