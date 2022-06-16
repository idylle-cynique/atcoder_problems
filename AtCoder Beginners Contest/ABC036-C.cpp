/* ABC036 - C
    座標圧縮処理を求める問題。
    実装する内容は座標圧縮そのままなので、入力値を受け取ってその通りの処理を実装するだけでよい

    具体的な実装方法については、C++の場合は
        1.) 数列を受け取る
        2.) 入力値から重複を省いてソートしたvectorを別途用意する
        3.) 数列の要素を順番に取り出し、ソート済みvectorから二分探索を用いて
            高速に順番(位置)情報を持つイテレータを取り出し、先頭のイテレータ(ポインタ)との相対的な位置
            との減算によって得る
        4.) 3.)で得た値を出力する
    という流れを取るのが基本的

    Pythonの場合は、3.)の処理を二分探索ではなく事前処理した辞書(C++におけるmap)
    を用いて各値の位置をハッシュ値から高速に取り出せるようにしたほうが高速とされる(ようだ)
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

template<typename Type_> // vectorの中身をcoutで出力
std::ostream& operator<<(ostream& os, vector<Type_>& coutvec){
    cout << "{";
    for(auto element: coutvec){
        os << element << ", ";
    }
    cout << "}" << endl;
    return os;
}

int main(void){
    int N;
    cin >> N;
    
    vector<int> BaseNumbers(N);
    vector<int> SortedNumbers;
    
    for(int i=0; i<N; i++){ cin >> BaseNumbers[i]; }
    
    copy(BaseNumbers.begin(),BaseNumbers.end(),back_inserter(SortedNumbers));
    sort(SortedNumbers.begin(), SortedNumbers.end());
    SortedNumbers.erase(unique(SortedNumbers.begin(),SortedNumbers.end()),SortedNumbers.end());
    
    //cout << SortedNumbers;    cout << BaseNumbers;
    
    auto num_itr = SortedNumbers.begin();
    int num_idx = 0;
    
    for(auto v: BaseNumbers){
        num_itr = lower_bound(SortedNumbers.begin(), SortedNumbers.end(), v);
        num_idx = num_itr - SortedNumbers.begin();
        
        cout << num_idx << endl;
    }
    
}
