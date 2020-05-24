import os
# os.chdir('F:\GitHub-reuity\Python\PythonBase\FileOps')
os.chdir('C:\Windows')

fname = input ("请输入文件名：")
fo = open(fname,"r",encoding='UTF-8')
# for line in fo.readlines():   # 一次性将文件所有内容读取到列表，占用内存会非常多，建议使用下面方法
for line in fo:    # 文件本身就是一个行序列，可直接遍历
  print(line,end='')
fo.close()


0