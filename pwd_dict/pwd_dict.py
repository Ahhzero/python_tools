# coding=utf-8
"""
主要用来处理（域名）对应的密码字典
"""
import exrex
from config import *

class Generate_pwd_dict(object):
    """
    专门用于生成密码字典的类
    """
    def __init__(self,domain):
        self._domain = domain
        self._domain_dict = "" # 用来存放域名信息
        self._domains = []

    def _domain_filter(self):
        # 获取有用的信息   web   sjcrm
        # 先去除domain中 最后的 /
        self._domain = self._domain.rstrip("/")
        # 先判断domain中是否存在  ://
        if "://" in self._domain:
            temp = self._domain.split("://")
            self._domain = temp[1]
        # 存储域名
        self._domain_dict = self._domain
        # 开始用点来切割
        self._domains = self._domain.split(".")

        # 准备过滤
        domains_true = []
        for d in self._domains:
            if d not in black_list:
                domains_true.append(d)
        self._domains = domains_true
    def generate(self):
        """
        生成字典的方法
        :return:
        """
        # 处理域名
        self._domain_filter()

        for d in self._domains:
            for p in passwd_m_lisit:
                pattern = d + pwd_gz + p + pwd_last_gz
                temp_pwd_list = list(exrex.generate(pattern))
                with open(f"./pwds/{self._domain_dict}.txt", "a+") as f:
                    for tp in temp_pwd_list:
                        f.write(f"{tp}\n")
                        
                        
  
