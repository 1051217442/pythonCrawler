# -*- coding: UTF-8 -*-
"""
@描述：
@作者：CYH
@版本：V1.0
@创建时间：2016-11-24 上午9:34:54
"""
from MysqlDBPool import getPTConnection, PTConnectionPool


def TestMySQL():
    # 申请资源
    with getPTConnection() as db:
        # SQL 查询语句;
        sql = "SELECT * FROM user"
        try:
            # 获取所有记录列表
            db.cursor.execute(sql)
            results = db.cursor.fetchall()
            for row in results:
                userId = row[0]
                name= row[1]
                # 打印结果
                print("userId=%d,name=%s" % (userId, name))
        except:
            print("Error: unable to fecth data")


TestMySQL()