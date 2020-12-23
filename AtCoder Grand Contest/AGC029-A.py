# AGC029 - A

# 要するに左側に"W"を、右側に"B"を寄せていく作業をしろということ
# それぞれの"W"の左側にある"B"を数え上げていき最終的にその総和を出力すればよい

s = list(input())
s_l = len(s)
k = 0
ans = 0

for i in range(0,s_l):
      if s[i] == "B":
            k += 1
      else:
            ans += k

print(ans)