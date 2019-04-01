#from read_csv import get_conn
import read_csv
def main():
    conn = read_csv.get_conn()
    conn.close()

if __name__ == '__main__':
    main()
