# ABC206 - B

# A問題同様にそのまま実装すればよい
# Nの入力値として10^9のようなきわめて大きな値も与えられるが、全く問題なく高速に処理が可能

N = int(input())

day = 0
money = 0

while(money < N):
    day += 1     # 日数を数え上げる
    money += day # 現時点の日数分だけお金を加える

print(day)