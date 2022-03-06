# ABC241 - A

'''
    そのまま実装するだけでよい
'''

A,B,C,X = map(int,input().split())

if X <= A:
    ans = float(1)
elif A<X and X<=B:
    ans = C/(B-A)
else:
    ans = float(0)

print(ans)