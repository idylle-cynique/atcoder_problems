# SOMPO HD プログラミングコンテスト2021(ABC192) - C

# 問題文の通りに実装すればよい問題。ここでは問題文で求められている処理を関数としてまとめた
# こちらの方が基本的な流れが明確で、あとから見た場合でも見当がつく

def func_for_this_question(num):
        a = sorted(list(str(num)),reverse=True)
        b = sorted(list(str(num)),reverse=False)
        
        #print(a,b)
        g_1,g_2 = "",""
        
        for i in a:
                if i == 0:
                        continue
                g_1 += i
        
        for i in b:
                if i == 0:
                        continue
                g_2 += i
        
        #print(g_1,g_2,":",int(g_1) - int(g_2))
        return int(g_1) - int(g_2)

        
n,k = [int(x) for x in input().split()]
ans = n

for i in range(k):
        ans = func_for_this_question(ans)
        
        if ans == 0:
                break

print(ans)