/* ABC264 - A
　  タイトルにある通り、C++の場合substrメソッド(メンバ関数)を用いることで
    問題で求められている処理を実装することができる
*/

#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>
using namespace std;
int main(void){
    string atcoder = "atcoder";
    int l,r;
    
    cin >> l >> r;
    l -= 1;
    //cout << l << "," << r << endl;
    
    cout << atcoder.substr(l,r-l) << endl;
}
