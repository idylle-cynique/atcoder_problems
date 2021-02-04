# ABC063 - C
# 提出予定

n = int(input())
tens = []
nottens = []
total = 0

for i in range(n):
      temp = int(input())
      total += temp
      
      if temp%10 == 0:
            tens.append(temp)
      else:
            nottens.append(temp)

nottens = sorted(nottens)
#print("tens   :",tens); print("nottens:",nottens)
if total%10 != 0:
      print(total)
      exit()
      
if len(nottens) == 0:
      print(0)
      exit()

for i in nottens:
      total -= i
      if total%10 != 0:
            print(total)
            exit()