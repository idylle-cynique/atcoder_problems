# EDP - A
n = int(input())
h = [int(x) for x in input().split()]
dp = [float('inf')]*n
dp[0] = 0

for i in range(1,n):
      #print(abs(h[i]-h[i-1]),abs(h[i]-h[i-2]))
      dp[i] = min(dp[i-1]+abs(h[i]-h[i-1]), dp[i-2]+abs(h[i]-h[i-2]))
            # 1つ前の山から移ってくるときのコスト + 1つ前の山までの移動コスト
            # 2つ前の山から移ってくるときのコスト + 2つ前の山までの移動コスト
            # の２つのうち、よりコストの小さい方をdpリストのdp[i]に代入する
            
            # i = 1のときdp[i-2]の添え字が負数になってしまうが、事前にfloat(inf)としてあるので正しくdp[i-1]...の方が選択される
      
#print(h); print(dp); 

print(dp[-1]) # dpの末尾を出力