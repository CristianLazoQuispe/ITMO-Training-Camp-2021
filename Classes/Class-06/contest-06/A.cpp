#include <bits/stdc++.h>

int a[1000002];
using namespace std;


int solve(int i, int j){

    if (i==j){
        return a[i];
    }
    int suma1 = solve(i,i+(j-i)/2);
    int suma2 = solve(i+(j-i)/2+1,j);
    return suma1+suma2;
}

int main(){

    int n,aux;
    string kind;
    int i,j;
    cin>>n;

    for(int i=0;i<n;i++){
        cin>>aux;
        a[i]=aux;
    }
    
    while(cin){
        cin>>kind>>i>>j;
        cout<<kind<<i<<j<<endl;
        const char* s = kind.c_str();
        if (strcmp(s,"set")){
            a[i-1] = j;
        }   
        else{
            cout<<solve(i-1,j-1)<<endl;
        }
    }


}