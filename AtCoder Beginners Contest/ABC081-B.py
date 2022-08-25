''' ABC081 - B
    数列の最大の長さは200と小さいので問題文に書かれている処理を
    そのまま愚直な形で実装して問題ない
'''
n = int(input())
a = [int(x) for x in input().split()]
flag = True
count = 0
while(flag == True):
    for i in a:
        if i%2 != 0:
            flag = False
      
    if flag == True:
        count += 1
        for i in range(len(a)):
            a[i] //= 2

print(count)