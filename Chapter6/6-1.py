#假设某游戏项目中需要定义一个精灵对象，其所需的属性有体重、颜色、高度、能量；
#具有行走、跳跃、进食能力，且行走和跳跃会消耗能量、进食增加能量。
#请根据描述定义这个精灵类。

class PetA:
    def __init__(self,weight,color,height,eneryg=100):#定义属性
        self.weight = weight
        self.color = color
        self.height = height
        self.energy = energy

    def move(self):#行走能力，消耗能量
        self.energy -= 1

    def jump(self):#跳跃能力，消耗更多能量
        self.energy -= 3

    def eat(self,n):#进食能力，吃多少加多少
        self.energy += n