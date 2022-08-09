''' ABC047 - C
    実際に例題について全て同じ色に変える処理を手で実現してみると、
    「白→黒ないし黒→白への色の転換が行われた回数」が答えになることが分かる
    なお、これは入力文字列についてランレングス圧縮を行ったときの配列の長さ-1と同じなため、
    変数名をRunLengthとし、実際にランレングス圧縮と同じ処理を行っている
'''

Reversi = list(input())
memo = Reversi[0]
RunLength = []
cnt = 1

for ele in Reversi[1:]:
    #print(memo,"-",ele)
    if memo == ele:
        cnt += 1
    else:
        RunLength.append([memo,cnt])
        memo = ele
        cnt = 1

RunLength.append([memo,cnt])
#print(RunLength)

print(len(RunLength)-1)