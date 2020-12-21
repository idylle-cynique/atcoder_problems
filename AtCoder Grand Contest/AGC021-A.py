# AGC021 - A
# もっと簡単な実装方法があるかも？

n = input()
n_l = len(n)
n_c = int(n[::-1])
ans,num = 0,0
f = False         # 1回以上上位の桁の減算処理を施したかどうかチェック

for i in range(n_l):
      if n_c%10 == 9 or f == True:
            num += 9
      elif i == 0:
            num += (n_c%10)
      else:
            num -= 10
            num += 9
            f = True
      #print(n_c,num)
      num *= 10
      n_c //= 10
      
num = str(num//10)

for i in num:
      ans += int(i)

print(ans)