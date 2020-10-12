#coding=utf-8
import os
import sys
import configparser

#base_path=os.getcwd()
#file_path=base_path+"/Appium_Mj/config/LocalElement.ini"
#cf=configparser.ConfigParser()
#cf.read(file_path)
#data_ini=cf.get('server','ip')

class Read_Init:


    def load_ini(self):
        file_path="C:/soft/Pycharm/workspace/Appium_Mj/config/LocalElement.ini"
        cf=configparser.ConfigParser()
        cf.read(file_path)
        self.cf=cf
        return self.cf

    def get_ini_vaue(self,key,node=None):
        #获取ini里面的值
        if node==None:
           node="'server"
        cf=self.load_ini()
        try:
            data=cf.get(node,key)
        except Exception:
            print("无参数")
            data =None

        return data

class Read_Ini:
    #读取配置文件
    def __init__(self,node):
        file_name="C:/soft/Pycharm/workspace/Appium_Mj/config/LocalElement.ini"
        self.file_name=file_name
        self.node=node
        if self.node==None:
           self.node="test"
        cf=configparser.ConfigParser()
        cf.read(self.file_name)
        self.cf=cf
    '''
    def load_init(self,file_name):
        cf=configparser.ConfigParser()
        cf.read(file_name)
        return cf
    '''
    def get_value(self,key):
        #读取配置文件中key值对应的value
        data=self.cf.get(self.node,key)
        return data
if __name__ == '__main__':
    #ini_dx=Read_Init()
    #print (ini_dx.get_ini_vaue("test","ip"))
    #ini_dx.get_ini_vaue("server","ip")
    R1=Read_Ini(node="test")
    print (R1.get_value("ip"))
    print (R1.get_value("username"))
