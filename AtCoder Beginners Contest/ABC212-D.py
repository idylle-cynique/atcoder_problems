''' ABC212 - D
    問題を解くにあたってのポイントとなる部分は以下の2つ
        1) 操作3「数列中の要素のうち最小のものを取り出す」をいかに実現するか
        2) 操作2「数列中の要素の値すべてにX_iを加える」をいかに実現するか
    
    まず1)については、最小の要素(最大でもよい)を高速に取り出す処理を実現するものとして
    ヒープ(優先度付きキュー)が容易に思い浮かぶ。
    pythonの場合は、標準モジュールheapqを用いてこれを実現すればよい

    2)については、制約の関係上実際に値の書き換え処理を行ってしまうと
    全体でのクエリの処理O(N)に加えて、操作2で優先度付きキューに対して線形計算量の処理が発生する
    仮に操作が全体のクエリの1/3程度に収まるとしても10^9～10^10ものループ処理が発生し
    到底制限時間内に処理を終えることはできない
    何かしらの工夫を施してO(1)～O(logN)程度の計算量でここの処理を実現する必要がある

    ここでは、ある要素(ボール)を数列内に加え入れ、その後取り出す際に
    「いつ入れたか」「いつ出したか」の情報と「その間に操作2で加算するように求められた値」
    の3つが分かっていれば、取り出した時点に一発計算して出力することが可能そうだ、という着眼点から
    「i番目のクエリを処理するまでにどれだけ操作2で加算値が与えられたか」の情報を格納した
    累積和リストacm_sumを用意し、更に各要素をいつ入れたかが分かるように、優先度付きキューに
    格納する要素にクエリの番号情報も付与した([要素, クエリ番号]といったような形)
    これによって操作3を行う際に
        その要素(ボールに書かれた値) + 現時点(操作3で取り出される)までに加算された値 - 対象の要素を格納する前に加算された値
    といったような計算を行うことで操作3の処理を実現することができる

    それから、操作2によって書き換え処理が行われることでその後に追加される要素との大小関係が変動し得るので
    操作1では、値そのまま要素の追加処理をすることはできないことに注意する必要がある

    操作2を省略しても数列中の要素の大小関係が維持されるように、ここでも累積和リストを利用し、
    「ある操作1の処理を行うまでに加算処理するよう求められた値の総和」を追加する要素から差し引いた上で
    優先度付きキューに加え入れる必要がある
'''

import heapq

class PriorityQueue:
    priorityqueue = list()

    def __init__(self,lst=list())->None:
        self.priorityqueue = lst
        heapq.heapify(lst)
    
    def heappush(self,element)->None:
        heapq.heappush(self.priorityqueue,element)
    
    def heappop(self):
        ret_ele = self.priorityqueue[0]
        heapq.heappop(self.priorityqueue)
        return ret_ele
    
    def __repr__(self)-> str:
        return f"PriorityQueue({self.priorityqueue})"


Q = int(input())
priority_queue = PriorityQueue()
acm_sum = [int(0) for x in range(Q)]

for i in range(Q):
    query = list(map(int,input().split()))
    
    if len(query) > 1:
        command,number = query
    else:
        command = query[0]

    if command == 1:
        acm_sum[i] = acm_sum[i-1]
        priority_queue.heappush([number-acm_sum[i],i])
    elif command == 2:
        acm_sum[i] = number + acm_sum[i-1]
    elif command == 3:
        acm_sum[i] = acm_sum[i-1]
        ball,idx = priority_queue.heappop()
        ball = ball + acm_sum[idx] + (acm_sum[i] - acm_sum[idx])
        print(ball)
        #print(acm_sum[i],acm_sum[idx])

