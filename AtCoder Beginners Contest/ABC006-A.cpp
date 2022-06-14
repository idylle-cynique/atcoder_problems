/* ABC006 - A
    要求されている通りの実装をすればよい
    ただし、問題の条件が今回のような小さい値でなく、極端に大きな値(10000桁の整数値など)である場合などは
    各桁の和から3の倍数か否かの判定をするなど、何かしらの工夫をする必要がある
*/

#include <iostream>
using namespace std;

int main(void){
    long long int N;
    cin >> N;
    if(N == 3 || N%3 == 0) cout << "YES" << endl;
    else                   cout << "NO" << endl;
}