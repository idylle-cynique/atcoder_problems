# ABC121 - B

n, m, c = [int(x) for x in input().split()]
bm = [int(x) for x in input().split()]
count = 0
source = 0

for i in range(n):
    tup_data = [int(x) for x in input().split()]
    #print(tup_data,end=":")
    
    for j in range(m):
        source += bm[j]*tup_data[j]
    #print(source + c)
    if source+c > 0:
        count += 1
    
    tup_data = []
    source = 0

print(count)