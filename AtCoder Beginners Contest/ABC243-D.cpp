/*  ABC243 - D
    二分木の操作+αという構成の問題

    基本的には問題の要求通り配列に対する二分木処理を再現するだけでよいが
    二分木の移動範囲が非常に大きく、C++のような算術オーバーフローを考慮しなければならない言語では勿論のこと
    pythonのような多倍長整数計算が可能な言語でも、計算値が大きくなりすぎるために制限時間内での処理が難しい場合がある

    ただし、この問題では問題文の最後に
        ”なお、答えが 10^18 以下になるような入力のみが与えられます。”
    という御都合主義的な条件が示されており、最終的な値は計算・出力が容易な程度の大きさに留まるように設定されている
    つまり、二分木の操作に着目して、実際に計算する必要のない処理を上手く省いて計算することで
    比較的小さい値での処理にまとめることができそうだ、と推察できる

    具体的な処理の省略方法についてだが、例題を用いて番号を考慮せずに各ノードの移動パターンだけに着目してみると
    「子ノードに移動し、再び親ノードに移動する」あるいは「親ノードに移動して、再び子ノードに移動する」
    といったような操作の場合、行って戻るだけなので計算を省いても正しい解が得られる

    したがって、このようなパターンを上手く省いていけばよい
    具体的な実装については、vectorをスタックに見立てて、スタックの頂点の要素(移動命令)と次に追加する要素(移動命令)が
    先に示したようなパターンの場合は取り出した後スタックには格納せずに破棄する、といったような具合にすることで実現している
    C++の場合専用のモジュール<stack>が存在するが、これは単にスタックの処理内容をよりそのまま簡単な形で利用できるように
    vectorをラップしたものなので、vectorを用いても特に問題はない
*/
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;
int main(void){

    unsigned long long int N,X;
    string commands;
    
    cin >> N >> X;
    cin >> commands;
    
    unsigned long long int node = X;
    stack<string> commands_stack;
    string c;
    string push_ele, top_ele;

    // 省略可能な処理をスタックから取り除く
    for(int i=commands.size(); i>=0; i--){
        if(commands_stack.empty()){ 
            c = commands[i];
            commands_stack.push(c);
        }else{
            push_ele = commands[i];
            top_ele = commands_stack.top();
            if((push_ele == "L" && top_ele == "U") || (push_ele == "R" && top_ele == "U")){
                commands_stack.pop();
            }
        }
    }
    
    // 二分木のノード移動処理を再現
    for(int i=0; i<commands.size(); i++){
        c = commands[i];
        if(c == "U") {node /= 2;}
        
        if(c == "L") {node *= 2;}
        
        if(c == "R") {node *= 2; node += 1;}
        // cout << commands[i] << " : " << node <<  endl;
    }

    // 解答出力
    cout << node << endl;
}
