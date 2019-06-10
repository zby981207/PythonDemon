#自定义计数空格
def count_space(list):
    n = len(list)
    count=0
    for i in range(n):
        if list[i] == ' ':
            count+=1
    print(count)

#输入一个数组
x = input("请输入一组内容")
count_space(x)