# github-speedup
解决 Mac 上 github 加载和下载速度慢的问题

直接获取 ip 地址并绑定本地 hosts，绕过 DNS 解析，通过脚本获取 github 相关网址的 ip

感谢 ➡️ [Windows 版解决方案](https://github.com/jvxiao/speed-github)


### setup
1. 安装 python3 后，安装：
   - BeautifulSoup4
   - requests
   - shutil

2. 终端打开此项目，输入：
```
sudo sh init.sh
```
或者
```
npm run init
```





### todo

- [ ] 添加 command 文件
- [ ] 用 node 改为 js 版本