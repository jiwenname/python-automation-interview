# 考题1   Python中单引号、双引号、三引号定义字符串有什么区别？
# 答     单引号('')和双引号("")在定义字符串的功能上完全相同，这样的语法设计主要为了代码的可读性和编写便利性。如果一个字符串本身携带一种引号，可以使用另外一种
# 引号进行定义。合理使用可避免使用转义符 如It's a name 写成"It's a name" 而不是It\s a name
# 三引号(""" """")用来定义多行字符串字面量，可以保留字符串的换行符和各种缩进，主要用来编写函数和类的文档字符串(docstring)和嵌入大段的sql和HTML模板

# 考题2 运行你的脚本时，input()得到的年龄是字符串，如何确保存入字典的是整数？这会引发什么问题？
def get_use_info():
    user_info = {}
    #获取输入框内容并去除两侧的空格
    user_name = input("请输入您的名字").strip()
    # 判断如果user_name为空或者假的,user_name是否为None,空字典，空列表，空字符串
    if not user_name:
        print("请输入正确的名字")
    user_info['username'] = user_name
    while True:
        user_age = input("请输入您的年龄").strip()
        try:
            # 强转输入框内容为int类型
            user_age = int(user_age)
            if 0<= user_age <= 150:
                user_info['age'] = user_age
            else:
                print("请输入0-150之间的年龄")
        except ValueError:
            print("请输入有效的数字")
        return user_info

if __name__ == '__main__':
    user = get_use_info()
    print(user)
#