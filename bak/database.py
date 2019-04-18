import random
import sys
import time
import requests
from openpyxl import Workbook
import pymysql.cursors


def get_conn():
    '''建立数据库连接'''
    conn = pymysql.connect(host='localhost',
                                user='aoliver',
                                password='3edc$RFV',
                                db='aoliver_house',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return conn

def insert(conn, info):
    with conn.cursor() as cursor:
        sql = "INSERT INTO dw_user (MSISDN, NAME, AGE) VALUES (%s, %s, %s)"
        cursor.execute(sql, info)
    conn.commit()

def main():
    conn = get_conn()
    '''
    info=[]
    info.append(sys.argv[0])
    info.append(sys.argv[1])
    info.append(sys.argv[2])
    '''
    info=[sys.argv[1],sys.argv[2],sys.argv[3]]
    insert(conn,tuple(info))
    conn.close()

if __name__ == '__main__':
    main()
