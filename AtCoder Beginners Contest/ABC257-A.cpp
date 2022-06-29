/* ABC257 - A
    本番ではシミュレーションによって正答を得たが、
    生成される文字列は規則的な形なので、除算処理によって一発計算で解を求めることができる
    当然こちらの方が処理が早いのでこちらの方法を取るのが理想的
*/

#include <iostream>
#include <string>
using namespace std;

int main(void){
    int N,X;
    cin >> N >> X;
    
    string alphs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char answer = alphs[(X-1)/N];
    cout << answer << endl;
}