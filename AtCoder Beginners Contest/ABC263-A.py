''' ABC263 - A
    フルハウスは同じ値のカード3枚と2枚の組み合わせによる役なので、
    Counterを用いて各数字のカードの出現回数を記録し、5枚のカードがこれに対応するかどうか調べればよい
'''

from collections import Counter
card = list(map(int,input().split()))
carddata = Counter(card)
flag = False

if len(carddata) == 2:
    for cnt in carddata.values():
        #print(cnt)
        if not(cnt == 2 or cnt == 3): break
    else:
        flag = True

answer = "Yes" if flag else "No"

print(answer)