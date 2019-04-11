'''

__author__:'shimengqi'
__description__:'配置日志服务'
__mtime__:2018/8/6
'''

import logging
import logging.config

import sys,os




class Log:
    def __init__(self):
        # 两种方式获取当前文件路径
        curPath = os.path.abspath(os.path.dirname(__file__))
        proDir = os.path.split(os.path.realpath(__file__))[0]
        filePath = os.path.split(curPath)[0] # 获取当前文件的上一层
        rootpath=os.path.split(filePath)[0]# 获取当前文件的上两层，即项目根目录
        sys.path.append(rootpath)
        logConfigPath=rootpath+'\config\log.ini'# 连接目录和文件名
        # logConfigPath = os.path.join(rootpath, "\config\log.ini")
        # path="../../config/log.ini"
        # logConfigPath = os.path.abspath(path)
        print("log.ini的路径是",logConfigPath)
        logging.config.fileConfig(logConfigPath)

        # create logger
        self.logger = logging.getLogger('request')

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


def main():
    logyyx = Log()
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.war('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.cri('一个致命critical信息')


if __name__ == '__main__':
    main()
