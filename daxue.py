#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests 
import re 

# 编写一个方法获取单个页面的所有mov格式地址

def get_mp4(url):
	res = requests.get(url) 
	# resources\u002F003第三课-结构搭建.mov
	address = re.compile(r'resources\\[^\.]*\.[^\"]*\"')
	res2 = address.findall(res.text)
	return res2 

# 编写一个循环获取所有的mp4
def get_all():
	all_mp4 = ''
	for x in range(2,10): 
		url = "https://jtduniversity.jvtd.cn/onlinecourses/"+str(x)+".html";
		all_mp4 = get_mp4(url) 
		for y in all_mp4:
			print("https://university-prod.oss-cn-beijing.aliyuncs.com/"+y.replace("\\","/").replace("\"","").replace("u002F",""))
	return ""


get_all()