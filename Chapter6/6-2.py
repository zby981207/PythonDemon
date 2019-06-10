#定义一个会跳跃、爬行、飞行、用身子撞击的FinalAnt
class FinalAnt:
    def __init__(self,x=0,y=0,color="black"):
        self.x = x
        self.y = y
        self.color = color

    def jump(self,x,y):#跳跃
        self.x = 2 * x
        self.y = 2 * y
        print('跳跃')
        self.info()

    def crawl(self,x,y):#爬行
        self.x = x
        self.y = y
        print("爬行")
        self.info()

    def info(self):
        print("当前位置：(%d,%d)"%(self.x,self.y))

    def fly(self,x,y):#飞行
        print('飞行')
        self.x = x
        self.y = y
        self.info()
        
    def attack(self):#撞击
        print('撞击')