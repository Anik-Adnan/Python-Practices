#include <iostream>
using namespace std;
int main(){
    int n,t,T=1,a[1000],i,j,temp;
    cin>>t;
    while(T<=t){
        cin>>n;
        for(i=0;i<n;i++)
            cin>>a[i];
        int count=0,sum=0;
        for(i=0;i<n;i++){
            for( j=i+1;j<n;j++){
                if(a[i]>a[j]){
                    temp=a[j];
                    a[j]=a[i];
                    a[i]=temp;
                    count++;
                }
            }
        }
        for(i=0;i<n;i++){
            if(a[i]>0) sum+=a[i];
        }
        cout<<"Case "<<T<<": "<<sum<<" "<<count<<endl;
        T++;
    }
    return 0;
}

