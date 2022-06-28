/* ABC256 - A
    C++の場合、pow関数を利用するにはcmathヘッダをインクルードする必要がある
    また、リファレンスを確認すると分かるがcmathにおけるpowは
    oubleないしfloat型で値を返し、桁数が多い場合には浮動小数点数表記でcoutされる
    参考) https://cpprefjp.github.io/reference/cmath/pow.html

    したがって、出力する際にはintへの型変換を用いるか、int型の変数に戻り値を格納
    するなどの工夫をすることで出力表記違いによるWAを回避する必要がある

    また、この他、2のN乗化処理はそのまま2進数のシフト演算に当てはまることを利用して
    シフト演算処理によって解を求める方法もある
*/

#include <iostream>
#include <cmath>    // pow関数を利用するために必要
using namespace std;

int main(void){
    int N;
    cin >> N;
    int answer = pow(2,N);
    cout << answer << endl;
}