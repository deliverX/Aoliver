#!/usr/bin/python
from DBUtils.PooledDB import PooledDB
import pymysql.cursors
from read_config import ReadConfig

class OPMysql(object):

    __pool = None
    data = ReadConfig()

    def __init__(self):
        # 构造函数，创建数据库连接、游标
        self.conn = OPMysql.getmysqlconn()
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 数据库连接池连接
    @staticmethod
    def getmysqlconn():
        host = OPMysql.data.get_db("mysql", "host")
        user = OPMysql.data.get_db("mysql", "user")
        password = OPMysql.data.get_db("mysql", "passwd")
        db = OPMysql.data.get_db("mysql", "db")
        port = OPMysql.data.get_db("mysql", "port")
        charset = OPMysql.data.get_db("mysql", "charset")
        if OPMysql.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=20, host=host, user=user, passwd=password, db=db, port=int(port), charset=charset)
        return __pool.connection()

    # 插入\更新\删除sql
    def op_execute(self, sql, data):
        related_num = self.cur.execute(sql, data)
        self.conn.commit()
        return related_num

    # 查询sql
    def op_search(self, sql):
        self.cur.execute(sql)
        select_res = self.cur.fetchall()
        return select_res

    # 释放资源
    def dispose(self):
        self.conn.close()
        self.cur.close()

if __name__ == '__main__':
    opm = OPMysql()
    sql = "select * from dw_user"
    for i in opm.op_search(sql):
        print(i)
    opm.dispose()
