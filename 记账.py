class Human:
    def __init__(self,n,a=1,):
        self.name = n # 姓名
        self.age = a # 年龄
        self.money = 0 # 财产
        self.skill = [] # 能力
    # 传授技能
    def teach(self,other,subject):
        other.skill.append(subject)
        print(self.name,'教',
              other.name,'学',subject)
    # 信息查询
    def print_info(self):
        print(self.age,'岁的',
              self.name,'有',
              self.money,'元，他学会了:',
              self.skill)
    # 赚钱
    def works(self,money):
        self.money += money
        print(self.name,'上班赚了',money,'元钱')
    # 借钱
    def brrow(self):
        pass


zhang3 = Human('张三',20)
li4 = Human('李四',22)

# 李四教张三Python
li4.teach(zhang3,'Python')
# 张三教李四画图
zhang3.teach(li4,'画图')
# 张三上班赚了10000元
zhang3.works(1000)



# 张三全部信息
zhang3.print_info()
# 李四全部信息
li4.print_info()
