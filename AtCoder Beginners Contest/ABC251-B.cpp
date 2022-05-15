/* ABC251 - B
    基本的には問題通りにシミュレートを行うものだが、制約が際どい値をとっていたため
    Pythonで提出した際にTLEとなってしまった

    本番中でのACを確保するためにC++によるコードを取り急ぎ提出した
    これもかなり処理効率は悪い書き方ではあるものの、数百ms程度で処理を終える事ができる
    どうやらC++のpush_backも含め、事前に取り扱うデータの長さを定めずに都度配列を拡張する
    書き方は全般的に処理効率の面で難がある模様

    以後こうした全探索ベースの問題ではvectorの長さを変数の宣言段階で決めてしまうのが望ましい
*/
#include <iostream>
#include <vector> 
#include <map>
#include <set>
using namespace std;
int main(void){
    int N,W;
    cin >> N >> W;
    
    vector<int> weigths;
    set<int> goodnumbers;
    int tmp_num;
    int sum_two,sum_three;
    for(int i=0; i<N; i++){
        cin >> tmp_num;
        // cout << tmp_num << " ";
        weigths.push_back(tmp_num);
    }
    for(int i=0; i<N; i++){ // 1つ選ぶことで作ることのできる「良い整数」
        if(weigths[i] <= W){
            goodnumbers.insert(weigths[i]);
        }
    }
    for(int i=0; i<N; i++){ // 2つ選ぶことで作ることのできる「良い整数」
        for(int j=i+1; j<N; j++){
            sum_two = weigths[i] + weigths[j];
            if(sum_two <= W){
               goodnumbers.insert(sum_two); 
            }
        }
    }
    for(int i=0; i<N; i++){ // 3つ選ぶことで作ることのできる「良い整数」
        for(int j=i+1; j<N; j++){
            for(int k=j+1; k<N; k++){
                sum_three = weigths[i]+weigths[j]+weigths[k];
                if(sum_three <= W){
                    goodnumbers.insert(sum_three);
                }
            }
        }
    }
    cout << goodnumbers.size() << endl;
}
