# coding=utf-8
import math

import  requests
from IPy import IP
import threading
from queue import Queue
from config import *
from fake_useragent import UserAgent
import sys
import time
"""
C段扫描
1. 利用IPY进行C段的IP 生成
2. 将IP和端口进行结合生成访问的链接
3. 利用request进行请求，然后判断响应的结果，判断这个服务是否开启
"""

class C_scan(object):
    def __init__(self,ipc,thread_count):
        self._ipc = ipc #  C段扫描的语法
        self.ips = []
        self._queue = Queue()
        self._thread_count = thread_count
        self._threads = []
        self._total_count = 0
        self._result = []


    def _init(self):
        # 利用IPY生成常用的IP
        self._ips = IP(self._ipc)
        # 将ip和端口进行结合 组成请求链接 然后放入queue
        for ip in self._ips:
            # 遍历端口
            for port in ports:
                # 组装链接
                self._queue.put(f"http://{ip}:{port}")
                # self._queue.put(f"https://{ip}:{port}")
        self._total_count = self._queue.qsize()


    def start(self):
        # 初始化
        self._init()
        # 准备线程
        for i in range(self._thread_count):
            self._threads.append(self.Scan_run(self._queue,self._total_count,self._result))
        # 启动线程
        for t in self._threads:
            t.start()
        # 等待子线程结束
        for t in self._threads:
            t.join()
        for r in self._result:
            with open(f"./c_scan_result/C段扫描-{time.time()}.txt","a+") as f:
                for r in self._result:
                    f.write(f"{r}\n")
        print("\nC段扫描完成！")
    class Scan_run(threading.Thread):
        def __init__(self,queue,total_count,result):
            super().__init__()
            self._queue = queue
            self._ua = UserAgent()
            self._total_count = total_count
            self._result = result

        def _msg(self):
            last = round((self._queue.qsize() / self._total_count) * 100, 3)
            s = round(100 - last)
            sys.stdout.write(f"\r已扫描：{math.floor(s)*'='}>{s}%")

        def run(self):
            while not self._queue.empty():
                scan_url = self._queue.get()
                # print(scan_url)
                # 请求地址
                self._msg()
                headers ={
                    "User-Agent":self._ua.random
                }
                try:
                    res = requests.get(scan_url, headers=headers, timeout=3)
                    if res.status_code != 404:
                        # print("****" + scan_url)
                        self._result.append(scan_url)
                except Exception as err:
                    pass

# scan = C_scan("192.168.219.0/24",1000)
# scan.start()