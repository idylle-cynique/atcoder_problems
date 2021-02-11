# ABC153 - D 

# そのまま問題の通りに実装すればよい

h = int(input())
cnt = 0

while(h > 0):
      #print(h,cnt)
      cnt += 1
      h //= 2
print(2**cnt-1)