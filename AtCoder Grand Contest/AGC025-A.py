# AGC025 - A

def digit_sum(x,y):
      total = 0
      while(x >= 1):
            total += x%10
            x //= 10
      while(y >= 1):
            total += y%10
            y //= 10
      return total
            
n = int(input())
ans = 10**5

for i in range(1,n//2+1):
      x,y = i,n-i
      temp = digit_sum(x,y)
      if temp < ans:
            #print(temp,"<",ans)
            ans = temp

print(ans)