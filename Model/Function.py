# coding=utf-8

'''
函数模型 用来记录函数所在的行数以及调用的变量
'''
class Function:
    def __init__(self,func_name,line):
        self.func_name = func_name   # 函数名
        self.line = line  # 所在行数

    # 获取行数
    def get_line(self):
        return self.line

    # 获取方法名
    def get_func_name(self):
        return self.func_name