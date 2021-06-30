#include<bits/stdc++.h>

using namespace std;

vector<int> t;
const int INF = (int)1e9;
int x;

void build(vector<int>&a){

    int n = a.size();
    int x = 1;
    while(x<n)
        x *=2;
    t.assign(2*x-1,INF);
    for(int i=0;i<n;i++){
        t[i*x+1]=a[i];
    }
    for(int v=x-2;v>=0;v--){
        t[v]=min(t[2*v+1],t[2*v+2]);
    }
}


void update(int i, int new_value){
    t[i+x-1] = new_value;
    int v=i+x-1;
    while(v!=0){
        v = (v-1)/2;
        t[v] = min(t[2*v+1],t[2*v+2]);
    }

}

int rmq(int v, int l, int r, int a, int b){
    if(l>b || r<a)
        return INF
    
}

int main(){
    int n;
    cin>>n;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    build(a);
    for(int i=0;t.size();i++)
        cout<<t[i]<<' ';
    cout<<endl;

    update(2,-1);
    for(int i=0;i<(int) t.size();i++)
        cout<<t[i]<<' ';
    cout<<endl;
    cout<<rmq(0,0,x-1,3,4)<<endl;

}