# ABC091 - B

# 問題文を誤読していた。
# 文字列を答えられるのは一度だけで、任意の回数答えていいわけではないことに留意する必要がある
# 先のコードで提出したのは任意の回数だけ文字列を答えて最大化を目指すためのコードとなっていた

n = int(input())
blues = {}

for i in range(n):
      card = input()
      if card not in blues:
            blues[card] = 1
      else:
            blues[card] += 1

m = int(input())
reds = {}

for i in range(m):
      card = input()
      if card not in reds:
            reds[card] = 1
      else:
            reds[card] += 1

#print(blues); print(reds)
ans = 0

for i in blues:
      if i in reds:
            if blues[i]-reds[i] > ans:
                  ans = blues[i]-reds[i]
      else:
            if blues[i] > ans:
                  ans = blues[i]

print(ans)