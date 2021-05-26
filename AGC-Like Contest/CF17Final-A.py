# Code Festival 2017 Final - A

# ・入力文字列が正解文字列よりも長い場合は常に間違いであること。
# ・正解文字列未満の文字列パターンは容易に全探索が可能であること。
# の二点に着目して、bit全探索により"AKIHABARA"中の任意の数の文字を抜き出して順番に並べ、その中から条件を満たすものを抜き出して集合として格納
# 最後に入力値がその中に含まれるか、をYES-NOで返せばよい

S = input()
Akiba = "AKIHABARA"          # 全探索文字列
Check_string = list("KIHBR") # 必ず含まれている必要のある文字列
correct_strings = set()

for i in range(2**(len(Akiba))):　
    tmp = ""
    for j in range(len(Akiba)): # bit全探索で文字列を生成
        #print(i>>j&1,end="")
        if (i>>j&1) == 1:
            tmp += Akiba[j]
    
    for k in Check_string: # for-else文による分岐
        if k not in list(tmp): # 必要な文字が入っていない場合はチェック終了
            break 
    else:                      # チェックをパスした文字列を格納
        correct_strings.add(tmp) 
#print(correct_strings)            

if S in correct_strings:
    print("YES")
else:
    print("NO")