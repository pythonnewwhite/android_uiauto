#coding=utf-8
from selenium import webdriver
import time
from PIL import Image
import pytesseract
def code_img(url):
    drive=webdriver.Chrome()
    drive.get(url)
    code_name=drive.find_element_by_name("anwser")
    drive.save_screenshot("C:/tmp/imp.png")
    anser_code=drive.find_element_by_class_name("verify-icon")
    #anser_code=drive.find_element_by_xpath("/ html / body / div[3] / form / div[4] / div[1] / img")
    left=anser_code.location['x']
    top=anser_code.location['y']
    right=anser_code.size['width']+left
    height=anser_code.size['height']+top
    im=Image.open("C:/tmp/imp.png")
    print (left,top,right,height)
    img=im.crop((left,top,right,height))
    img.save("C:/tmp/imp1.png")
    img1 = Image.open("C:/tmp/imp1.png")
    return img1
def code(url):
    test = pytesseract.image_to_string(code_img(url))
    print(test)
    str=""
    for i in test:
        if i ==" ":
            continue
        else:
            str=str+i
    return str


def login(url):
    drive=webdriver.Chrome()
    drive.get(url)
    drive.find_element_by_name("username").send_keys("admin")
    time.sleep(1)
    drive.find_element_by_name("password").send_keys("Tm123456")
    time.sleep(1)
    if code(url)=="":
        print("识别识别")
        login(url)
    else:
        drive.find_element_by_class_name("anwser").send_keys(code(url))

url="http://mgtportal-uat.mobje.faw-vw.com/rcs/login.html"

code_img(url)
print (code(url))