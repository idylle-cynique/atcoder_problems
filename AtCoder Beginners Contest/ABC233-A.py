# ABC233 - A

X,Y = map(int,input().split())
rest = max(0,Y-X)
appendix = rest//10 + int(bool(rest%10))
print(appendix)