# ARC069 - C

s,c = map(int,input().split())
scc = 0
cc = 0

# (1) Sを1つ、Cを2つ使ってSCCを作る
# (2) Cを4つ使ってSCCを作る
# のいずれかによってSCCを作ることができる

# (1)の方法でsccを作れるだけ作る -------------------
cc = (c//2) ## cをccに変換
c -= (cc*2)

tmp = min(s,cc)
scc += tmp
s -= tmp
cc -= tmp

#print("scc:",scc); print("cc:",cc); print("s:",s); print("c:",c); print()
#---------------------------------------------------

# cc を cに戻す
c += (cc*2)
cc -= cc

# (2)の方法でsccを作れるだけ作る -------------------
tmp = c//4
scc += tmp
c -= (4*tmp)
#print("scc:",scc); print("cc:",cc); print("s:",s); print("c:",c)
#---------------------------------------------------

print(scc)