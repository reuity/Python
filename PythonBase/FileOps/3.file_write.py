import os
os.chdir('F:\GitHub-reuity\Python\PythonBase\FileOps')

fname = input ("请输入文件名：")
fo = open(fname,"a+",encoding='UTF-8')
ls = ['qwe','asd','zxc']
fo.writelines(ls)
fo.seek(0)
for line in fo :
  print(line)
fo.close()

