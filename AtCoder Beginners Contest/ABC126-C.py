# ABC126 - C

# 問題の通りに実装すればよい
# 出た時点でk以上になるような目はまとめて計算してもよいが、^-9未満の部分で誤差が出る
# 1 <= n <= 10**5という制約を考えると、まとめて計算せずに愚直に解を求めた方が無難

# 誤差を許容して計算速度を早めるなら
#    if times == 0:
#        ans += ((1/n)*(n-i+1))
#        break
# このようなコードをfor文に入れればよい(AC判定確認済み)

def check_expo(n,x): # 何回連続で表が出ればk以上になるかを求める
    ret = 0
    while(x*2**ret < n):
        #print(x*2**ret,n)
        ret += 1
    return ret

n,k = map(int,input().split())
ans = 0

for i in range(1,n+1):
    times = check_expo(k,i)
    tmp = (1/n) * ((1/2)**times)
    #print(i,times); print(1/n,"*",(1/2)**times,":",tmp)
    ans += tmp

print(ans)