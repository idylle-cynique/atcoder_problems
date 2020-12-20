# ABC172 - B
s = input()
t = input()
j = 0
     
for i in range(len(s)):
      if s[i] is not t[i]:
            j += 1
     
print(j)