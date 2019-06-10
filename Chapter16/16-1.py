"""
学生管理系统
主要特点：1.可以检测学号是否重复/有误（不为纯数字）
        2.可以检测手机号是否合法（是否为纯数字）
        3.可以检测性别是否为男或者女
        4.能选择性修个学生的某个属性信息，比如只修改某个学生的手机号码
        5.能够实现基本的增删改查
        6.优化了代码
"""
 
 
name_list = []  # 存储学生信息字典，学生信息用字典存，再用列表存储字典
 
 
# 菜单
def display_menu():
    print("-"*30)
    print("   学生管理系统  v8.8  ")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询单个学生信息")
    print("5.查询所有学生信息")
    print("6.退出系统")
    print("-"*30)
 
 
# 选择序号的获得
def get_choice():
    selected_key = input("请输入选择的序号：")
    return selected_key
 
 
# 检查性别是否合法
def check_sex(new_sex):
    flag = True
    while flag:
        if new_sex == '男' or new_sex == '女':
            flag = False
        else:
            new_sex = input("输入性别有误，请重新输入(男/女)：")
    return new_sex
 
 
# 检查电话号码是否合法
def check_phone(new_phone):
    flag = True
    while flag:
        if new_phone.isdigit():
            flag = False
        else:
            new_phone = input("您输入的电话号码有误，请重新输入：")
    return new_phone
 
 
# 检查学号是否重复或者有误
def check_id(new_id):
    flag = True
    while flag:
        # 先检查是不是纯数字再去考虑是否重复的事情，如果不是纯数字直接pass
        if new_id.isdigit():
            for i in range(len(name_list)):
                if name_list[i]['id'] == new_id:
                    new_id = check_id(input("您输入的学号重复，请重新输入："))
            flag = False
        else:
            new_id = input("您输入的学号有误，请重新输入：")
    return new_id
 
 
# 添加学生信息
def add_name():
    new_info = {}
    new_id = check_id(input("请输入学号："))
    new_info['id'] = new_id
    new_name = input("请输入姓名：")
    new_info['name'] = new_name
    new_sex = check_sex(input("请输入性别(男/女)："))
    new_info['sex'] = new_sex
    new_phone = check_phone(input("请输入电话号码："))
    new_info['phone'] = new_phone
    name_list.append(new_info)
    print("添加成功！")
 
 
# 查询所有学生信息
def find_all():
    print("="*30)
    for name in name_list:
        print(name['id'], name['name'], name['sex'], name['phone'])
    print("=" * 30)
 
 
# 删除学生信息
def del_name():
    del_id_is = input("请输入要删除的学生学号：")
    flag = False
    index = 0
    for i in range(len(name_list)):
        if name_list[i]['id'] == del_id_is:
            flag = True
            index = i
            break
    if flag:
        name_list.pop(index)
        print("删除成功！")
    else:
        print("学生未找到！请检查学号输入是否有误！")
 
 
# 名字修改细节函数
def choice_of_name(index):
    while True:
        choice = input("请输入要修改学生的(1.id 2.姓名 3.性别 4.电话号码，5.全部修改)：")
        if choice == '5':
            new_id = input("请输入新的学号：")
            name_list[index]['id'] = new_id
            new_name = input("请输入新的姓名：")
            name_list[index]['name'] = new_name
            new_sex = check_sex(input("请输入性别(男/女)："))
            name_list[index]['sex'] = new_sex
            new_phone = check_phone(input("请输入电话号码："))
            name_list[index]['phone'] = new_phone
            break
        elif choice == '1':
            new_id = input("请输入新的学号：")
            name_list[index]['id'] = new_id
            break
        elif choice == '2':
            new_name = input("请输入新的姓名：")
            name_list[index]['name'] = new_name
            break
        elif choice == '3':
            new_sex = check_sex(input("请输入性别(男/女)："))
            name_list[index]['sex'] = new_sex
            break
        elif choice == '4':
            new_phone = check_phone(input("请输入电话号码："))
            name_list[index]['phone'] = new_phone
            break
        else:
            print("输入有误，请重新输入！")
 
 
# 修改学生信息
def re_name():
    id_is = input("请输入要修改的学生学号：")
    flag = False
    index = 0
    # 先找到要修改的学生的下标
    for i in range(len(name_list)):
        if name_list[i]['id'] == id_is:
            flag = True
            index = i
            break
    if flag:
        choice_of_name(index)
        print("修改成功！")
    else:
        print("修改失败，学生信息未找到！")
 
 
# 查询单个学生信息
def find_name():
    find_id_is = input("请输入要查询的学生学号：")
    flag = False
    index = 0
    for i in range(len(name_list)):
        if name_list[i]['id'] == find_id_is:
            flag = True
            index = i
            break
    if flag:
        print("学生查询到，学生信息为：")
        print(name_list[index]['id'], name_list[index]['name'], name_list[index]['sex'], name_list[index]['phone'])
    else:
        print("学生未找到！")
 
 
def main():
    exit_name = True
    while exit_name:
        display_menu()
        key = get_choice()
        if key == '1':
            add_name()
        elif key == '2':
            del_name()
        elif key == '3':
            re_name()
        elif key == '4':
            find_name()
        elif key == '5':
            find_all()
        elif key == '6':
            exit_name = False
        else:
            print("请输入正确的数值！")
 
 
main()