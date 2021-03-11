# ABC109 - C

# 各区間の距離の最大公約数が解となるので、ユークリッドの互除法を用いて高速に最大公約数を求めていくことが解が明らかになる

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b) 
    
n,x = map(int,input().split())
a = [int(x) for x in input().split()] + [x]
a = sorted(a)

distances = []
ans = 10**9 

for i in range(n): # 各区間の距離を求める
    distances.append(a[i+1]-a[i])

for i in range(len(distances)-1):
    ans = min(ans,gcd(distances[i+1],distances[i]))
    #print(ans)
    
    if ans == 1: # 解の最小値は1なので、1が現れた時点で計算をやめてよい
        print(1)
        exit()

if len(distances) == 1: # コーナーケース
    print(distances[0])
else:
    print(ans)