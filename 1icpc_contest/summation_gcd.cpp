#include <iostream>
using namespace std;
int gcd(int a,int b);
int main(){
    int n,i,j,sum_of_gcd;
    while(1){
        cin>>n;
        if(n==0) break;
        sum_of_gcd=0;
        for(i=1;i<n;i++){
            for(j=i+1;j<=n;j++) sum_of_gcd+=gcd(i,j);
        }
        cout<<sum_of_gcd<<endl;
    }
    return 0;
}
int gcd(int a,int b){
    if(a==0) return b;
    else return gcd(b%a,a);
}
