/* ABC260 - A
    そのまま問題文の通り実装すればよい
    ここではPythonにおけるCounterのようなものを作成して、
    そこからカウンタの値が1である文字列を取り出す、
    といったような具合にして解を出力している
*/

#include <iostream>
#include <string>
#include <map>
using namespace std;
int main(void){
    string S;
    string key;
    string answer = "";
    map<string, int> counter;
    cin >> S;
    
    for(int i=0; i<3; i++){
        //cout << S[i] << endl;
        key = S[i];
        
        if(counter.find(key) != counter.end()){
            counter[key] += 1;
        }else{
            counter[key] = 1;
        }
    }
    
    for(auto itr=counter.begin(); itr!=counter.end(); itr++){
        //cout << itr->first << ": " << itr->second <<  endl;
        if(itr->second == 1)    answer = (itr->first);
    }
    
    if(answer.size()) cout << answer << endl;
    else              cout << -1 << endl;
}
