#-*- coding:utf-8 -*-
import os

##
#日期计算函数，通过接收到的参数决定取到距离当日日期之前多少天的日期
#返回值：parseDate
#

class config:

    #sqlite可执行程序的目录
    def getBinPath(self):

        return os.path.abspath('./bin/')

    #导出结果保存目录
    def getDocPath(self):
        
        return os.path.abspath('./doc/')


    #处理过程中中转数据库文件存储目录
    def getDbPath(self):
        
        return os.path.abspath('./db/')

    #日志分析的log保存目录
    def getLogPath(self):

        return os.path.abspath('./log/')

    #日志原件存放目录

    def getFilePath(self):

        return os.path.abspath('./file/')

    #日期设置
    date = "2013-06-17"



    
