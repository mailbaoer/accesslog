#-*- coding:utf-8 -*-

import sqlite3

##
#日期计算函数，通过接收到的参数决定取到距离当日日期之前多少天的日期
#返回值：parseDate
#

class DataBase:

    def getConnection(self,dbfile):

        self.conn = sqlite3.connect(dbfile)

        return self.conn

    def createTable(self,tablename,c,conn):

        try:
            
            c.execute('''create table [%s] (date text,url text,status text,size integer,laststime integer,useragent text,ip text,refer text)''' % tablename)

            conn.commit()

        except:
            pass


    def selectAll(self,tablename,c,conn):

        try:
            c.execute('''select date,url,size,laststime,ip from [%s]'''%tablename)

            data = c.fetchall()

            return data
        except:
            pass

    def insertLog(self,logItem,tablename,c):

        try:
            c.execute('insert into [%s] values (?,?,?,?,?,?,?,?)' % tablename, logItem)
        except:
            pass
    


