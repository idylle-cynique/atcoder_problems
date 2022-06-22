''' ABC1740 - B
    問題文を用いて愚直に全探索を行うだけでよい
'''

n,d = [int(x) for x in input().split()]
counts = 0

for i in range(n):
      x,y = [int(x) for x in input().split()]
      if d**2 >= x**2 + y**2:
            counts += 1

print(counts)