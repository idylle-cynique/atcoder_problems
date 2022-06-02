'''ABC252 - C
    解法自体は単純で、実際にスロットの処理内容を探索・シミュレートして
    最速でリールの目を揃えた場合の時間を保持・出力すればよい

    問題は「ある目を揃える場合の最小所要時間をどのように求めるか」という部分
    どのリールの目も初期状態で並び合っていない、或いは全て並びあっている場合については
    そのまま「手近にあるものから順に止めていく」というようにすれば問題ないが
    一部のリールの目の初期位置が同じである場合、事情が変わってくる

    例えば入力例1の
        1937458062
        8124690357
        2385760149
    の場合で、0の目を揃える場合、一番手近にある2番目のリールを止め、
    次に2番目のリールと同じ位置にある3番目のリールを一周するまで待って止め、
    最後に1番目のリールを止める……としたくなるが、これは最速ではない

    2番目のリールを止めた後、1秒後に1番目のリールを止め、最後に9秒待って3番目のリールを止めるのが最速
    つまり、目の位置が同じであるリールが複数存在する場合、そのうちの一つを止めたあと、
    他のリールは後回しにして、それ以外の位置の異なるリールを先に止める必要があり、
    これを処理に組み込む必要がある

    ここでは、各目で止める場合を全探索する際に
    それぞれのリールを止める時間を初期位置を元に取得後、さらに同じ時刻に止められるリールが複数あった場合、
    止める時間を10秒後(一周後)に遅らせるように再設定させている
    この処理後に残った再設定後のリールを止める時間のリストを再度ソートしてやると
    一番最後の目を止めた時刻がリストの最後尾に現れ、これがその目を揃える場合の最小所要時間となる
    
    こうして０～９までのすべての目について、その目をそろえる場合の最小所要時間を求め
    その中で最も所要時間の短いものが解となる
'''

N = int(input())
Reels = [[int(x) for x in list(input())] for y in range(N)]
answers = [float('inf') for n in range(10)]

for n in range(len(Reels[0])):
    flag = False
    num_idices = []
    for r in Reels:
        num_idices.append(r.index(n))
    
    num_idices.sort()
    #print(n,":",num_idices); print(len(set(num_idices)),len(num_idices))
    prepos = 0
    k = 1
    for i in range(len(num_idices)):
        if i:
            if num_idices[i] == prepos:
                #print(k,"here:",num_idices[i],prepos)
                num_idices[i] += (10*k)
                k += 1
            else:
                prepos = num_idices[i]
                k = 1
        else:
            prepos = num_idices[i]
    num_idices.sort()
    #print(n,num_idices)
    answers[n] = num_idices[-1]

#print(answers)

answer = min(answers)
print(answer)