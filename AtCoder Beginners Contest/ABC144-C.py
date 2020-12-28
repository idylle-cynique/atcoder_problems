# ABC144 - C

# 掛算表、というのは要するに2個の整数とその積を表にしたもの
# 入力値Nのある座標(x,y)におけるx,yはNを因数分解して得られる数の組み合わせのうち、
# 座標の初期位置(1,1)からもっとも近いもののことを指している

# つまりこの問題の本質は二次元リストの操作ではなく、整数処理

def seek_ncombi(n): # nの数が膨大でも、√N までしか探索しないので計算量は大きくない
      x = 1
      ncombi = []
      while(x**2 <= n):
            if n%x == 0:
                  ncombi.append((x,n//x))
            x += 1
      else:
            return ncombi
                  

n = int(input())
nums = seek_ncombi(n)
ans = n**12
#print(nums)

for i in nums:
      #print(i[0]-1 + i[1]-1)
      if (i[0]-1 + i[1]-1) < ans:
            ans = i[0]-1 + i[1]-1
      
print(ans)