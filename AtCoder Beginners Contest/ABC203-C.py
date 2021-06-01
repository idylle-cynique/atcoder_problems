# ABC203 - C

# 村番号のより大きな村を目指すには、友人のいる村番号の小さい村から順番に立ち寄って
# お金をもらいながらより大きな村を目指すのがよい
# したがって、友人のいる村のデータを村番号で昇順に整理したうえで
# 現在の所持金との兼ね合いを見ながらより村番号の大きな村へ移動していけばよい

N,K = map(int,input().split())
villages = []
now,mymoney = 0,K # 今いる村の番号, 今の所持金額

for i in range(N): # 友人のいる村ともらえるお金に関する入力値を受け取る
    a,b = map(int,input().split())
    villages.append([a,b])

villages = sorted(villages) # 村の情報を昇順で整列

for ville,money in villages: # 現在地から一番近くにある友人のいる村を目指して移動していく
    #print("now:",now,"to:",ville,money)
    if mymoney >= (ville-now): # 友人のいる村に行くのに必要な分だけの所持金額があるとき
        mymoney -= (ville-now)  # 所持金から移動にかかったお金を差し引く 
        now = ville             # 現在地を次の村の村番号に変更
        mymoney += money        # 村の友人からお金を貰って所持金額に加える

if mymoney > 0: # まだ所持金が余っているとき
    now += mymoney  # すべてのお金をつぎ込んで移動できるだけ移動する
    mymoney = 0     # 所持金は0になる(しなくても問題ない処理ではある)

print(now)