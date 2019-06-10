def User(name,passw):
     
     names=[{'name':'jhon','passw':'2345kdd','usertype':1},
     {'name':'zkz','passw':'0725abc','usertype':2},
           {'name':'wxj','passw':'0829wxj','usertype':6},
           {'name':'jhon','passw':'2345kdd','usertype':9}]
     for line in names:

        if line['name']==name and line['passw']==passw:
        
                  #print(name,passw)
                  type=line['usertype']
                  #print(type)
                  print('验证成功：%s'% type)
                  break #注意：加和不加break大不一样，重点体会
     else:
          print('验证失败！')

     




name=input("请输入姓名：")
passw=input("请输入密码：")
User(name,passw)
     
          
