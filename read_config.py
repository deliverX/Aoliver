#!/usr/bin/python

import configparser
import os

class ReadConfig:
    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            root_dir = os.path.abspath('.')
            configpath = os.path.join(root_dir, "mysqlinfo.config")
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_db(self, option, param):
        value = self.cf.get(option, param)
        return value

    def get_items(self, option):
        items = self.cf.items(option)
        return items


if __name__ == '__main__':
    rc = ReadConfig()
    result = rc.get_items("mysql")
    print(result)
    print(result[0][1])

    res = rc.get_db("mysql","host")
    print(res)
