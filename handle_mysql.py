#!/usr/bin/python
import pymysql.cursors
from read_config import ReadConfig

class HandleMysql:
    def __init__(self):
        self.data = ReadConfig()

    def conn_mysql(self):
        """连接数据库"""
        host = self.data.get_db("host")
        user = self.data.get_db("user")
        password = self.data.get_db("passwd")
        db = self.data.get_db("db")
        charset = self.data.get_db("charset")
        self.conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
        self.cur = self.conn.cursor()

    def execute_sql(self, sql, data):
        """执行操作数据的相关sql"""
        self.conn_mysql()
        self.cur.execute(sql, data)
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def search(self, sql):
        """执行查询sql"""
        self.conn_mysql()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return result


if __name__ == '__main__':
    hm = HandleMysql()
    sql = "select * from dw_user"
    for i in hm.search(sql):
        print(i)
