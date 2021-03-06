#!/usr/bin/python
import pymysql.cursors
import os
from read_config import ReadConfig

class HandleMysql:
    def __init__(self):
        self.data = ReadConfig()

    def conn_mysql(self):
        """连接数据库"""
        host = self.data.get_db("mysql","host")
        user = self.data.get_db("mysql","user")
        password = self.data.get_db("mysql","passwd")
        db = self.data.get_db("mysql","db")
        charset = self.data.get_db("mysql","charset")
        self.conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
        self.cur = self.conn.cursor()

    def execute_sql(self, sql, data):
        """执行操作数据的相关sql"""
        self.conn_mysql()
        self.cur.execute(sql, data)
        self.conn.commit()

    def search(self, sql):
        """执行查询sql"""
        self.conn_mysql()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.conn.commit()
        return result

    def dispose(self):
        self.cur.close()
        self.conn.close()
if __name__ == '__main__':
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK' 
    splitTag = '|'
    fileCode = 'utf-8'
    localPath = './'
    fileName = 'aoliver_complain.csv'
    filePath = os.path.join(localPath,fileName)
    file = open(filePath,'w',encoding='utf-8') 
    hm = HandleMysql()
    sql = "select * from dw_user"
    tableResult = hm.search(sql)
    for row in tableResult:
        rowdata = ''
        for column in row :
            if column == None:
                column =''        
            try:        
                #rowdata = rowdata + (str(column)).encode(fileCode).decode('gbk').replace('\n', '') + splitTag
                rowdata = rowdata + str(column).replace('\n', '') + splitTag
            except Exception as e:
                print(e)
        file.write(rowdata[:-1]+'\n')
    file.close()
    hm.dispose()
