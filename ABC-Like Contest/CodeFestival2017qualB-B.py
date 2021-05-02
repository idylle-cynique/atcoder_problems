import collections

# 早い話 (t in d) == Trueであればいい、ということだが、そのままでは処理が間に合わない。
# Pythonの場合はcollectionsライブラリのCounter()を用いることで簡単に実装が可能

n = int(input())
d = [int(x) for x in input().split()]

m = int(input())
t = [int(x) for x in input().split()]

# d,tの中身をそれぞれ整理
d_data = collections.Counter(d)
t_data = collections.Counter(t)

#print(d_data); print(t_data)

for i in t_data.keys():
    
    if i in d_data and t_data[i] <= d_data[i]:
        pass
    else:
        print("NO")
        exit()

print("YES")