# ABC098 - C

# 実際にそのままある点を選んだ時に点よりも西側にいて西側を向いている人間、
# 東側にいて東側を向いている人間の数をその都度数えようとすると、処理が間に合わずTLEになってしまう
# 事前に列中の各人がどちらを向いてるかを整理しておけば、端から順番に各要素の値を見るだけで
# 向きを変えさせる必要のある人間の数が求められる

from collections import Counter

n = int(input())
s = list(input())

wests = {"W":0,"E":0}
easts = Counter(s)

ans = 3*(10**5)

for ele in s:
    # ele をリーダーにしたときに向きを変える必要のある人の数を考える
    
    easts[ele] -= 1 # リーダーに設定した人間を取り除く
    
    x = wests["W"] # リーダーよりも西側の人間で、西を向いている人の数
    y = easts["E"] # リーダーよりも東側の人間で、東を向いている人の数
    
    #print(x+y,":",str(wests["W"])+"+"+str(easts["E"]))
    ans = min(ans,x+y) # x+yが最小値になる場合 ans に記録
    
    wests[ele] += 1 # 検証を終えたので西側にいる人間として加える

print(ans)