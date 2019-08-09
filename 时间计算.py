import time

year = int(input('请输入年份:'))
month = int(input('请输入月份:'))
day = int(input('请输入日期:'))

# 形成时间元组
tuple_give = (year,month,day,0,0,0,0,0,0)
# 得到出生时计算机时间
give_second = time.mktime(tuple_give)

# 得到一共过了多少秒
second = time.time() - give_second
print('已经过%d秒' %second)
# 得到一共过了多少分钟
minute = second/60
print('已经过%d分钟' %minute)

# 得到一共过了多少小时
hour = minute/60
print('已经过%d小时' %hour)

# 得到一共过了多少天
day = hour//24
print('已经过%d天' %day)

# 算出输入时间是星期几
t = time.localtime(give_second)
weeks = {
    0:  '星期一',
    1:  '星期二',
    2:  '星期三',
    3:  '星期四',
    4:  '星期五',
    5:  '星期六',
    6:  '星期日',
}

print('您输入的时间是:',weeks[t[6]])