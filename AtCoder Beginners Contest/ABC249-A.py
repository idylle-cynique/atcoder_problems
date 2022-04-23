'''ABC249 - A
    問題における処理をそのまま計算させることで解が得られる
    forループなどを用いて1秒ずつシミュレートすることで解を得ることもできるが、
    入力値が大きくなった場合それでは高速に処理できないので、計算式を自分で組み立てるのが望ましい
'''

A,B,C,D,E,F,X = map(int,input().split())

def calc_movingdistance(runtime,velocity,interval,joggingtime): # 走る時間、走る時の速度、休憩時間、ジョギングに取り組む時間 
    runtimes = joggingtime//(runtime+interval)             # 走る～休むまでの一連の行動を何回繰り返すか
    resttime = min(joggingtime%(runtime+interval),runtime) # 余り時間のうち何秒間まで走る時間に費やせるか
    
    base_movedist = runtimes * runtime * velocity   # 走る～休むを繰り返す過程で走った距離  
    mod_movedist = resttime * velocity              # 余り時間分で走った距離
    total_dist = base_movedist + mod_movedist       # 合計距離
    return total_dist

takahashi = calc_movingdistance(A,B,C,X) # X秒内に高橋君が走った距離を計算
aoki = calc_movingdistance(D,E,F,X)      # X秒内に青木君が走った距離を計算
#print(takahashi, aoki)

if takahashi > aoki:    # 高橋君の方が走った距離が長いとき
    print("Takahashi")
elif takahashi < aoki:  # 青木君の方が走った距離が長いとき
    print("Aoki")
else:                   # それぞれが走った距離が等しいとき
    print("Draw")