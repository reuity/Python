def reverse(s):
  if s == "":
    return s
  else:
    return reverse(s[1:])+s[0]

# s=str(input("输入字符串："))
s=input("输入字符串：")
s=reverse(s)
print(s)