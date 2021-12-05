# ABC211 - B
# ここでは真偽判定に集合演算を用いている

S = [input() for i in range(4)]
condition = {"H","2B","3B","HR"}
#print(condition - set(S))

if condition - set(S):
    print("No")
else:
    print("Yes")