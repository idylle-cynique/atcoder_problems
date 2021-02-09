# ABC173 - C

# h,wの値が小さい数にとどまっているので、bit全探索による全探索で解答を求めることが出来る
# 探索の実装にやや複雑であること、リストの参照にcopy(deepcopy)を用いる必要があることに注意する必要がある

import copy

def check_block(c):
      h_c,h_w = len(c),len(c[0])
      cnt = 0
      for i in range(h_c):
            for j in range(h_w):
                  if c[i][j] == "#":
                        cnt += 1
      return cnt

def view_list(lst):
      for i in lst:
            print(i)
      return True
      
h,w,k = [int(x) for x in input().split()]
c = [list(input()) for x in range(h)]
ans = 0

for i in range(2**(h+w)):
      tmp = copy.deepcopy(c)
      
      for j in range(h+w):
            #print((i>>j)&1,end="")
            
            if (i>>j)&1 == 1:
                  if j < h:
                        for l in range(w):
                              tmp[j][l] = "."
                  else:
                        for l in range(h):
                              tmp[l][h+w-j-1] = "."
      
      if check_block(tmp) == k:
            #print("check:",check_block(tmp)); view_list(tmp);
            ans += 1

print(ans)
