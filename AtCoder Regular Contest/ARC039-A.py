# ARC039 - A

# 想定すべきパターンは次の通りなので、全探索してうち最大になるものを出力すればよい
# (aaa-bbb), (9aa-bbb), (a9a-bbb), (aa9-bbb), (aaa-1bb), (aaa-b0b), (aaa-bb0)

A,B = map(int,input().split())
max_diff = A-B

for i in range(3):
    tmp_str = list(str(A))
    tmp_str[i] = "9"
    tmp_int = int("".join(tmp_str))
    #print(tmp_int)
    
    max_diff = max(max_diff,tmp_int-B)

for i in range(3):
    if i == 0:
        tmp_str = list(str(B))
        tmp_str[i] = "1"
        tmp_int = int("".join(tmp_str))
    else:
        tmp_str = list(str(B))
        tmp_str[i] = "0"
        tmp_int = int("".join(tmp_str))
    #print(tmp_int)
    
    max_diff = max(max_diff,A-tmp_int)

print(max_diff)
