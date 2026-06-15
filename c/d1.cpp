#include <iostream>
using namespace std;
 
int main(){
    int i, j; char k='A';

    for(i=1; i<=5; i++){
        for(j=0; j<i; j++){
            cout << char(k + j);
        }
        cout << "\n";
    }

    return 0;
}