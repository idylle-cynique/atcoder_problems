# ABC219 - B

# コマンド部分は先入れ先出しなので、queueによる実装にしてみてもいい

Strings = [input() for _ in range(3)]
Commands = list(input())
Answer = []

for c in Commands: # コマンドを前から順に取り出していく
    Answer.append(Strings[int(c)-1]) # 対応する文字を解答文字列に加えていく

print("".join(Answer))    