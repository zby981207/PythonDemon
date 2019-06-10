import datetime
class Person:
    def __init__(self, name, height, weight, bod=datetime.datetime.now()):
        self.name = name
        self.height = height
        self.weight = weight
        self.bod = bod

    def isHealthy(self):
        # Insturction that I can't understand
        # 分别输出这个人的年龄、体重是否达标（体重范围为身高-110+20，身高-110+20）
        self.age = datetime.datetime.now().year - self.bod.year
        print("%s, %d 岁, " % (self.name, self.age), end=" ")
        if self.weight < self.height -110+20:
            print("健康")
        else:
            print("不健康")

if __name__ == "__main__":
    me = Person("郑博洋", 189, 85, datetime.date(1998, 12,7))
    me.isHealthy()
