#-*- coding:utf-8 -*-

import os
import re
import datetime
import time
import glob
from database import DataBase


##
#日期计算函数，通过接收到的参数决定取到距离当日日期之前多少天的日期
#返回值：parseDate
#

class ParseCore:

    def findLogGz(self,filepath):

        gzlist = glob.glob(filepath+"*.gz")

        return gzlist
        

    def checkGzip(self):

        pass

    def checkLines(self,line):

        pass

    def checkRex(self,logTime,rex,startTime,endTime):
        #return re.match('(.*)\.gif$|(.*)\.png$|(.*)\.bmp$|(.*)\.jpeg$|(.*)\.jpg$|(.*)\.css$|(.*)\.txt$|(.*)\.ico$|(.*)\.js$|(.*)\.css$',logItem[1])
        try:
            #logTime = time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(logItem[0],"%Y-%m-%d %H:%M:%S"))
            #endTime = time.strftime('%Y-%m-%d %H:%M:%S',time.strptime("2012-09-10 16:15:00","%Y-%m-%d %H:%M:%S"))
            
            #print time.mktime(time.strptime("2012-09-10 16:15:00","%Y-%m-%d %H:%M:%S"))
            return startTime < logTime and logTime < endTime
            #visitTime1 = logItem[0].split(" ")
            #visitTime1 = visitTime1[1].split(":")
            #visitTime2 = visitTime1[0]+":" +visitTime1[1]
            #temp = visitTime1[0]
            #return (int(visitTime1[0])==15 and int(visitTime1[1])>44 and int(visitTime1[1])<60) or (int(visitTime1[0])==16 and int(visitTime1[1])>=0 and int(visitTime1[1])<15)
            #return int(visitTime1[0])>=12 and  int(visitTime1[0])<16 

        except:
            pass    

    
    def parseLine(self,line):
        strinfo = re.compile('webapp/wcs/stores/servlet')#正则表达式替换
        splittwo = ",- ,- ,"
        splitthree = ",- ,- ,- ,"
        urlParse = [] #截断url
        logItem = [] #加入数据库
        if(line.find(splitthree)!=-1):
            backhalf = line.split(splitthree)
        else:
            backhalf = line.split(splittwo)
        try:
            urlParse  = backhalf[1].split(" ,")
        except:
            pass
        if (len(urlParse) > 4):
            #url处理开始           
            #第二步，替换操作
            url = strinfo.sub('emall',urlParse[2])
            status = strinfo.sub('emall',urlParse[5])
            #logger.info(urlParse[1])
            #时间记录添加
            time1 = urlParse[0]
            #time.strptime(time1, '%Y-%m-%d %H:%M:%S')
            #s = time.mktime(time.strptime(time1, '%Y-%m-%d %H:%M:%S'))
            #time1 = s+float(urlParse[7])/1000000
            #x = time.localtime(time1)
            #s = time.strftime('%Y-%m-%d %H:%M:%S',x)
            logItem.append(time1)
            #url记录添加                
            logItem.append(url)

            logItem.append(status)
            #访问大小记录添加
            visitSize = urlParse[6]
            if visitSize=="-":
                visitSize = 0
            logItem.append(visitSize)
            #访问时间记录添加
            visitTime = urlParse[7]
            refer = urlParse[8]
            logItem.append(visitTime)
            userAgent = urlParse[9]
            logItem.append(userAgent)
            logItem.append(urlParse[10])
            logItem.append(refer)
            #添加进入del文件
            return logItem
        else:
            file = open("error.txt", 'a')
            file.write(line)
            file.close()
        
            
        
