#encoding=utf-8
import logging
import datetime
import time
import os
import sys


logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
#控制台输出日志
'''
consel=logging.StreamHandler()
logging._addHandlerRef(consel)
logging.debug("test")
consel.close()
logging._removeHandlerRef(consel)

'''
#文件夹输出日志
'''
fd=logging.FileHandler("C:/soft/Pycharm/workspace/Appium_Mj/config/log.log")
formatter=logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s--->%(message)s ')
fd.setFormatter(formatter)
logger.addHandler(fd)
logger.debug("test")
fd.close()
logger.removeHandler(fd)
'''
#生成日志文件名
#base_path=os.path.dirname(os.path.abspath(__file__))
#print (base_path)
#log_dir=os.path.join(base_path,"config")
#print (log_dir)
log_dir=os.getcwd()+"/Appium_Mj/config"
log_file=datetime.datetime.now().strftime("%Y-%m-%d")+".log"
print (log_file)
log_name=log_dir+"/"+log_file
print (log_name)

fd=logging.FileHandler(log_name,'a',encoding='utf-8')
formatter=logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s--->%(message)s ')
fd.setFormatter(formatter)
logger.addHandler(fd)
logger.debug("test")
fd.close()

logger.removeHandler(fd)


