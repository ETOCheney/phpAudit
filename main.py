# coding=utf-8
from controller import CodeAudit
import getopt
import sys

if __name__ == "__main__":
    # 获取输入参数
    argv = sys.argv[1:]
    hello = '''
           __             ___                 __   _   __ 
    ____  / /_  ____     /   |   __  __  ____/ /  (_) / /_
   / __ \/ __ \/ __ \   / /| |  / / / / / __  /  / / / __/
  / /_/ / / / / /_/ /  / ___ | / /_/ / / /_/ /  / / / /_  
 / .___/_/ /_/ .___/  /_/  |_| \__,_/  \__,_/  /_/  \__/  
/_/         /_/                                                                  

                                                  version:0.1.2(开发中……)             
    '''
    # 解析参数
    try:
        opts, args = getopt.getopt(argv, "HP:G", ["help", "path="])
    except getopt.GetoptError:
        print("Try -H for more information!")
        sys.exit(2)
    if len(opts) <=0:
        print("Try -H for more information!")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-H", "--help"):
            print(hello)
            print("main.py -P [phpProject]  --------  开始扫描")
            print("")
            print("-H   --help      获取帮助")
            print("-P   --path      指定扫描目录")
            print("-G               启动ui版")
            sys.exit(0)
        elif opt in ("-P", "--path"):
            print(arg)
            if '/' in arg or '\\' in arg:
                path = arg
            else:
                print("文件路径不要使用\\,使用/或者使用\\\\")
                exit(0)
        elif opt in ("-G"):
            print("开发中……")
            sys.exit(0)

    if 'path' in dir():
        f = CodeAudit.FileList(path, "func.json")
        f.audit_init()
