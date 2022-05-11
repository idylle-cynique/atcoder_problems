''' ABC250 - B
    問題で要求されている通りに実装を行えばよい
    ただし、文字列でタイルを生成する際にブロックベースで文字列を生成しようと
    するとかえって処理が複雑になってしまう

    ブロックベースではなく、1行ごとにパターンを生成したあと、
    A行単位分だけパターンを並べて行単位で文字列を生成していくのが好ましい

    もちろん、行の偶奇によってパターンも1ブロックずつズレるので
    ズレたパターンも用意して交互に並べること
'''

N,A,B = map(int,input().split()) # A行B列のパターン

base_pattern0 = "."*B # 白いタイルをB個分だけ並べる
base_pattern1 = "#"*B # 黒いタイルをB個分だけ並べる

def print_pattern(pattern): # 解の出力
    for line in pattern:
         print("".join(line))
         
line_pattern0 = ""  # 一行ごとのパターンを記録(偶数列)
line_pattern1 = ""  # 一行ごとのパターンを記録(奇数列)
for n in range(N):  # 偶奇に対応するタイルパターンを並べていく
    if n%2:
        line_pattern0 += base_pattern0
        line_pattern1 += base_pattern1
    else:
        line_pattern0 += base_pattern1
        line_pattern1 += base_pattern0

pattern0 = []
pattern1 = []
#print(line_pattern0, line_pattern1)

for n in range(A):  # 指定された行数分だけ同じものを並べ、A行単位でのパターンを生成
    pattern0.append(line_pattern0)
    pattern1.append(line_pattern1)

for n in range(N):  # 偶奇に対応するA行単位のパターンを交互に出力
    if n%2:
        print_pattern(pattern0)
    else:
        print_pattern(pattern1)