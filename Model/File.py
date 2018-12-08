# coding=utf-8
from Model import Function

'''
文件模型 用来存储文件的方法行数以及调用的变量
'''
class File:
    def __init__(self,filename):
        self.file_name = filename
        self.function = {}

    # 添加方法
    def add_func(self,func,line,var=[]):
        try:
            function = Function.Function(func, line, var)
            self.function[func] = function
        except Exception as e:
            print(e)
            exit(10087)

    # 获取方法
    def get_func(self,func_name):
        if func_name in self.function:
            return self.function[func_name]
        else:
            return None

    # 获取文件地址和文件名
    def get_file_name(self):
        return self.file_name