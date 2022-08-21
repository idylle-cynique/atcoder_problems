''' ABC235 - D
    まずサンプル入出力を手作業で解いてみると見通しが立ちやすい
    問題中で行う処理は同じ桁数の別の値に変更する処理か、或いはより大きな値へと変更する処理しかない
    つまりx=1からNへと近づけていく処理を重複的な探索だけは確実に避けつつ手あたり次第に探索していけば
    自ずとNになるか、でなければNにはなりようのない値(Nより大きい値)になる

    あとはどうやって探索するかだが、幅優先探索がここでは適している
    Nの値は最大2*10^5でaは少なくとも2以上(最低でも2倍処理)なので、
    到達までにかかる探索(再帰的処理)回数はそれほど多くなることはなく、十分高速に問題を解くことができる
'''

from collections import deque

a,N = map(int,input().split())
dist = 1
digitN = len(str(N))
queue = deque([1])
distdict = {1:0}
reachable = set([1])

while(queue):
    number = queue.popleft()

    new_number = number*a
    new_digit = len(str(new_number))
    
    if new_digit <= digitN and new_number not in distdict:
        queue.append(new_number)
        reachable.add(new_number)
        distdict[new_number] = distdict[number]+1
        
    if number >= 10 and number%10:
        digit = len(str(number))
        new_number = (number%10)*(10**(digit-1)) + number//10
        #print(new_number)
        new_digit = len(str(new_number))
        if new_digit <= digitN and new_number not in distdict:
            queue.append(new_number)
            reachable.add(new_number)
            distdict[new_number] = distdict[number]+1
    #print(queue)

answer = distdict[N] if N in distdict else -1
    
print(answer)