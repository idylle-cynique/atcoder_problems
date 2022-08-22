/* ABC082 - A
    C++などの静的型付け言語の場合は型変換を行う必要がある
    数値などでの基本的な型変換処理についてはおおむねstatic_cast<Type>()を用いればよい
    四捨五入処理を行うround関数については<cmath>ヘッダにある
*/

#include <iostream>
#include <cmath>
using namespace std;

int main(void){
    int A,B;
    cin >> A >> B;
    
    float af = static_cast<float>(A);
    float bf = static_cast<float>(B);
    float meanAB = (af+bf)/2;
    int answer = round(meanAB);
    cout << answer << endl;
}