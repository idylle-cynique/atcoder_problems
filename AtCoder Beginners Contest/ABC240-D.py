# ABC240 - D

'''
    基本的には、問題で示されている処理をそのまま再現することで解を求めることができるようになっている
    ただし、そのまま愚直に処理を再現すると、たとえば10^5の値が書かれたボールを10^5個積み上げるような入力値が
    与えられた場合、「一番上のボールと同じ番号が書かれたボールが何個重なっているか」のチェックに
    1個目から10^5個目まで積み上げるまでに((1+10^5)*10^5)//2 ≒ 10^10ものループ処理が必要となり、
    制限時間内に処理を完了することができない

    したがってこの「一番上のボールと同じ番号が書かれたボールが今何個重なっているか」
    のチェックを高速に行う方法を考えなければならない

    ここではランレングス圧縮のアルゴリズムの発想を利用して、ボールの番号と一緒に
    「今連続して重なっているボールの数」をリストで格納し、このリストをスタックに積み上げるようにすることで
    上記の処理と「ボールに書かれた値と同じ数だけ積まれたボール群の処理」をそれぞれO(1)で行えるようにした
    これによって全体の計算はN個のボールのスタック処理のみ、すなわちO(N)で問題の処理が再現でき
    制限時間内に高速に解を求めることができる
'''

def false_answer(): # 愚直に問題文を再現した場合(TLEで不正解)
    N = int(input())
    Balls = [int(x) for x in input().split()]

    Stack = []

    for ball in Balls:
        Stack.append(ball)
        #print(Stack)
        
        cnt = 0
        check = ball

        for i in range(len(Stack)-1,-1,-1):
            if Stack[i] == check:
                cnt += 1
            else:
                break
        #print(ball,cnt)
        if ball == cnt:
            for _ in range(ball):
                Stack.pop()
        
        print(len(Stack))



N = int(input())
Balls = [int(x) for x in input().split()]

Stack = []
total = 0

for ball in Balls:
    #print(ball,":")
    if len(Stack) == 0:
        Stack.append([ball,1])
    elif Stack[-1][0] == ball:
        Stack[-1][1] += 1
    else:
        Stack.append([ball,1])
    
    total += 1
    #print(Stack)
    
    if Stack[-1][0] == Stack[-1][1]:
        total -= Stack[-1][-1]
        Stack.pop()
    
    print(total)