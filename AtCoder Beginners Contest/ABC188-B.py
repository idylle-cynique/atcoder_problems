# ABC188 - B

# 問題文に書かれている通りに実装すればよい問題

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
ip = 0

for i in range(n):
      #print(a[i]*b[i])
      ip += (a[i]*b[i])

if ip == 0:
      print("Yes")
else:
      print("No")
      
#print(ip)