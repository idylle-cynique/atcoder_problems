''' ABC011 - C
    問題で要求されている通りの処理をそのままシミュレートすることで正答を得ることができる
    シミュレートするのは、問題における最適なステップパターンで、
    これは貪欲(greedy)法を用いることで得られる

    具体的には
        1) ある地点から1～3までステップした時にNGマスに当たるか当たらないかをチェック
            i) この時可能な限りステップ数を削減したいので、チェックは3マス→2マス→1マスという順で試す
        2) ステップ可能なら対象のマスに移動
        3) 移動先がゴール(0)、あるいはステップ移動が不可能だったりステップ回数制限に達した場合には
           シミュレートを終了する
    といった処理を行えばよい

    この他コーナーケースとして、「スタート地点が既にNG地点の場合」というものがあるので注意すること
'''


N = int(input())
NGs = set([int(input()) for _ in range(3)])
Steps = [3,2,1]
now = N
goal = 0
limit = 100
counter = 1

while(now != goal and counter <= limit and now not in NGs):
    #print(counter,":",now,goal)
    idx = 0
    counter += 1
    while(idx < len(NGs)):
        #print(now,Steps[idx])
        if (now - Steps[idx] not in NGs) and (now - Steps[idx] >= 0):
            now -= Steps[idx]
            break
        idx += 1
    else:
        continue

answer = "YES" if now == 0 else "NO"
print(answer)
