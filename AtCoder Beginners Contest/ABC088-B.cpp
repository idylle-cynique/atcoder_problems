/* ABC088 - B
    カードに関する情報は二人のプレイヤーから完全に見えている状態なので、
    (当然ながら)今場に残っているカードのうち数字が最も大きいものをとって行くのが最適
    カードの数値情報をvectorに格納したうえで降順にソートし、
    交互にAliceとBobにスコアを割振り、最後にその差を出力してやればよい
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(void){
    int N;
    cin >> N;
    vector<int> card(N,0);
    int alice = 0;
    int bob = 0;
    
    for(int i=0; i<N; i++) cin >> card[i];
    sort(card.begin(), card.end(), greater<int>());
    
    for(int i=0; i<N; i++){
        //cout << i << ":" << card[i] << endl;
        if(i%2) bob += card[i];
        else    alice += card[i];
    }
    int answer = alice-bob;
    
    //cout << alice << " : " << bob << endl;
    cout << answer << endl;
}
