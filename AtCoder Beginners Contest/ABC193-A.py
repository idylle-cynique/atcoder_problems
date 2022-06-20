''' ABC193 - A
    そのまま計算するだけでよい
'''

a,b = [int(x) for x in input().split()]
print(((a-b)/a)*100)