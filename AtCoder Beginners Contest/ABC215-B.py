''' ABC215 - B
N の制約が10^18と非常に大きいが、累乗によるループのため全く問題なく動作する
N = 10**18のときでも、ループ処理は60回程度で打ちとめとなる
'''
N = int(input())
n = 2
k = 0

while(n**(k+1) <= N):
    k += 1

print(k)