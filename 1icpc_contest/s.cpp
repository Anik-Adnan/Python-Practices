#include<iostream>
#include <algorithm>
using namespace std;
int gcd(int a,int b);
int main()
{
    int a,b,m,i,t,j=1,k,c;
    cin>>t;
    while(j<=t)
    {
        c=0;
        cin>>a>>b>>m;
        for(i=0; i<=m; i++)
        {
            k =gcd(a+i,b+i);

            if(k==1)
                c++;
        }
        cout<<"Case "<<j<<": "<<c<<endl;
        j++;
    }
    return 0;
}
int gcd(int a,int b){
    for(int i=1;i<=a&&i<=b;i++){
        if (a%i==0&&b%i==0)
            return i;
    }
}
