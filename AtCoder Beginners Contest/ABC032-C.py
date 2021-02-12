# ABC032 - C

# 尺取り法の演習問題
# 大まかな実装方法こそ浮かんだものの、境界値や二つの添え字の管理方法が上手く分からず
# ほぼ解説を見ながらの実装となってしまった

n,k = [int(x) for x in input().split()]
s = [int(input()) for x in range(n)]
mult = max(1,s[0])
ans = -1
r = 1

for i in s:
      if i == 0:    # 数列の要素に 0 が含まれるとき、すべての要素からなる数列でも条件を満たす
            print(n)
            exit()
      if i <= k:    # すべての要素が k 以上であるとき、 いかなる部分列でも条件を満たすことはできない
            ans = 0

if ans == -1:       # 変数 ans を 対象数列の要素チェックに用いている
      print(0)
      exit()
else:
      ans = 0
      
for l in range(n):
      while(mult <= k and r < n):
            #print(s[l:r],mult)
            if mult*s[r] <= k:
                  mult *= s[r]
                  r += 1
            else:
                  #print("break"); 
                  break
                  
      ans = max(ans,r-l)
      
      if l == r:    # 次の要素が大きく、部分列の要素数が空になってしまったとき
            r += 1
      else:         # 一番左の要素だけ取り除いて再検討したいとき
            mult //= s[l]
            
print(ans)