import os
os.chdir('F:\GitHub-reuity\Python\PythonBase\FileOps')

fo = open("abc.csv","r",encoding="UTF-8-sig")   # sig删除文件开头\ufeff
ls = []
for line in fo:
    line = line.replace("\n","")
    ls = line.split(",")
    lns = ""
    for s in ls :
        lns += "{}\t".format(s)
    print(lns)
fo.close