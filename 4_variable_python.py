import math
#用python算出-X-2X+3=0这个一元二次方程的解,求根公式X=(-b+-(b**2-(4*a*c)**(2/1)))/2a
a=-1
b=-2
c=3
print((-b+math.sqrt(b**2-4*a*c))/2*a)
print((-b-math.sqrt(b**2-4*a*c))/2*a)
#根据用户提供的数字来求出解
user_num1=int(input("请输入a的值:"))
user_num2=int(input("请输入b的值:"))
user_num3=int(input("请输入c的值:"))
