# coding=utf-8
import os
import re
import chardet
from Model import File
import json

'''
审计类
'''


class FileList:

    def __init__(self, file_path, rule):
        # 切换工作目录至php代码的目录
        os.chdir(file_path)
        self.files = self.dir_list()
        self.rule = rule
        # 保存php工程目录
        self.php_path = file_path
        self.rule_dict = {}
        self.count = 0
        # 获取规则
        self.rule_dict = self.jsonfile_load(self.rule)

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
        # 初始化php项目
        os.chdir(self.php_path)  # 切换工作目录至PHP代码目录
        # 逐个php文件处理
        for i in self.files:
            # 为每个文件创建文件对象
            file_ood = File.File(i)
            file_content = self.php_file_read(i)
            for index, v in enumerate(file_content):
                self.audit_print(v, file_ood, index)
        print("共发现" + str(self.count) + "个可疑漏洞点")

    # 规则匹配 并打印 取出函数和形参 用作命令行
    def audit_print(self, content, file_ood, line):
        # 匹配取出所有的方法
        for k,v in self.rule_dict.items():
            regular = k
            result = re.findall(regular,content)
            # print(regular)
            if len(result) > 0:
                for i in result:
                    print("--------------------------------")
                    print("[*] "+ v)
                    print("[*] file:"+file_ood.get_file_name())
                    print("[*] line:"+str(line+1))
                    print("[*] code:"+content.strip()[:40])
                self.count+=1

    # 规则匹配 存储危险函数列表 用于后期UI版
    def audit_gui(self,content,file_ood,line):
        pass

    # txt读入列表
    def txt_to_list(self, file_name):
        # 获取程序当前路径
        path = os.path.dirname(os.path.realpath(__file__))
        # 切换至当前路径
        os.chdir(path + '\\..\\')
        str_list = []
        # 逐行读取危险函数文件
        with open(file_name, 'r') as f:
            for line in f:
                str_list.append(line.split()[0])
        return str_list

    # json读取
    def jsonfile_load(self, file_name):
        # 获取程序当前路径
        path = os.path.dirname(os.path.realpath(__file__))
        # 切换至当前路径
        os.chdir(path + '\\..\\')
        with open(file_name, 'r') as f:
            rule_dict = json.load(f)
        return rule_dict

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
            return ''
