# ABC223 - A 

# Xが100の倍数かつX≠100であればYes, そうでなければNo
X = int(input())

if X != 0 and X%100 == 0:
    print("Yes")
else:
    print("No")