#-*- coding:utf-8 -*-

import datetime

##
#日期计算函数，通过接收到的参数决定取到距离当日日期之前多少天的日期
#返回值：parseDate
#

class DateClass:


    def getDate(self,daysBeforeToday):
        today = datetime.date.today()
        deltaday = datetime.timedelta(days=daysBeforeToday)
        parseDate = today - deltaday
        return(parseDate)


    def dateToString(self,date):

        return str(date)


    def formantDate(self,date):

        return date.strftime('%Y-%m-%d')
    
