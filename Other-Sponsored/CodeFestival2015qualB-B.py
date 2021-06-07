# Code Festival 2015 Qual-B - B

# 問題文で要求されたとおりの処理をそのまま実装すればよい
# collections.Counterを利用すると実装が楽

from collections import Counter

N,M = map(int,input().split())
Answers = [int(x) for x in input().split()]
answers_data = Counter(Answers)
#print(answers_data)

for key,value in answers_data.items():
    if value > N//2:
        print(key)
        exit()
    else:
        pass

print("?")