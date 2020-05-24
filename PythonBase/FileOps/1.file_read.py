import os
os.chdir('F:\GitHub-reuity\Python\PythonBase\FileOps')
textFile = open("abc.txt", "rt",encoding='UTF-8')
print(textFile.readline())
textFile.close()
binFile = open("abc.txt", "rb")
print(binFile.readline())
binFile.close()
