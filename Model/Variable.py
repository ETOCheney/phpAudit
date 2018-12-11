# coding=utf-8
'''
变量模型 记录变量所在的行数
'''

class Variable:
    def __init__(self,var_name,line):
        self.var_name = var_name
        self.line = line

    # 获取变量行数
    def get_line(self):
        return self.line