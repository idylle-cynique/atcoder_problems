# ABC087 - B

# 制約が 0 <= y500,y100,y50 <= 50
# 程度なので、貪欲法で全探索してもループ回数は51*51*51≒130,000程度
y500 = int(input())
y100 = int(input())
y50 = int(input())
x = int(input())
ans = 0


for i in range(y500+1):
      for j in range(y100+1):
            for k in range(y50+1):
                  #print(i,j,k,":",500*i + 100*j + 50*k)
                  if 500*i + 100*j + 50*k == x:
                        ans += 1

print(ans)