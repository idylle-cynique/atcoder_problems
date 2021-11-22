# ABC226 - B

'''
与えられた複数の数列から重複する数列を含めずに数え上げを行えばよい
重複を含めずに数え上げ、となると集合(set)型が思い浮かぶが、
集合型ではイミュータブル(中途変更可能)な数列リストを格納することはできない
そのため、とんちをきかせて区切り文字などで分割した文字列、
あるいは問題の制約上発生しえない10個以上の0を区切り数字として間に挟んだ数字を
setに格納する、といったようなひと手間をさらにかける必要がある
'''

N = int(input())
Nums_set = set()

for i in range(N):
    temp = list(map(str,input().split()))
    num = "-".join(temp[1:])
    #print(num)
    Nums_set.add(num)

print(len(Nums_set))
    