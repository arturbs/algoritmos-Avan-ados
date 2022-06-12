#include<bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define ll                  long long
#define fr(i,n)             for (ll i=0;i<n;i++)
#define pb                  push_back

string s[55];
vector<pair<ll,ll>>caminho;
ll mapa[55][55];
void dfs(ll x1, ll y1, ll n)
{
    if(x1>=n or y1>=n)return ;
    if(x1<0 or y1<0)return ;

    if(mapa[x1][y1]==1)return ;
    mapa[x1][y1]=1;
    caminho.pb(make_pair(x1,y1));
    dfs(x1+1, y1,n );
    dfs(x1-1, y1, n);
    dfs(x1, y1+1, n);
    dfs(x1, y1-1, n);
}
int main()
{
    ll i,r,n;
    ll x1, x2, y1, y2;
    scanf("%lld", &n);
    cin>>x1>>y1>>x2>>y2;
    x1--, y1--, x2--, y2--;
    fr(i,n)cin>>s[i];
    fr(i,n) fr(j,n)mapa[i][j]=s[i][j]-'0';
    caminho.clear();
    dfs(x1, y1, n);
    vector<pair<ll,ll>> inicio=caminho;
    caminho.clear();
    dfs(x2, y2, n);
    vector<pair<ll,ll>> fim=caminho;
    ll custo=0, resposta=1e18;
    fr(i, inicio.size())
    {
        fr(j, fim.size())
        {
            custo=(inicio[i].first - fim[j].first )*(inicio[i].first - fim[j].first );
            custo+=(inicio[i].second - fim[j].second )*(inicio[i].second - fim[j].second );
            resposta=min(resposta, custo);
        }
    }
    if(inicio.size()==0 or fim.size()==0)resposta=0;
    printf("%lld\n",resposta);
return 0;
}