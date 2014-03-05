#-*- coding:utf-8 -*-

import os

##
#日期计算函数，通过接收到的参数决定取到距离当日日期之前多少天的日期
#返回值：parseDate
#

class FileUtil:

    #def openFile(fileName):

    def mkDir(self,path):

        if os.path.isdir(path):
            pass
        else:
            os.mkdir(path)


    def checkFile(self,fileName):

        if os.path.exists(os.path.abspath(fileName)):
            
            os.remove(os.path.abspath(fileName))
            
        else:
            pass
