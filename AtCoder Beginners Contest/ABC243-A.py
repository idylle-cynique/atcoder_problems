# ABC243 - A

'''
    コンテスト中は入力値の制約を見て見通しが立てやすい、ということで愚直な探索法で解答したが
    余計な繰り返し部分は余り値を用いて省くことができ、
    これによって入力値が問題の場合より飛躍的に大きくなっても
    高速に動作させることができるため、改めて改良したコードを示す
'''

def old_answer():
    V, A, B, C = map(int, input().split())

    rest = V
    Family = {"F":A, "M":B, "T":C}
    Next = {"F":"M", "M":"T", "T":"F"}
    key = "F"

    while(rest >= Family[key]):
        #print(rest,":",key,Family[key])
        rest -= Family[key]
        key = Next[key]

    print(key)

V, A, B, C = map(int, input().split())

total = sum([A,B,C])
rest = V%total # old_answerにおける無駄な繰り返し部分は省く

if rest < A: # 父が使う分が残っているか
    print("F")
    exit()

rest -= A # 父が使った分を差し引く

if rest < B: # 母が使う分が残っているか
    print("M")
    exit()

print("T") # 高橋君が使う分が残っていることはないのでそのまま解を出力

