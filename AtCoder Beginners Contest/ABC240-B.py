# ABC240 - B

'''
    重複した値は格納しない集合(set)型を利用して入力値を格納してやると
    その集合の長さがそのまま解となる

    ただし、この問題の場合では与えられる数列の長さが最大で1000と小さいので
    そのままソートした数列を愚直に線形探索を利用して重複チェックを行い、
    重複を取り除いた場合の数列の長さを求めることも可能

    また、入力された数列をソートしても解の導出に問題がない、というところに着目して
    重複チェックに二分探索などを利用すれば、愚直な全探索でも解の高速化が可能
'''

N = int(input())
A_set = set([int(x) for x in input().split()])

print(len(A_set))
    