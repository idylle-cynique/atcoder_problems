# ABC233 - B

'''
    求められている処理をそのまま実装すればよい
'''

L,R = map(int,input().split())
String = input()

front = String[:L-1]
rear = String[R:]
rev_String = String[L-1:R]
rev_String = rev_String[::-1]

print(front + rev_String + rear)