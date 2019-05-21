#coding=utf-8

import pymysql
from config.conf import Config

#创建数据库连接，注意这里我加入了charset和cursorclass参数
conn = pymysql.connect(
    host = Config.db_host,
    user = Config.db_account,
    password = Config.db_passwd,
    database = Config.db_database,
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor)

#获取游标
cursor = conn.cursor()
try:
    # 执行一条insert语句，返回受影响的行数
    # cursor.execute("INSERT INTO para5(name,age) VALUES(%s,%s);",('次牛','12'))
    # 执行多次insert并返回受影响的行数
    cursor.executemany("INSERT INTO language(Lang) VALUES(%s);", [('zh-Hant')])
    # 提交执行
    conn.commit()
except Exception as e:
    # 如果执行sql语句出现问题，则执行回滚操作
    conn.rollback()
    print(e)
finally:
    # 不论try中的代码是否抛出异常，这里都会执行
    # 关闭游标和数据库连接
    cursor.close()
    conn.close()