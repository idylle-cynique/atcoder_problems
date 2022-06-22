''' ABC194 - C
    そのまま全探索するのではTLEで不正解となる
    また求める値が差の二乗なので累積和などを用いる形でも正しい値が得られない
    
    この問題を解くためには、制約に書かれている -200 <= a_i <= 200 という部分に着目する必要がある
    a_iとして想定される値は400個までということなので、想定される計算値 |a_i-b_i|^2 の値として考えられるのは400^2程度
    この
    collectionsライブラリのCounter()を用いて各値の出現回数を事前に調べてコンテナに格納後、
    これを用いて同じ値については一括計算して出現回数分の積を取れば、要素数を大幅に減らすことができ、
    高速に解を求めることができる
'''

import collections 
n = int(input())
a = [int(x) for x in input().split()]

a_data = collections.Counter(a)
a_data_lst = []
ans = 0

for i in a_data:
    a_data_lst.append((i,a_data[i]))

for i in range(len(a_data_lst)):
    for j in range(i+1,len(a_data_lst)):
        tmp = abs(a_data_lst[i][0] - a_data_lst[j][0])**2 * a_data_lst[i][1] * a_data_lst[j][1]
        #print(a_data_lst[i][0]**2,"-",a_data_lst[j][0]**2,tmp)
        ans += tmp

print(ans)
        
    