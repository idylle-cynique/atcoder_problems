/* ABC018 - A
    プレイヤーA,B,Cの元の番号、スコア降順に並べた際の順番(順位)を
    map(dict)などを用いて対応付けたあと、それを用いてプレイヤー番号順に順位を出力してやればよい
*/
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <algorithm>
using namespace std;
int main(void){
    int len = 3;
    vector<vector<int>> score(3,{0,0});
    unordered_map<int, int> ranking;
    
    for(int i=0; i<len; i++){
        cin >> score[i][0];
        score[i][1] = i;
    }
    
    sort(score.rbegin(),score.rend());
    
    for(int i=0; i<len; i++){
        //cout << score[i][0] << ":" << score[i][1] << endl;
        ranking[score[i][1]] = i+1;
    }
    
    for(int i=0; i<len; i++){
        cout << ranking[i] << endl;
    }
}
