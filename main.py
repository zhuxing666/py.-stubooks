##学生系统
#菜单
def showMenu():
    print('1.添加学生')
    print('2.删除学生')
    print('3.修改学生信息')
    print('4.查询单个学生信息')
    print('5.查询所有学生信息')
    print('6.退出系统')
#添加学生函数
stu_list=[]
def insert_student():
        name=input('请输入学生的姓名')
        for stu in stu_list:
            if stu['name']==name:
                print('学生信息存在')
                return
        age=input('请输入学生的年龄')
        gender=input('请输入学生性别')
        stu_dict={'name':name,'age':int(age),'gender':gender}
        stu_list.append(stu_dict)
        print('学生信息添加成功')

#删除学生
def remove_student():
    name=input('请输入你要操作的名字')
    for stu in stu_list:
        if stu['name']==name:
            stu_list.remove(stu)
            break
    else:
         print('学生信息不存在')

#修改学生信息
def modify_student():
    name=input('请输入你要操作的名字')
    for stu in stu_list:
        if stu['name']==name:
            stu['name'] == input("输入新的名字")
            stu['age']=int(input('请输入新的年龄:'))
            break
    else:
         print('学生信息不存在')

#查找学生信息
def search_student():
    name=input('请输入你要操作的名字')
    for stu in stu_list:
        if stu['name']==name:
            print(f'name:{stu["name"]},age:{stu["age"]},性别:{stu["gender"]}')
            break
    else:
         print('学生信息不存在')


#显示所有信息
def  show_all_info():
   if len(stu_list) :
        for stu in stu_list:
            print(f'name:{stu["name"]},age:{stu["age"]},性别:{stu["gender"]}')
   else:
       print('目前没有学生信息')


#封装的选择入口
def main():
    while True:
        showMenu()
        opt=input('请输入你操作的编号:')
        if opt=='1':
            insert_student()
            print('1.添加学生')
        elif opt=='2':
            remove_student()
            print('2.删除学生')
        elif opt == '3':
            modify_student()
            print('3.修改学生信息')
        elif opt == '4':
            search_student()
            print('4.查询单个学生信息')
        elif opt == '5':
            show_all_info()
            print('5.查询所有学生信息')
        elif opt == '6':
            print('6.欢迎下次使用！')
            break
        else:
            print('输入有误，请再次输入！')
            continue
        input('。。。。回车键继续操作。。。。')
main()
