import sys
import pymysql.cursors
from hashlib import md5
import decorator as dr
def get_conn():
    conn = pymysql.connect(host='localhost',
                           user='aoliver',
                           password='3edc$RFV',
                           db='aoliver_house',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn

def insert_many(conn,list):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO dw_user_info(NAME ,AGE ,sex ,height ,born,MSISDN) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.executemany(sql,list)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("批量插入错误:%s" % (e))

def insert(conn,info):
    try:
        with conn.cursor() as cursor:
            sql = "insert into `dw_user_info`(`NAME`,`age`,`sex`,`height`,`born`,`MSISDN`) values (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,info)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("插入错误:%s" % (e))

@dr.decorator
def read_csv(filename):
    with open(filename,'r') as f:
        userList = []
        for line in f.readlines():
            curLine = line.strip('\n')
            '''如果是strip()可用这个方法
            Str = curLine.split()[0]
            lineStr = Str.split("|")
            '''
            lineStr = curLine.split("|")
            userStr = []
            userStr.append(lineStr[0])
            userStr.append(int(lineStr[1]))
            userStr.append(lineStr[2])
            userStr.append(int(lineStr[3]))
            userStr.append(lineStr[4])
            userStr.append(md5(lineStr[5].encode("utf8")).hexdigest())
            userList.append(userStr)
    return userList

def main():
    conn = get_conn()
    userList = read_csv(sys.argv[1])
    print(userList)
    insert_many(conn,userList)
    conn.close()

if __name__ == '__main__':
    main()
