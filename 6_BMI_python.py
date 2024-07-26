#BMI=体重/(身高**2)
#嵌套选择结构
user_weight=float(input("请输入你的体重(单位:kg):"))
user_height=float(input("请输入你的身高(单位:m):"))
user_BMI=user_weight/(user_height**2)
print("您的BMI指数为:"+str(user_BMI))
if user_BMI <= 18.5:
    print("您的BIM值低于正常值，偏瘦，体重过低，需增加营养")
elif 18.5 <= user_BMI <= 24:
    print("您的BIM值位于正常值，均衡，正常范围值")
elif 24 <= user_BMI <= 28:
    print("您的BIM值超过正常值，超重，注意控制饮食，减肥")
else:
    print("您的BMI值严重超过正常值，肥胖，需严格控制饮食，尽快减肥。")
