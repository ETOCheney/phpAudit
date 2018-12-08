# coding=utf-8
import os
import re
import chardet
from Model import File

'''
审计类
'''


class FileList:

    def __init__(self, file_path, rule):
        # 切换工作目录至php代码的目录
        os.chdir(file_path)
        self.files = self.dir_list()
        self.rule = rule
        self.php_dict = {}
        # 保存php工程目录
        self.php_path = file_path
        self.rule_list = []
        self.count = 0

    # 目录遍历
    def dir_list(self, file_path='.'):
        path = os.listdir(file_path)
        files = []
        for i in path:
            temp = file_path + '/' + i
            if os.path.isdir(temp):
                # 如果为文件 则递归读取
                files.extend(self.dir_list(temp))
            # 判断文件后缀是否为.php
            elif i[-4:] == '.php':
                files.append(temp)
        return files

    # 规则匹配初始化
    def audit_init(self):
        # 获取规则列表
        self.rule_list = self.txt_to_list(self.rule)
        # 初始化php项目
        os.chdir(self.php_path)  # 切换工作目录至PHP代码目录
        # 逐个php文件处理
        for i in self.files:
            # 为每个文件创建文件对象
            file_ood = File.File(i)
            file_content = self.php_file_read(i)
            for index, v in enumerate(file_content):
                self.audit(v, file_ood, index)
        print("共发现"+str(self.count)+"个可疑漏洞")

    # 规则匹配 取出函数和形参
    def audit(self, content, file_ood, line):
        # 匹配取出所有的方法
        fun = re.findall(r'\W*(\w+?)\(', content)
        for k in fun:
            # 匹配参数列表,是否有变量
            variable = re.findall(r'(\$[\w\->]+?)[,|\)]',content)
            if len(variable) > 0:
                if k in self.rule_list:
                    print("-----发现危险函数中存在变量-----")
                    print("file path: "+file_ood.get_file_name())
                    print("line: "+str(line+1))
                    print("function: "+k)
                    print("variable: "+','.join(variable))
                    print("--------------------------------")
                    self.count += 1
            file_ood.add_func(k, line=line,var=variable)

    # txt读入列表
    def txt_to_list(self, file_name):
        # 获取程序当前路径
        path = os.path.dirname(os.path.realpath(__file__))
        # 切换至当前路径
        os.chdir(path+'\\..\\')
        str_list = []
        # 逐行读取危险函数文件
        with open(file_name, 'r') as f:
            for line in f:
                str_list.append(line.split()[0])

        return str_list

    # php文件读取
    def php_file_read(self, file):
        with open(file, 'rb') as f:
            fstr = self.unified_code(f.read())
            flist = fstr.split('\n')
        # 返回读取的文件列表
        return flist

    # 编码统一转换为utf-8
    def unified_code(self, string):
        try:
            # 获取编码
            string_code = chardet.detect(string)['encoding']
            # 编码统一
            finall_string = string.decode(string_code).encode('utf-8').decode('utf-8')
            return finall_string

        except Exception as e:
            print("编码转换失败")
            exit(10086)
