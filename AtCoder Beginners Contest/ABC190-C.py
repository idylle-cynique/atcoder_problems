# ABC190 - C

def check_condition(choice, conditions):
      cnt = 0
      for c in conditions:
            if c[0] in choice and c[1] in choice:
                  cnt += 1
      return cnt
                  

n,m = [int(x) for x in input().split()]
conditions = [[int(x) for x in input().split()] for y in range(m)]

k = int(input())
balls = [[int(x) for x in input().split()] for y in range(k)]

choice = set()
ans = 0

#print(conditions); print(balls)

for i in range(2**k):
      for j in range(k):
            if (i>>j)&1 == 1:
                  choice.add(balls[j][1])
            else:
                  choice.add(balls[j][0])
      
      ans = max(ans, check_condition(choice, conditions))
      #print(choice); print(ans)
      choice = set()
      
print(ans)