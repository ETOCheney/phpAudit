# coding=utf-8
from Model import Function
from Model import Variable

'''
文件模型 用来存储文件的方法行数以及调用的变量
'''
class File:
    def __init__(self,filename):
        self.file_name = filename
        # 文件所有方法
        self.funcs = {}
        # 文件所有变量
        self.vars = {}
        # 危险代码
        self.danger_line = {}

    # 添加方法
    def add_func(self,func,line):
        try:
            function = Function.Function(func, line)
            self.funcs[func] = function
        except Exception as e:
            print(e)
            exit(10087)

    # 获取某个方法
    def get_func(self,func_name):
        if func_name in self.funcs:
            return self.funcs[func_name]
        else:
            return None

    # 添加变量
    def add_variable(self,var_name,line):
        try:
            variable = Variable.Variable(var_name,line)
            self.vars[var_name] = variable
        except Exception as e:
            print(e)
            exit(10088)

    # 获取某个变量
    def get_variable(self,var_name):
        if var_name in self.vars:
            return self.vars[var_name]
        else:
            return None

    # 获取文件地址和文件名
    def get_file_name(self):
        return self.file_name