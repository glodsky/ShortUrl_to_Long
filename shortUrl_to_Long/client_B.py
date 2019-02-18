#下载geckodriver 浏览器驱动
#拷贝到python安装目录下
#pip install selenium //测试插件 用于浏览器启动
#pip install websocket_server //socket包
import time
from selenium import webdriver
from websocket_server import WebsocketServer   
 
#启动浏览器
browser = webdriver.Chrome()                                                                                                   
#新连接回调                 
def new_client(client, server):                                                 
        print("New client connected and was given id %d" % client['id'])        
 
#断开连接回调                                         
def client_left(client, server):                                                
        print("Client(%d) disconnected" % client['id'])                         
                                                                             
#接受消息回调                                         
def message_received(client, server, message):                                   
        browser.get(message)#浏览器打开url，
        url = browser.current_url#获取解析后的url
        print(url)
        server.send_message(client, url)#推送给服务端，解析后的url
           
#运行服务
PORT=9501                                                                       
server = WebsocketServer(PORT, "0.0.0.0")   
#监听连接的客户端                                    
server.set_fn_new_client(new_client)  
# 接收客户端数据 
server.set_fn_message_received(message_received) 
# 断开客户端连接                                        
server.set_fn_client_left(client_left)  
#启动socket服务                               
server.run_forever()
