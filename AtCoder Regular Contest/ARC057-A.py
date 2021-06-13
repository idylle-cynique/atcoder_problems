# ARC057 - A

# おおむね、要求された通りに実装を行えばよい
# ただし、K = 0のとき 一日の上昇幅は 1+0*t = 1とたった1円の上昇に留まるので2000ms以内で処理を終えることができない
# この部分についてのみコーナーケースとして別途処理を行うようにすること

A,K = map(int,input().split())
    
money = A
day = 0

if K == 0: # コーナーケース
    print(2*10**12 - money)
    exit()
    
while(money < 2*10**12):
    #print(money)
    money += (1+K*money) # 所持金を 1+K*t分だけ増やす
    day += 1             # 経過日数をインクリメント
    
print(day)