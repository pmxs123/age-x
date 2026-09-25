print("欢迎来到哥斯拉酒吧")

wa=input("请输入你的姓名：")
asb=int(input("请输入你的年龄:"))
vp=int(input("你的VIP等级是多少？:"))

if asb>18:
    print()
    print(wa)
    print("已成年允许进入")
    
    if vp>50:
        print("你的vip已达到50级，享有专属服务😘")
    else:
        print("你是普通用户，没有专属服务")
else:
    print(wa)
    print("你是未成年不能进入")
