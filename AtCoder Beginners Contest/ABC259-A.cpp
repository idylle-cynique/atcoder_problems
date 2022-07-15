/*　ABC259 - A
    問題文の通りに条件づけを行えばよい
    else時の値の算出については、そのまま愚直にループ処理を用いても十分高速に機能するが
    やはり式で一発計算するのが望ましい
*/
#include <iostream>
using namespace std;
int main(void){
    int N,M,X,T,D;
    cin >> N >> M >> X >> T >> D;
    
    if(X <= M && M < N){ // X-N歳の間なら T cmのまま
        cout << T << endl;
    }else{
        cout << T - (X-M)*D << endl;
    }
}
