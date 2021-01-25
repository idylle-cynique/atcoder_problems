# ABC189 - D

# 解説AC
# まだ十分に理解していないが、S_nである真理値を得たいとき、その前のS_n-1の値によって値の得方が決まるのはわかる

def pre_logic(t):
      if len(t) == 0:
            return 1
      else:
            if t[0] == "AND":
                  return 1 * pre_logic(t[1:])
            else:
                  return 2**len(t) + pre_logic(t[1:])

n = int(input())
s = [input() for x in range(n)]
s = s[::-1]

print(pre_logic(s))