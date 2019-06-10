#编程实现对用户输入的整数进行求和与求平均值。
#当用户输入的不是整数时跳过，并提示而不中止程序
i = 1
sum = 0

while(1):
    n = input('请输入第%d个数:'%i)
    if n.isdigit():#判断是否是整数
        n = int(n)
        i += 1
        sum += n
    else:
        print('您输入的不是整数，请重新输入')
    print('目前的和是：',sum,'平均值为',sum/(i-1))