''' ABC193 - B
    実際に高橋君がN軒の店を回ってゲーム機を買い求めている状態をシミュレートすればよい
    時間経過処理については、直接0.5分という小数で扱うよりは
    10倍処理などを施して整数として扱う方が比較処理などでも不具合がなく安全性が高い
    
    なお、ここでは入力値の受取時に先に事前処理を施してからシミュレートを行っている
'''

n = int(input())
shoplist = []
ans = 10**9

for i in range(n): 
        tmp = [int(x) for x in input().split()]
        tmp[0] = tmp[0]*10-5 # 計算しやすいように10倍して整数化、さらに一律1分おきに在庫が減る、と解釈できるようにしておく
        tmp[2] -= 1          # 最初の5分での在庫減少分を先に計算しておく
        shoplist.append(tmp) 

for i in shoplist:
        #print(i); print(i[0]//5)
        if i[0]//10 >= i[2]: # 在庫がもうない場合
                continue

        ans = min(ans,i[1])

if ans == 10**9:
        print(-1)
else:
        print(ans)