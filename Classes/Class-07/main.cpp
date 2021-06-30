// problem d
#include<bits/stdc++.h>

using namespace std;

vector<int> calc_depths(vector<int> &p){
    vector<int> d(p.size());
    d[0] = 0;

    for(int i = 1; i<(int)p.size();i++)
        d[i] = d[p[i]]+1;
    return d;
}
int logn;
vector<vector<int>> precalc(vector<int> &p){
    int n = p.size();
    logn =1 ;
    while((1<<logn)<=n){
        logn++;
    }
    vector<vector<int>> jmp(n,vector<int>(logn+1));

    for(int i=0; i<n;i++){
        jmp[i][0] = p[i];
    }
    jmp[0][0]=0;

    for(int k=1; k< logn;k++)
        for(int i=0;i<n;i++)
            jmp[i][k] = jmp[jmp[i][k-1]][k-1];

    return jmp

}

int lca(int u, int v, vector<vector<int>>& jmp, vector<int>& d){
    if(d[u]<d[v])
        swap(u,v);
    int delta = d[u]-d[v];
    for(int k = logn; k>= 0;k--){
        if (delta >= (1<<k)){
            u = jmp[u][k];
            delta -= (1<<k);
        }
    }
    if(u==v){
        return u;
    }
    for(int k = logn -1 ; k>= 0;k--){
        int u_ = jmp[u][k];
        int v_ = jmp[v][k];
        if(u_ != v_){
            u = u_;
            v = v_;
        }
    }

    return jmp[u][0];

}

int main(){
    int n;
    cin>>n;
    vector<int> p(n);
    p[0] = -1;

    for(int i=1; i<=n;i++){
        cin>>p[i];
        p[i]--;
    }
    vector <int> d = calc_depths(p);
    /*
    for(int i; i< (int)d.size();i++)
        cout<<d[i]<<' ';
    cout<<endl;
    return 0;*/
    vector<vector<int>> jmp = precalc(p);
    /*for (int i=0;i<n;i++){
        for(int k =0;k<logn;k++)
            cout<<jmp[i][k]<<' ';
        cout<<endl;
    }
    */
    int m;
    cin>>m;
    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;
        u--,v--;
        cout<<lca(u,v,jmp,d)+1<<endl;
    }
    return 0;
}