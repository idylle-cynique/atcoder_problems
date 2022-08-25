/* ABC081 - C
    最小のボール(要素)の書き換え回数で問題の処理を完了したい場合
    出現個数の少ない番号が書かれたボールから順に書き換えればよい

    ここではcounter関数を用いて各値の出現回数を記録したunordered_map(dict)を生成
    さらにこれを二次元vectorに変換したものを用意し、
    出現回数(ここでは二次元vectorの1列目の要素)をキーとしてソートし、
    出現回数の少ない値から順に読み出せるようにする

    あとは頭から順に値の種類がK種類になるまでボールの出現回数を変数に記録し
    最後にそれを出力すればよい
*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

unordered_map<int, int> counter(vector<int> sample){
    unordered_map<int,int> count_map;
    int key;

    for(int i=0; i<sample.size(); i++){
        key = sample[i];
        
        if(count_map.find(key) != count_map.end()){
            count_map[key] += 1;
        }else{
            count_map[key] = 1;
        }
    }
    return count_map;
}

template<typename Type_>
std::ostream& operator<<(ostream& os, vector<Type_>& coutvec){
    cout << "{";
    for(auto itr = coutvec.begin(); itr != coutvec.end(); itr++){
        if(itr != coutvec.end()-1)    os << *itr << ", ";
        else                          os << *itr;
    }
    cout << "}";
    return os;
}

int main(void){
    int N,K;
    cin >> N >> K;
    
    vector<int> number(N);
    for(int i=0; i<N; i++) cin >> number[i];
    
    unordered_map<int,int> number_counter = counter(number);
    vector<vector<int>> counter_vec(number_counter.size(),{0,0});
    int pos = 0;
    
    for(unordered_map<int,int>::iterator itr = number_counter.begin(); itr != number_counter.end(); itr++){
        counter_vec[pos] = {itr->first, itr->second};
        pos += 1;
    }
    
    //for(vector<int> vec: counter_vec) cout << vec << endl;
    
    sort(   // 第一引数でソートさせる
        counter_vec.begin(),
        counter_vec.end(),
        [](const vector<int> &alpha,const vector<int> &beta){return alpha[1] < beta[1];}
        );
    
    //for(vector<int> vec: counter_vec) cout << vec << endl;
    int looptime = counter_vec.size()-K;
    int answer = 0;
    
    for(int t=0; t<looptime; t++) answer += (counter_vec[t][1]);
    cout << answer << endl;
    
}