/* ABC047 - A
    もっともたくさんキャンディが入っているパックと、
    それ以外の2つのキャンディのパックに入っているキャンディの個数の和が等しいかどうか調べればよい
    
    そのまま個別の変数a,b,cという形で調べると処理がややこしくなるので、
    ここでは区別せずvectorに格納して取り扱っている
*/

#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>
using namespace std;
int main(void){
    int n = 3;
    vector<int> candy(3,0);
    
    for(int i = 0; i<n; i++) cin >> candy[i];
    sort(candy.rbegin(), candy.rend());
    //for(auto ele: candy) cout << ele << endl;
    
    string answer = (candy[0] == candy[1]+candy[2])? "Yes" : "No";
    cout << answer << endl;
}