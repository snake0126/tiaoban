import re
import MySQLdb as mysql

f = open('/tmp/access.log')
res = []

con = mysql.connect(user='root',passwd='',host='localhost',port=3306)
cur = con.cursor()
con.select_db('nginxlog')
for l in f:
    arr = l.split(' ')
    ip = arr[0]
    url = arr[6]
    time = arr[3]
    status = arr[8]
    cpuid = arr[16]
    res = [ip, url, status,cpuid,time]
    sql = 'INSERT INTO logtest values("%s","%s","%s","%s","%s")' % (res[0],res[1],res[2],res[3],res[4])
    cur.execute(sql)
    con.commit()
