
import os
os.path.abspath("C:\\soft\\Pycharm\\workspace\\APP_auto\\Base_paskage\\config\\login.yaml")
import yaml

class HandleYaml:
    def read_yaml(self):
        path = os.getcwd()
        file_path=(path + '\\config\\login.yaml')
        fs=open(file_path,'rb')
        self.ya=yaml.load(fs,Loader=yaml.Loader)
        return self.ya

if __name__ == '__main__':
    print(HandleYaml().read_yaml())
