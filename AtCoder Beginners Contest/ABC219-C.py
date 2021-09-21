# ABC219 - C

def how_to_solve():
    '''
    愚直に新しい辞書順にソートすることを考えるのではなく、
    受け取った名前を新しいアルファベット順から旧いアルファベット順に直した場合どのような文字列になるか、を考え
    旧いアルファベット順に直された文字列をsorted()でソートする、というふうに発想を変えてやると上手く解くことができる

    具体的な手順は以下の通り

    1.) 新旧のアルファベットがそれぞれ順番的にどの文字がどの文字に対応するかを考える
    2.) 受け取った名前を、順番的に対応する旧いアルファベットに変換し、辞書順にソートできるようにする
    3.) 新しいアルファベット順での名前と旧いアルファベット順の名前を辞書型リストでまとめ、対応付ける
    4.) 旧いアルファベット順で並べた名前リストをもとに、辞書から対応する新しい名前を出力する
    '''
    
OldAlphs = list("abcdefghijklmnopqrstuvwxyz")
NewAlphs = list(input())

N = int(input())
Names = [input() for _ in range(N)] # 入力文字列を受け取る
NewDict = {}  # 新しいアルファベット順での辞書
NewNames = [] # 新しいアルファベット順に直した名前のリスト
NameDict = {} #

def convert_Name(old_name): # 古いアルファベット順から新しいアルファベット順に変換
    ret_str = ""
    for c in old_name:
        ret_str += OldAlphs[NewDict[c]]
    
    return ret_str

for i in range(len(NewAlphs)): # 新しいアルファベット順に辞書順での番号を付与して辞書化
    NewDict[NewAlphs[i]] = i
#print(New_Dict)

for name in Names:
    ele = convert_Name(name)
    NewNames.append(ele)
    NameDict[ele] = name # 旧い名前と新しい名前とを対応付ける

NewNames = sorted(NewNames) # 辞書順に並べ替える

for name in NewNames: # 解を出力
    print(NameDict[name])
        
        