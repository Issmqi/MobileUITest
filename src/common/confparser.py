#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'shimengqi'
__description__:'读取配置文件信息'
__mtime__:2018/2/10
'''
import os
import configparser
import log

Log=log.Log()

# configPath="../../config/config.ini"


class ReadConfig:
    def __init__(self):
        curPath = os.path.abspath(os.path.dirname(__file__))
        filePath = os.path.split(curPath)[0]
        proPath = os.path.split(filePath)[0]
        self.configPath = proPath + '\config\config.ini'

        self.cf = configparser.ConfigParser()
        self.cf.read(self.configPath,encoding="utf-8-sig")

    def get_config(self, field, key):
        '''获取config.ini信息'''
        result = self.cf.get(field, key)
        # Log.debug('%s的%s是：%s' % (field, key, result))
        return result

    def set_config(self, field, key, value):
        '''修改config.ini信息'''
        fd = open(self.configPath, "w")
        self.cf.set(field, key, value)
        # log.debug('%s的%s修改成功 ,value=%s' % (field, key, value))
        self.cf.write(fd)


def main():
    config = ReadConfig()
    deviceName=config.get_config("oppoADB", "deviceName")
    print(deviceName)

if __name__ == '__main__':
    main()