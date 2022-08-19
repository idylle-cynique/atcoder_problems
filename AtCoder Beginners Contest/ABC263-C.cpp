/* ABC263 - C
    問題で求められているのは結局のところ以下の通り
        「1以上M以下の整数の集合からN個取り出して昇順に並べることで得られる配列を全列挙せよ」
    つまり1以上M以下の整数のリスト(vector)を作成して組み合わせを列挙し、それを順番に出力するだけでよい

    本番ではPythonと標準モジュールitertoolsのcombinations関数を用いて実装したが、
    これでは少々出題意図(再帰を用いた実装を行え)に沿わないので、
    combinations関数をC++で自作し、これを用いることで再度問題を解き直した

    組み合わせ数はM_C_N(M個の整数からN個選ぶときの組み合わせ)で、
    N,Mはそれぞれ最大で10なので高々10_C_5 = 126通りにしかならない
    C++では10ms前後程度できわめて高速に解くことができる
*/

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <experimental/iterator>
#include <iterator>
using namespace std;

template<typename Type_>
std::ostream& operator<<(ostream& os, vector<Type_>& coutvec){
    cout << "{";
    for(auto itr = coutvec.begin(); itr != coutvec.end(); itr++){
        if(itr != coutvec.end()-1)    os << *itr << ", ";
        else                          os << *itr;           // 最後の列にはカンマは要らないので付けずにcout
    }
    cout << "}";
    return os;
}

vector<vector<int>> combinations(vector<int> arg_vec, int r=0){
    vector<vector<int>> ret_vec;
    vector<vector<int>> rest;
    vector<int> tmp_vec;
    vector<int> slice;
    int element = 0;
    if (r == 0) r = arg_vec.size();
    //cout << arg_vec << "から" << r << "個取ったときの組み合わせ" << endl;
    if (r == 1){
            for(int ele: arg_vec) ret_vec.push_back({ele});
    }
    else{
        ret_vec = {};
        for(int i=0; i<arg_vec.size(); i++){
            element = arg_vec[i];
            slice = {};
            slice.insert(slice.end(),arg_vec.begin()+i+1,arg_vec.end());
            //cout << slice << endl;
            rest = combinations(slice,r-1);
            for(vector<int> ele_vec: rest){
                tmp_vec = {element};
                tmp_vec.insert(tmp_vec.end(),ele_vec.begin(),ele_vec.end());
                ret_vec.push_back(tmp_vec);
            }
        }
    }
    return ret_vec;
}

int main(void){
    int N,M;
    cin >> N >> M;
    vector<int> numbers(M,0);
    
    for(int n=1; n<=M; n++) numbers[n-1] = n;
    //cout << numbers << endl;
    
    vector<vector<int>> combies = combinations(numbers,N);
    
    for(vector<int> line: combies){
        std::copy(line.begin(), line.end(), 
                  std::experimental::make_ostream_joiner(cout," "));
        cout << endl;
    }
}
