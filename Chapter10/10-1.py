num = 1 #num1 当前模块的全局变量
def outer():
    num = 10 #num2 outer作用域的局部变量
    def inner():
        #global num  num3 既是全局变量num1，又是inner局部变量
        nonlocal num #num3 既是inner局部变量，又是外层outer局部变量
        print(num) #输出outer的局部变量num2
        num = 100 #将100赋值给num
        print(num) #num3 100 输出inner的局部变量num3
    inner() # inner()函数结束，num3作为外层变量(outer局部变量)被保留成为num2
    print(num) #num2 100 输出outer的局部变量num2(在inner中被改变)
outer() #outer函数结束，num2作为outer的局部变量被释放
print(num) #num1 1 输出全局变量中的num1