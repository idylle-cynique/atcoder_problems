/* ABC213 - C
    二次元配列の座標圧縮処理の実装を求める問題
    行・列の座標圧縮は、行ごと・列ごとで独立なので、
    行の圧縮処理が列の圧縮結果を変動させたり、その逆が起こることはない
    つまり、行と列をそれぞれ座標圧縮して、その結果を元の番目に従って組(座標)を
    作り、それを出力するだけで正答が得られる

    ただし、二次元配列なので次のように、x座標、y座標の値が重複する場合がある
        ex.) カードをc、何も置いていない場所を*とすると
            c*c
            cc*
            c**
        のようなとき、 列番号(x座標)が1であるものが3つ存在するので
        列番号を受け取って配列を作ると{1,1,1,2,3}となり、重複値が発生し、列番号の順序を
        正しく得られなくなってしまう
    したがって、事前に確かに重複値を取り除いたうえで圧縮処理を行う必要がある
    C++の場合はunique関数とerase関数を用いることで、Pythonの場合は一時的にリストをsetに格納し、
    再度リストに格納しなおすことで重複値を取り除くことができる
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <unordered_map>
using namespace std;
template<typename Type_> 
std::ostream& operator<<(ostream& os, vector<Type_>& coutvec){
    cout << "{"; for(auto element: coutvec){ os << element << ", ";} cout << "}";
    return os;
}
int main(void){
    int H,W,N;
    cin >> H >> W >> N;
    
    vector<int> verticals(N), horizontals(N);
    for(int i=0; i<N; i++){
        cin >> verticals[i] >> horizontals[i];
    }
    
    vector<int> sortvert = verticals;
    vector<int> sorthori = horizontals;
    
    sort(sortvert.begin(),sortvert.end());
    sortvert.erase(unique(sortvert.begin(),sortvert.end()),sortvert.end());
    sort(sorthori.begin(),sorthori.end());
    sorthori.erase(unique(sorthori.begin(),sorthori.end()),sorthori.end());
    
    unordered_map<int,int> vertpos(N);
    unordered_map<int,int> horipos(N);
    auto num_itr = sortvert.begin();
    int num_pos = 0;

    for(int i=0; i<N; i++){
        num_itr = lower_bound(sortvert.begin(),sortvert.end(),verticals[i]);
        num_pos = num_itr - sortvert.begin();
        //cout << verticals[i] << ": " << num_pos << endl;
        vertpos[verticals[i]] = num_pos+1;
    }
    
    for(int i=0; i<N; i++){
        num_itr = lower_bound(sorthori.begin(),sorthori.end(),horizontals[i]);
        num_pos = num_itr - sorthori.begin();
        //cout << horizontals[i] << ": " << num_pos << endl;
        horipos[horizontals[i]] = num_pos+1;
    }
    
    for(int i=0; i<N; i++){
        cout << vertpos[verticals[i]] << " " << horipos[horizontals[i]] << "\n";
    }
}
