#自定义排序函数(冒泡法)
def list_sort(list):
    n = len(list)
    for i in range(n-1):
        for j in range(i+1,n):
            if list[i]<list[j]:
                list[i],list[j]=list[i],list[j]
            else:
                list[i],list[j]=list[j],list[i]

#输入一个数组
x = input("请输入一些列数字")
xlist = x.split(" ")
xlist = [int(xlist[i]) for i in range(len(xlist))]
print("输入的数组为")
print(xlist)#打印数组

list_sort(xlist)#排序
print("排序……")
print(xlist)