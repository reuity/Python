import os
os.chdir('F:\GitHub-reuity\Python\PythonBase\FileOps')

fo = open("abc.csv","w+")  
ls = ['仙桃','103.1','111.1','123.4']
fo.seek(2)
fo.write("\n"+",".join(ls)+ "\n")

