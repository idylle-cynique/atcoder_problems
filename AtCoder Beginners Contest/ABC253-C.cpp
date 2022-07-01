/* ABC253 - C
    データ構造への理解を求める問題
    具体的には順序付き集合の理解と実装を求める問題

    問題における各クエリの処理を制限処理時間の問題をクリアしながら高速に行うためには
    問題の一連の処理をそれぞれ最大でO(logN)程度で収める必要があるが、これを実現するためには
    順序付き集合や平衡二分探索木を用いる以外に方法はない

    Pythonでは標準ライブラリに順序付き集合が存在しないため、ここでは解答にC++を用いた
*/

#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;
int main(void){
    int Q;
    cin >> Q;
    vector<int> query(3,0);
    multiset<int> orderdset;
    
    for(int i=0; i<Q; i++){
        query = {-1,-1,-1};
        for(int j=0; j<3; j++){
            cin >> query[j];
            
            if(query[0] == 1 && j == 1) break;
            if(query[0] == 3) break;
        }
        //for(int j=0; j<3; j++){if(query[j] != -1) cout << query[j] << " ";} cout << "\n";
        
        if(query[0] == 1){
            // cout << "::" << query[1] << endl;
            orderdset.insert(query[1]);
        }
        if(query[0] == 2){
            for(int k=0; k<query[2]; k++){
                if(orderdset.find(query[1]) == orderdset.end()){
                    break;
                }else{
                    orderdset.erase(orderdset.find(query[1]));
                } 
            } 
        }
        if(query[0] == 3){
            cout << *orderdset.rbegin() -  *orderdset.begin() << endl;
        }   
    }   
}