#-*- coding:utf-8 -*-

import gzip
import time
import datetime
import sqlite3
import os
import logging
from database import DataBase
from fileUtil import FileUtil
from date import DateClass
from config import config
from parseCore import ParseCore
from html import html


logger=logging.getLogger()

class Main:

    def accessLogParse(self):
        t=time.clock()
        dd = DataBase()
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"初始化数据库"+ self.dbfile)
        conn = dd.getConnection(self.dbfile)
        c = conn.cursor()
        dd.createTable(self.tablename,c,conn)
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"创建数据库表："+ self.tablename)

        parsecore = ParseCore()
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"开始处理日志")
        gzlist = parsecore.findLogGz(self.filepath)
        for gzipname in gzlist:
            if(gzipname.find(str(self.parseday))!=-1):
                logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"处理日志文件："+ gzipname)
                f = gzip.open(gzipname, "rb") 
                for line in f.readlines():
                    logItem = parsecore.parseLine(line)
                    dd.insertLog(logItem,self.tablename,c)
                f.close()
                conn.commit()
            else:
                pass
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"日志处理完毕")
        #计算处理日志的时间
        parseLog = int(time.clock()-t) 
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"处理日志共用时"+str(parseLog)+u"秒钟")
        
    def exportLog(self):
        htmlname = self.export + self.tablename+".html"
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"创建html文件："+ htmlname)
        file = open(htmlname, 'w')
        file.write(self.header)
        file.write(self.css)
        file.write(self.start)
        file.close()
        sql = 'select url,count(1) cc,sum(size),sum(laststime),round(avg(size),2),round(avg(laststime),2) from '+"'"+self.tablename+"'"+' group by url order by cc desc'+ ' limit 500'
        #sql = 'select date,url,size,laststime from '+"'"+self.tablename+"'"+' where laststime>600000000'
        #sql = 'select date,url,count(useragent) cc,ip,useragent from '+"'"+self.tablename+"'"+' group by url order by  cc desc'+ ' limit 500'
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"开始执行sql语句："+ sql)
        os.popen(self.binpath +'/'+ "sqlite3.exe -html  " + self.dbfile +" \"" + sql +" \""+ ">>" + htmlname)
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"sql执行完毕，结果计入html文件")
        file = open(htmlname, 'a')
        file.write(self.end)
        file.write(self.js)
        file.close()


    def __init__(self):

        handler=logging.FileHandler("Log_test.txt")
        logger.addHandler(handler)
        logger.setLevel(logging.NOTSET)
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"初始化系统")
        #处理日期初始化，可以从config中读取
        parseDate = DateClass()
        parseconfig = config()
        parsehtml = html()
        self.parseday = parseconfig.date
        #初始化配置信息
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+"初始化日至处理日期："+self.parseday)
        self.binpath = parseconfig.getBinPath()+'\\'
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"初始化可执行文件目录："+ self.binpath)
        self.logpath = parseconfig.getLogPath()+'\\'
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"初始化日志文件目录："+ self.logpath)
        self.docpath = parseconfig.getDocPath()+'\\'
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"初始化文档目录："+ self.docpath)
        self.dbpath = parseconfig.getDbPath()+'\\'
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"初始化数据库文件目录："+ self.dbpath)
        self.filepath = parseconfig.getFilePath()+'\\'
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"初始化日志文件目录："+ self.filepath)
        self.header = parsehtml.header
        self.css = parsehtml.css
        self.start = parsehtml.start
        self.end = parsehtml.end
        self.js = parsehtml.js
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"初始化html参数")
        #设置数据库表名
        self.tablename = "sn"+parseconfig.date
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"初始化数据库表名："+ self.tablename)
        #数据库文件存储地址
        self.dbfile = self.dbpath + self.parseday + '.db'
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"初始化数据库文件："+ self.dbfile)
        self.export = self.docpath + parseconfig.date+"\\"
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"初始化html文档目录："+ self.export)
        ff = FileUtil() 
        ff.mkDir(self.export)
        logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"创建html文档导出目录："+ self.export)
        fileCheck = FileUtil()
        errorLog = self.logpath+self.parseday
        fileCheck.checkFile('log/'+errorLog)
        fileCheck.checkFile('db/'+self.parseday)

if __name__=='__main__':
    logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"日至分析开始")
    t0 = time.clock()
    ss = Main()
    ss.accessLogParse()
    ss.exportLog()
    cost = str(int(time.clock()-t0))
    logging.info(time.strftime('%Y-%m-%d %H:%M:%S')+"---"+u"日至分析结束,共用时："+cost+u"秒钟")
