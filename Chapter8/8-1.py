#编写一个模块来包含数学中的求平方、求绝对值、判断素数
#这个模块可以独立运行，并输出一个数的平方、绝对值、是否素数
import math
#平方
def pingfang(num):
    num = num*num
    print('平方是',num)
#绝对值
def jueduizhi(num):
    if num<0:
        num = -num
    else:
        num = num
    print('绝对值是',num)
    
#判断是否素数
def sushu(num):
    # 素数大于 1
    if num > 1:
        # 查看是否有其他因子
        for i in range(2, num//2+1):
            if (num % i) == 0:
                print(num,"是素数")
                break
        else:
            print(num, "不是素数")

    # 如果输入的数字小于或等于 1，不是素数
    else:
        print(num, "不是素数")


if __name__ == '__main__':
    #用户输入一个数字
    num = int(input('请输入一个数字：'))
    pingfang(num)
    jueduizhi(num)
    sushu(num)