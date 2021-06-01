# ABC203 - B

# pythonでは文字列型から整数型への変更が容易なので、要求されたとおりに実装すればよい
# N,Kの入力値は一桁までなので、そのままi*100 + jでその総和値を求める、としてもよい
# 仮に二桁以上もあり得る問題だった場合は3階の10号室が310(本来3010であるべき)となってしまうので工夫する必要がある

N,K = map(int,input().split())
total = 0

for i in range(1,N+1):
    for j in range(1,K+1):
        tmp = str(i) + "0" + str(j)
        #print(tmp)
        total += int(tmp)
print(total)