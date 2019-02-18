#下载geckodriver 浏览器驱动
#拷贝到python安装目录下
#pip install selenium //测试插件 用于浏览器启动
#pip install websocket_server //socket包
import time
import sys
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from websocket_server import WebsocketServer


def filter_Non_BMP_Characters(target):    
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    name=target.translate(non_bmp_map)
    return name

short_Urls = []
long_Urls = []
cur_file = "分享单曲s.txt"
with open(cur_file,'r',encoding='ansi') as fn:
    datas = fn.readlines()
    fn.close()
    
target_pat = "http://t.cn/" #E5nl7m9"
for line in datas:
    ss = line.split("data-url=\"")
    if len(ss) > 1 :
        lengs = ss[1].find("\"")
        short_url = ss[1][0:lengs] 
        print(short_url)
        short_Urls.append(short_url)

chrome_driver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
browser = webdriver.Chrome(executable_path=chrome_driver) 
for short_url in short_Urls:                                                                                                                                            
    browser.get(short_url)#浏览器打开url，
    url = browser.current_url#获取解析后的url
    print(url)
    long_Urls.append(url)
with open("long_urls.txt","w+",encoding="utf-8") as fn:
    fn.write("\n".join(long_Urls))
    fn.close()
browser.quit()
