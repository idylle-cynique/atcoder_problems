# ABC231 - C
'''
 基本的には
 (1) 生徒の身長データをリストに格納しソート
 (2) 各クエリについて、x_i以上の値を取る要素の数をリスト探索によって求め、解を出力する
 という処理によって解を求めることができるが、
 (2)の処理は、そのままリストへの線形探索によってx_i未満の値を取るインデックスを求め、
 そこから|リストの長さ| - |x_i未満の値を取る要素の個数| というふうに実装すると、
 その都度O(N)の処理が行われることになり、全体ではO(N・Q)もの計算を要し、処理が間に合わない

 そのため、リストへの検索処理を何かしらの形で高速に機能させる必要がある。
 ソートされたリスト(配列)への検索ではO(logN)の高速な検索を行える二分探索アルゴリズムがあり、
 これを利用することで各クエリの処理がO(logN)で実装でき、全体でもO(Q・logN)と高速に処理を行うことができる

 ここでは自作した二分探索関数を用いて処理を行っているが、
 Pythonではリストの二分探索を行うことができるbisectモジュールが標準モジュールとして用意されているので
 そちらを使ってもいいし、そちらを使う方が手間がかからない
'''

N,Q = map(int,input().split())
Students = sorted([int(x) for x in input().split()])

def ex_binarysearch(array,val,mode=None): # 自前で実装したリストの二分探索用関数
      # モード指定で検索値未満の値のうちの最近値、検索値より大きい値のうちの最近値まで検索できるように実装した拡張版
      l,r = 0,len(array)-1
      idx = (r+l)//2
      #print("start:",idx,array[l:r])
      while(l <= r):
            #print("left:",l,"-","right:",r); print("val:",val,":",array[idx]); print(idx,":",array[l:r+1])
            idx = (r+l)//2
            if array[idx] == val:
                  return idx
            elif array[idx] < val:
                  l = idx+1
            else:
                  r = idx-1
    
      if mode == None:
            return False
      elif mode == "left":
            l = max(0,l-1)
            #print("mode-> left:",l)
            if l == 0:
                  return l if array[l] < val else None
            else:
                  return l if array[l] < val else l-1
      elif mode == "right":
            r = min(r+1,len(array)-1)
            #print("mode-> right:",r)
            if r == len(array)-1:
                  return r if val < array[r] else None
            else:
                  return r if val < array[r] else r-1
      else:
            print("ERROR: mode not exist")
            return False

#print(Students)

for i in range(Q):
    q = int(input())
    
    index = ex_binarysearch(Students,q,mode="right")
    if index == None:
        index = -1
    
    if index == -1:
        print(0)
    else:
        print(len(Students) - int(index))
