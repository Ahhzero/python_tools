# coding=utf-8
"""
配置文件
"""
# 黑名单
black_list = ['com', 'cn', 'net', 'www']
# 密码的木本
passwd_m_lisit = ["admin","123456","123123","111111","test","guest"]
# 生成密码中间的规则
pwd_gz = r"[@#!]{1,2}"
# 生成密码最后面的规则
pwd_last_gz = "[&*]"