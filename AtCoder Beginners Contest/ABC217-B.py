''' ABC217 - B
    問題で要求されている通りに実装すればよい
'''

Contests = ["ABC", "ARC", "AGC", "AHC"]
Inputs = [input() for i in range(3)]

for c in Contests:
    if c not in Inputs:
        print(c)