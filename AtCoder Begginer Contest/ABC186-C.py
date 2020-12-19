# ABC186 - C
n = int(input())
ans = 0

for i in range(1,n+1):
      dec_i = str(i)
      oct_i = oct(i)
      if "7" not in dec_i and "7" not in oct_i:
            #print(i,oct_i)
            ans += 1
            
print(ans)