#-*- coding:utf-8 -*-
import os

##
#日期计算函数，通过接收到的参数决定取到距离当日日期之前多少天的日期
#返回值：parseDate
#

class html:

    

    #日期设置
    date = "2013-04-21"

    header = '''

<html>
<head>
    <title>Access_log日志分析结果图</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <script type="text/javascript"src="../script/jquery-1.8.2.min.js"></script>
</head>

             '''


    css = '''

<style>
        #header
        {
            width: 1000px;
            margin-left: auto;
            margin-right: auto;
            font-weight:bold;
        }
        #tblGrid
        {
            border-collapse: collapse;
            width: 1000px;
            border: 0;
            cellpadding: 0;
            cellspacing: 1;
            margin-left: auto;
            margin-right: auto;
        }
        #tblGrid thead tr td
        {
            color: #025aa4;
            background-color: #def3fc;
            height: 36px;
            font-size: 14px;
            font-weight: bold;
            text-align: center;
        }
        #tblGrid th, #tblGrid td
        {
            border: 1px solid #E1E1E1;
            text-align: center;
        }
        .hover
        {
            background-color: #5dd354;
            cursor: pointer;
        }
        .sorted
        {
            background-color: oldlace;
        }
        .clickable
        {
            text-decoration: none;
        }
        a:link{text-decoration:none ; color:#0033FF ;}
        a:visited {text-decoration:none ; color:#CC6600;}
        a:hover {text-decoration:underline ; color:#FF0000;}
        a:active {text-decoration:none ; colorwhite;}
    </style>
          '''

    start = '''

<body>
    <table id="header" height="200">
        <tr height="100">
            <td align="center">
				Access_log日志分析结果图                        
            </td>
			<td align="right">
				<a href="../../index.html">返回上一层</a>                        
            </td>
        </tr>
        <tr>
			<td><font color="#FF0000">1、下表默认按照访问次数由大到小进行排名，显示前排名500的记录</font></td>	
		</tr>
		<tr>
			<td><font color="#FF0000">2、可以点击各个标题按照该列从大到小或者从小到大进行排列</font></td>	
		</tr>
		
        <tr>
            <td align="right" colspan="2">
        </td>
        </tr>
    </table>
    <table id="tblGrid" style="table-layout:fixed">
    <thead>
        <tr>
            <td class="sort-alpha">
                url
            </td>
            <td class="sort-numeric">
                访问次数
            </td>
            <td class="sort-numeric">
                总访问大小
            </td>
            <td class="sort-numeric">
                总访问时间
            </td>
        </tr>
    </thead>
    <tbody>
            '''

    end = '''
            </tbody>
        </table>
    </body>
</html>
              '''
    js = '''

<script type="text/javascript" language="javascript">
    $(function () {
        $('#tblGrid').each(function () {
            var $table = $(this);                       //将table存储为一个jquery对象

            $('thead td', $table).each(function (column) {
                var findSortKey;
                if ($(this).is('.sort-alpha')) {       //按字母排序
                    findSortKey = function ($cell) {
                        return $cell.find('sort-key').text().toUpperCase() + '' + $cell.text().toUpperCase();
                    };
                } else if ($(this).is('.sort-numeric')) {       //按数字排序
                    findSortKey = function ($cell) {
                        var key = parseFloat($cell.text().replace(/^[^\d.]*/, ''));
                        return isNaN(key) ? 0 : key;
                    };
                }

                if (findSortKey) {
                    $(this).addClass('clickable').hover(function () { $(this).addClass('hover'); }, function () { $(this).removeClass('hover'); }).click(function () {
                        //反向排序状态声明
                        var newDirection = 1;
                        if ($(this).is('.sorted-asc')) {
                            newDirection = -1;
                        }
                        var rows = $table.find('tbody>tr').get(); //将数据行转换为数组
                        $.each(rows, function (index, row) {
                            row.sortKey = findSortKey($(row).children('td').eq(column));
                        });
                        rows.sort(function (a, b) {
                            if (a.sortKey < b.sortKey) return -newDirection;
                            if (a.sortKey > b.sortKey) return newDirection;
                            return 0;
                        });
                        $.each(rows, function (index, row) {
                            $table.children('tbody').append(row);
                            row.sortKey = null;
                        });

                        $table.find('thead td').removeClass('sorted-asc').removeClass('sorted-desc');
                        var $sortHead = $table.find('thead td').filter(':nth-child(' + (column + 1) + ')');
                        //实现反向排序
                        if (newDirection == 1) {
                            $sortHead.addClass('sorted-asc');
                        } else {
                            $sortHead.addClass('sorted-desc');
                        }

                        //移除已排序的列的样式,添加样式到当前列
                        $table.find('td').removeClass('sorted').filter(':nth-child(' + (column + 1) + ')').addClass('sorted');
                        $table.trigger('repaginate');
                    });
                }
            });
        });
    });
</script>
         '''
    

    
