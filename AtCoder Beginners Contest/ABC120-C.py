# ABC120 - C
import collections

# 処理する文字列の長さが大きいので、愚直に処理を行おうとするとTLEになってしまう
# キューブは"0"と"1"の二種類しかなく、二個のキューブの取り外し処理はどちらか一方が無くなるまで続く
# とすると、具体的に処理を行わなくとも、各キューブの個数から自動的に解が求まる

s = input()
s_cnt = collections.Counter(s)
print(min(s_cnt["1"],s_cnt["0"])*2)