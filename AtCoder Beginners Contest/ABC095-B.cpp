/* ABC095 - B
    条件を満たしつつもっとも多くのドーナツを作る方法は次の方法しかない
        全ての種類のドーナツを1つずつ作った後、残りの材料を使って、最も必要材料量が少ないドーナツを作れるだけ作る
    あとはこれをそのまま実装すればよい
*/

#include <iostream>
#include <vector>
using namespace std;

int main(void){
    int N,X;
    cin >> N >> X;

    vector<int> material(N);
    for(int i=0; i<N; i++) cin >> material[i];
    
    int answer = 0;
    int rest = X;
    int min_donut = 100000000;
    
    for(int m: material){
        answer += 1;
        rest -= m;
        min_donut = min(m, min_donut);
    }
    //cout << min_donut << ", " << rest << endl;
    answer += (rest/min_donut);
    cout << answer << endl; 
}