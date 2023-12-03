# coding=utf-8
import time
import traceback
import paramiko
import logging
import socket
import ping3
from paramiko import ssh_exception
from paramiko.ssh_exception import AuthenticationException
 
 
def login(ip, port, user, passwd):
    conn = paramiko.SSHClient()
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        conn.connect(ip, port=port, username=user, password=passwd, timeout=15)
        connect_result = "Connect Server {0} {1} {2} {3} 主机连接成功!\n".format(
            ip, port, user, passwd)
        # 连接成功
        logging.info(connect_result)
        data = '{"code": "1000", "msg": "主机连接成功","result": true}'
    except AuthenticationException:
        connect_result = "Connect Server {0} {1} {2} {3} 用户名或密码错误!\n".format(
            ip, port, user, passwd)
        # 用户名或密码错误
        print(traceback.format_exc())
        logging.info(connect_result)
        data = '{"code": "5000", "msg": "用户名或密码错误","result": false}'
    except socket.timeout:
        connect_result = "Connect Server {0} {1} {2} {3} 主机连接异常!\n".format(
            ip, port, user, passwd)
        # 主机连接异常
        print(traceback.format_exc())
        logging.info(connect_result)
        data = '{"code": "6000", "msg": "主机连接异常","result": false}'
    except ssh_exception.SSHException:
        connect_result = "Connect Server {0} {1} {2} {3} 端口错误!\n".format(
            ip, port, user, passwd)
        # 端口错误
        print(traceback.format_exc())
        logging.info(connect_result)
        data = '{"code": "7000", "msg": "端口错误","result": false}'
    return data
 


def ping(ip):
    while True:
        # 使用ping函数发送ICMP回显请求并等待响应，返回延迟时间（毫秒）
        delay = ping3.ping(ip)
        
        if delay is not None:
            print(f"Ping {ip} 成功，延迟时间：{delay}ms")
        else:
            print(f"Ping {ip} 失败")
        
        time.sleep(1)  # 1秒钟的延迟



 
if __name__ == '__main__':
    ping("192.168.1.1")
    # res = login("192.168.1.1", 22, "root", "admin")
    # print(res)
    
# trans = paramiko.Tranport(("114.132.73.249", 22))
# trans.connect(username="ubuntu", password="Yzh281316")