/*  ABC255 - A
    問題文通りの処理を実装すればよい
*/

#include <iostream>
#include <vector>
using namespace std;
int main(void){
    int R,C;
    cin >> R >> C;
    
    vector<vector<int>> A(2,{0,0});
    
    for(int i=0; i<A.size(); i++){
        for(int j=0; j<A[i].size(); j++){
            cin >> A[i][j];
        }
    }
    
    cout << A[R-1][C-1] << endl;
}
