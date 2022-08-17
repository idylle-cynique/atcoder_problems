/* ABC258 - A
    問題で要求されている通りに実装すればよい
    数値のゼロ埋め処理については、<iomanip>ヘッダのsetfill, setwによって実装可能
*/

#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
using namespace std;

int main(void){
    int hour, minute;
    hour = 21;
    minute = 0;
    
    int delta;
    cin >> delta;
    
    hour += (delta/60);
    minute += (delta%60);
    
    cout << setw(2) << setfill('0') << hour << ":" << setw(2) << setfill('0') << minute << endl;
}