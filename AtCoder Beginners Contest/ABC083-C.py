# ABC083 - C
x,y = [int(x) for x in input().split()]
cnt = 0
a = x

while(a <= y):
      #print(a)
      cnt += 1
      a *= 2

print(cnt)