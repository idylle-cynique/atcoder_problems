/* ABC006 - B
    フィボナッチ数列を求める処理に似た処理を実装させる問題
    実装に当たっては次のような点に留意する必要がある
        i)  N番目のトリボナッチ数は非常に大きな値を取る場合があり、
            そのまま具体的な値を求めようとすると最も大きな値を格納できるデータ型を用いても
            桁あふれを起こし正しく計算出来なかったり、計算が複雑で処理が間に合わない場合がある
        ii) トリボナッチ数を求める際に、再帰関数を用いて
            n-1番目～n-3番目のトリボナッチ数を求めることでn番目のトリボナッチ数を求める……
            といったような実装をする場合、メモ化再帰などを用いて同じ番目のトリボナッチ数を求める処理を
            省略するなどの工夫をしなければ再帰回数が指数関数的に増え、
            天文学的な計算時間になってしまう場合がある

    上記二点の具体的な解決策としては、各トリボナッチ数を直接記録するのではなく、
    トリボナッチ数の10007の剰余値を計算し、この剰余値だけを用いて計算する方法があり、
    これによってデータ型や占有メモリ量を気にすることなく正答を得ることができる
*/

#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<long long int> triboNumbers(10000000,-1);
long long int MOD = 10007;
long long int tribonacci(int n){    
    if(triboNumbers[n] == -1){
        // cout << n << ", " << triboNumbers[n] << " : " << triboNumbers[n-1] << " + " << triboNumbers[n-2] << " + " << triboNumbers[n-3] << endl;
        triboNumbers[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);
    }
    
    // cout << "tribonacci[" << n << "]" << " = " << triboNumbers[n] << endl;
    return triboNumbers[n]%MOD;
}

int main(void){
    long long int N;
    cin >> N;
    triboNumbers[0] = 0; triboNumbers[1] = 0; triboNumbers[2] = 0; triboNumbers[3] = 1;
    
    long long int answer = tribonacci(N);
    cout << answer << endl;
}
