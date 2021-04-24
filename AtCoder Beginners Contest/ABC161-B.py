# ABC161 - B

# 問題の通りに実装すればよい
# a数列を降順にソートしておき、基準値を満たさない要素が出てきた時点でforループを終了する、という風にすると処理効率が高まる
# そのようにしなくても正しい解は得られるので必須ではない

n,m = map(int,input().split())
a = sorted([int(x) for x in input().split()], reverse=True) # 順序は替えても問題ないので、降順にソートしておく
total = sum(a)
ref_value = total*(1/(4*m))
pop_goods = 0

#print(m); print(total,":",ref_value,a)

for goods in a:
    #print(ref_value,":",goods)
    if goods >= ref_value:
        pop_goods += 1
    else:
        break
    
    if pop_goods == m:
        print("Yes")
        exit()
        
print("No")