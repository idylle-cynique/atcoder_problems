# Code Festival 2016 qual A - B

# 模範解答通りの実装方法を自力で導き出して、模範的なコードを書いて解答できた。
n = int(input())
rabbits = [int(x)-1 for x in input().split()]
ans = 0

for i in range(n):
      #print(i,rabbits[rabbits[i]])
      if rabbits[rabbits[i]] == i:
            ans += 1    

print(ans//2) 
      # ループ時点では組み合わせの重複カウントを許してしまっているので、最後に2で割る必要がある