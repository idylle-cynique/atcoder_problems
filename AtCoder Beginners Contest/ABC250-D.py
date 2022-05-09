

import bisect

def elatos(n):
      x = 2
      shieve = set([int(x) for x in range(2,n+1)])
      garbage = set()
      check_list = set()

      while(x*x < n):
            garbage = set([x*int(i)+x for i in range(1,n//x+1)])
            shieve -= garbage
            check_list.add(x)
      
            #print(shieve)
            #print(min(shieve-check_list))
      
            x = min(shieve-check_list)
      
      return shieve

N = int(input())

cnt = 0
max_q = int(N**(1/3)//1)
primes = sorted(elatos(max_q))

for q in primes:
    div = min(N//(q**3),q)
    div = min(div,q)

    if div == q:
        div -= 1
    idx = bisect.bisect_right(primes, div)
    #print(q,":",q**3,div); print(f"-> {idx}?")
    cnt += (idx)

print(cnt)