"""
作者：小宇
日期：2021年12月16日
"""

import time
class Bike:
    def __init__(self, NO, age, state=0):
        self.NO = NO
        self.age = age
        self.state = state  # 0表示待租借，1表示已租借

    def __str__(self):
        if self.state == 0:
            status = "待租借"
        else:
            status = "已租借"
        return "车辆编号%s,已经使用%d年,车辆状态：%s" % (self.NO, self.age, status)


# bike_1 = Bike(1001, 2)
# print(bike_1)

class Manage:
    bikes = []  #存放的是Bike类

    def __init__(self):
        bike_1 = Bike(1001, 2)
        bike_2 = Bike(1002, 1)
        bike_3 = Bike(1003, 1)
        self.bikes.append(bike_1)
        self.bikes.append(bike_2)
        self.bikes.append(bike_3)

    def menu(self):  # 菜单
        print('------欢迎使用共享单车租借系统------')
        while True:
            time.sleep(2)
            index = int(input('1.查看所有车辆信息\n2.共享车辆\n3.租借车辆\n4.归还车辆\n5.退出系统\n请输入要进行的操作:'))
            if index == 1:
                self.info()

            elif index == 2:
                self.share()

            elif index == 3:
                self.lease()

            elif index == 4:
                self.ret()

            elif index == 5:
                print("------小宇出品，必属精品------")
                break
            else:
                print("想必小主是输错了吧，请再试一遍")

    def info(self):  # 查询所有车辆
        for i in self.bikes:
            print(i)

    def share(self):  # 共享
        flag = True
        while flag:
            new_NO = int(input("请输入车辆的编号："))
            for i in self.bikes:
                if i.NO == new_NO:
                    print("对不起，您输入的编号已被使用，请重试")
                    break
            else:
                flag = False
        new_age = int(input("请输入车辆的已使用年数："))
        new_bike = Bike(new_NO, new_age)
        self.bikes.append(new_bike)
        print("车辆共享成功，感谢您的支持！")

    def lease(self): #借出
        flag = True
        while flag:
            lease_NO = int(input("请输入要租借的车辆编号："))
            for i in self.bikes:
                if i.NO == lease_NO:
                    if i.state == 1:
                        print("该车已被租借，请重新选择")
                        break
                    else:
                        flag = False
                        i.state = 1
                        print("车辆租借成功")
                        break
            else:
                print("未找到对应的车辆，想必小主是输错了吧，请重新输入")

    def ret(self): #归还
        flag = True
        while flag:
            ret_NO = int(input("请输入要归还的车辆编号："))
            for i in self.bikes:
                if i.NO == ret_NO:
                    if i.state == 0:
                        print("该车尚未被租借，想必小主是输错了吧，请重新选择")
                        break
                    else:
                        flag = False
                        i.state = 0
                        print("车辆归还成功")
                        break
            else:
                print("未找到对应的车辆，想必小主是输错了吧，请重新输入")

user = Manage()
user.menu()