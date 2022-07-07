''' ABC235 - A
    問題文で求められている内容をそのまま実装するだけでよい
'''

abc = input()
a,b,c = [x for x in abc]
abc = int(a+b+c)
bca = int(b+c+a)
cab = int(c+a+b)
print(abc + bca + cab)