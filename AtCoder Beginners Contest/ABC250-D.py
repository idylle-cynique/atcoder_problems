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

q = 2
cnt = 0
max_q = int(N**(1/3)//1)
print(N,":",max_q)
primes = sorted(elatos(max_q))

print(primes[:100])
for p in primes:
    div = N//(p**3)
    print(p,":",p**3,div)

    div = min(div,q)

    idx = bisect.bisect_left(primes, div)
    print(f"-> {idx}?")

    cnt += (idx)

    

