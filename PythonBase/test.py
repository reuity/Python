# num = input("输入一个整数")
num = eval(input("输入一个整数"))
# print (num)
# print (abs(num))
print (int(num))





print(int("11345345",10))




def reverse(s):
  if s == "":
    return s
  else:
    return reverse(s[1:])+s[0]

# s=str(input("输入字符串："))
s=input("输入字符串：")
s=reverse(s)
print(s)