from selenium import webdriver # 引入模块，详见关于selenium安装和使用链接
import time  # 加入缓冲时间
import requests
from hashlib import md5
import re
import os
import codecs
import django
from webdriver_manager.chrome import ChromeDriverManager
import xlwings as xw
import shutil
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
extension_path = r'C:\Users\低椰\Desktop\chropath.crx'
chrome_options.add_extension(extension_path)#C:\Program Files\Google\Chrome\Application
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),chrome_options=chrome_options)
driver.get("https://onlinenew.enetedu.com/zjiet")#打开网址
driver.find_element(By.ID,"dl_div_2").click()
driver.find_element(By.NAME,"useremail").click()
driver.find_element(By.NAME,"useremail").clear()
driver.find_element(By.NAME,"useremail").send_keys("15268112200@163.com")
driver.find_element(By.NAME,"userpassword").click()
driver.find_element(By.NAME,"userpassword").clear()
driver.find_element(By.NAME,"userpassword").send_keys("Qw123456Qw123456`")
text = driver.page_source # 获取页面信息
pic = driver.find_element(By.XPATH,'//*[@id="createImage"]') # 获取元素
d=r'C:\Users\低椰\Desktop\t'
if not os.path.exists(d): #如果没有这个文件夹就创建一个
	os.mkdir(d)
pic.screenshot(r"C:\Users\低椰\Desktop\t\a.png")#保存成名为a.png的图片




#获取验证码并发送到百度ocr识别
from aip import AipOcr


APP_ID = '28097148'
API_KEY = 'Owit5QqFTSPQU4HT0WPhCzND'
SECRET_KEY = 'wvGbk8SpbjczdiCp5V0ytoUbCHrbykx4'


client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(r'C:\Users\低椰\Desktop\t\a.png')

result = client.basicGeneral(image)
print(result)
print("*******************************************")

for item in result['words_result']:
    print(item['words'])

print("*******************************************")

string_text = ""
for item in result['words_result']:
    string_text += item['words']
print('string_text:', string_text)
#




driver.find_element(By.NAME,"validateCode").click()
driver.find_element(By.NAME,"validateCode").clear()
driver.find_element(By.NAME,"validateCode").send_keys(string_text)
driver.find_element(By.XPATH,"//input[@name='']").click()
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/ul/li[2]/a").click()
driver.find_element(By.XPATH,"//*[@id='SearchForm']/div/div[2]/div/div/ul/li[3]/a").click()
