# ABC239 - D

'''
    値の制約に着目すると、高橋君・青木君の2人が出す整数値の組み合わせとして有り得るのは
    最大でも100×100 = 10^4個程度しかないことがわかる。ここからさらに各値について素数判定を行うにしても、
    そのまま愚直にO(√N)で整数Nの素数判定を行っても、高々10^5×2程度のループ処理で全探索を行うことができる

    実装にあたっての判定処理は、青木君がどのような整数を出しても素数値にならないような値を高橋君が出した場合に
    勝利者を高橋君として出力して終了、そのまま全探索を終えてしまった場合には青木君と出力して終了、といった具合にしている

    また、ここでは素数判定にエラトステネスの篩を用いたsetを利用して、前処理をO(N・loglogN)、判定をおおむねO(1)で出来るようにした
    ここでは通常の素数判定と実速度は変わらないが、素数判定に掛かる時間が大幅に短縮されるため、
    1～1000までの場合など、制約がより大きいようなときでも十分高速に機能する
'''

def another_answer(): # 通常の素数判定を利用した場合(AC確認済)
        def isprime(x):
        i = 2
        while(i**2 <= x):
            #print(x,":",i)
            if x%i == 0:
                return False       
            i += 1
        return True

    A,B,C,D = map(int,input().split())

    for n in range(A,B+1):
        answer = "Takahashi"
        for m in range(C,D+1):
            #print(n,n+m)
            
            if isprime(n+m):
                answer = "Aoki"
                continue
        
        if answer == "Aoki":
            continue
        else:
            print("Takahashi")
            exit()

    print("Aoki")

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

primes = elatos(100+100)
A,B,C,D = map(int,input().split())

for n in range(A,B+1):
    answer = "Takahashi"
    for m in range(C,D+1):
        #print(n,n+m)
        
        if n+m in primes:
            answer = "Aoki"
            continue
    
    if answer == "Aoki":
        continue
    else:
        print("Takahashi")
        exit()

print("Aoki")