# ABC220 - B

# 問題で求められているような処理を実現する関数を実装し、それをもとに計算を行えばよい
# 今回作った関数は再利用出来そうなので、修整の上で別途保存しておいた

K = int(input())
A,B = map(str,input().split())

def BaseNtoBase10(Number,Base): # Base進数で記述された文字列数字を整数型の十進数に変換する
    Nums = list(Number)
    length = len(Nums)
    ret = 0
    
    for i in range(length):
        ele = int(Nums.pop())
        ret += ele * (Base**i)
    
    return ret

Answer = BaseNtoBase10(A,K) * BaseNtoBase10(B,K)
#print(BaseNtoBase10(A,K); print(BaseNtoBase10(B,K))
print(Answer)