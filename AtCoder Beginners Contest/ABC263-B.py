''' ABC263 - B
    問題の説明が(個人的には)あまりピンとこなかったが、
    内容自体は要求されているものをそのまま実装するだけでよい、というもの

    ある番目の番号とその親の番号とを辞書(map, dict)などを用いて対応付けて記録し
    1番目の親の番号に対応する親の番号に対応する親の……といった具合に再帰やwhileループを用いて
    番号Nが何代前になるかを調べればよい

    こういった書き方はUnionFindTreeの実装などで求められることがあり、
    おそらくそのあたりを念頭に置いた問題とされる
'''

N = int(input())
parent = [int(x) for x in input().split()]
parentdict = dict()

for i,p in enumerate(parent):
    i += 2
    if i not in parentdict:
        parentdict[i] = p

#print(parentdict)
cnt = 1
key = N

while(parentdict[key] != 1):
    #print(key,parentdict[key])
    cnt += 1
    key = parentdict[key]

print(cnt)