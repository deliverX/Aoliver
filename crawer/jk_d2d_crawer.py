#!/usr/bin/python
import requests
import sys
import io

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def main():
   headers = {
       'Accept':'application/json, text/javascript, */*; q=0.01',
       'Accept-Encoding':'gzip, deflate',
       'Accept-Language':'zh-CN,zh;q=0.9',
       'Connection':'keep-alive',
       'Cookie':'JSESSIONID=80A212DDDB037D38CDDA46E2E7427A90',
       'Host':'10.40.96.34:6600',
       'Referer':'http://10.40.96.34:6600/jsjk/plugins/main/log/sysoplog/createByMenu.ilf?menuName=%E6%A6%82%E8%A7%88',
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
       'X-Requested-With':'XMLHttpRequest'
   }
   #cookies = {'JSESSIONID':'80A212DDDB037D38CDDA46E2E7427A90'}
   url = 'http://10.40.96.34:6600/jsjk/plugins/familynet/index/main.jsp'
   resp = requests.post(url, headers = headers)
   #r = resp.json()
   #print(r)
   print (resp.content.decode('utf-8'))

if __name__ == '__main__':
    main()
