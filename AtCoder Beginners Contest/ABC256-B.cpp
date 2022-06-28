/*  ABC256 - B
    問題で要求されている処理を実際に実装してみればよい
    元が野球のゲームシステムの再現、というものなので特に計算量等について
    考慮する必要はない
*/

#include <iostream>
#include <vector>
using namespace std;
template<typename Type_>
std::ostream& operator<<(ostream& os, vector<Type_>& coutvec){
    cout << "{";
    for(auto element: coutvec){
        os << element << ", ";
    }
    cout << "}";
    return os;
}

int main(void){
    long long int N;
    cin >> N;
    
    vector<int> array(N);
    for(int i=0; i<N; i++){ cin >> array[i]; }
    
    vector<int> field(4);
    int P = 0;
    
    for(int v: array){
        for(int i=field.size(); i>=0; i--){
            if(field[i]){
                if(i+v < field.size()){
                    field[i+v] = field[i];
                    field[i] = 0;
                }
                else{
                    field[i] = 0;
                    P += 1;
                }
            }
        }
        if(v < field.size()){ field[v] = 1; }
        else                { P += 1; } 
        //cout << v << endl << field << " score: " << P << endl;
    }
    cout << P << endl;
}