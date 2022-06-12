#include<bits/stdc++.h>
long long mod=1000000007;
using namespace std;
#define rep1(i,x,y) for (int i = x;i <= y;i++)

vector<int> parMocha,rankMocha,parDiana,rankDiana;

int encontra(int p,vector<int>& par){
    if(par[p]==p) return p;
    return par[p]=encontra(par[p],par);
}

bool uniao(int p1,int p2,vector<int>& par,vector<int>& rank)
{
    int parMocha=encontra(p1,par),parDiana=encontra(p2,par);
    if(parMocha==parDiana) return 1;
    int u=rank[parMocha],v=rank[parDiana];
    if(u==v) par[parDiana]=parMocha,rank[parMocha]++;
    else if(u>v) par[parDiana]=parMocha;
    else par[parMocha]=parDiana;
    return 0;
}

void facil()
{
    long long n,p,q;
    cin>>n>>p>>q;
    parMocha.resize(n+1);
    rankMocha.resize(n+1,0);
    parDiana.resize(n+1);
    rankDiana.resize(n+1,0);
    rep1(i,0,n) parMocha[i]=i;
    rep1(i,0,n) parDiana[i]=i;
    vector<long long> g1[n+1],g2[n+1];
    rep1(i,0,p-1){
        long long x,y;cin>>x>>y;
        g1[x].push_back(y);
        g1[y].push_back(x);
        uniao(x,y,parMocha,rankMocha);
    }
    rep1(i,0,q-1){
        long long x,y;cin>>x>>y;
        g2[x].push_back(y);
        g2[y].push_back(x);
        uniao(x,y,parDiana,rankDiana);
    }
    long long ans=0;vector<pair<int,int>> v;
    rep1(i,1,n){
        rep1(j,i+1,n){
            int x=i,y=j;
            int p1=encontra(x,parMocha),p2=encontra(y,parMocha);
            if(p1==p2) continue;
            p1=encontra(x,parDiana),p2=encontra(y,parDiana);
            if(p1==p2) continue;
            uniao(x,y,parMocha,rankMocha);
            uniao(x,y,parDiana,rankDiana);
            ans++;v.push_back({x,y});
        }
    }
    cout<<ans<<endl;
    for(auto& x:v) cout<<x.first<<" "<<x.second<<endl;
}

int main()
{
ios_base::sync_with_stdio(false);
cin.tie(0);cout.tie(0);
int t=1;
while(t--)
{
facil();
}
return 0;
}