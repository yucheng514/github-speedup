
import requests
from bs4 import BeautifulSoup
import re 
import shutil
import os 
import datetime

# 需要获取ip的网址

sites =[ 
	"github.com",
	"github.global.ssl.fastly.net",
	"assets-cdn.github.com",
	"documentcloud.github.com",
	"gist.github.com",
	"help.github.com",
	"nodeload.github.com",
	"raw.github.com",
	"status.github.com",
	"training.github.com",
	"ithubusercontent.com",
	"avatars1.githubusercontent.com",
	"codeload.github.com"
	]
	
addr2ip = {}

# 获取网址的 ip

def getIp(siteAdd):
	
	# engine = "https://ipaddress.com/search/"
	# headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36','Host':'movie.douban.com'}	

	url = "http://ip.tool.chinaz.com/" + siteAdd
	try:
		res = requests.get(url)
		soup = BeautifulSoup(res.text,'html.parser')
		result = soup.find_all('span', class_="Whwtdhalf w15-0 lh45")
		trueip = None
		for c in result:
			ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", c.text)
			if len(ip) != 0:
				trueip = ip[0] 
	except:
		print("查询" + siteAdd + " 时出现错误")
		return None
	
	return trueip	
	

# 生成数据表
def generateDict():

	for site in sites:
		ip = getIp(site)
		if ip != None:
			addr2ip[site] = ip
			print(site + "\t" + ip)
		

def chachong(line):
	flag = False
	for site in sites:
		if site in line:
			flag = flag or True
		else:
			flag = flag or False
	return flag 
	

# 更新 host

def updateHost():
	generateDict()
	today = datetime.date.today()
	path = "/private/etc/hosts"
	backup = "/private/etc/hosts.backup"
	temphost = "./src/temphost"
	shutil.copy(path, backup) # 做一份 host 备份
	f1 = open(path, "r") # r: 以只读方式打开文件。文件的指针将会放在文件的开头。
	lines = f1.readlines()
	f2 = open(temphost, "w") 
	# f2 = open("temphost", "w+") # w: 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
	
	for line in lines:                       # 为了防止 host 越写用越长，需要删除之前更新的含有 github 相关内容
		if chachong(line) == False:
			f2.write(line)
	f2.write("\n\n# ********************* github " + str(today) + " update ********************\n")
	for key in addr2ip:
		f2.write(addr2ip[key] + "\t" + key + "\n")
	f1.close()
	f2.close()
	
	shutil.copy(temphost, path) #覆盖原来的 host
	
updateHost()	