#include<bits/stdc++.h>
#define pb push_back
using namespace std;
const int mx=401;
typedef pair<int,int>pii;
vector<pii>trem[mx];
vector<pii>onibus[mx];
set<pii>s;
int dist_trem[mx];
int dist_onibus[mx];
bool visitado[mx];
int saida;

void djkstra(vector<pii>adj[],int *dist) {
    priority_queue<pii,vector<pii>,greater<pii> >pq;
    pq.push(make_pair(0,1));
    dist[1]=0;
    while(!pq.empty()) {
        int u=pq.top().second;
        pq.pop();
        if(visitado[u]) continue;
        visitado[u]=true;
        for(int i=0;i<adj[u].size();i++) {
            int v=adj[u][i].first;
            int weight=adj[u][i].second;
            if(dist[v]>dist[u]+weight) {
                dist[v]=dist[u]+weight;
                pq.push(make_pair(dist[v],v));
            }
        }
    }
}
int main() {
    int n,m,a,b,c;
    cin>>n>>m;
    c = 0;
    while(c < m) {
        c++;
        cin>>a>>b;
        trem[a].pb(make_pair(b,1));
        trem[b].pb(make_pair(a,1));
        s.insert(make_pair(min(a,b),max(a,b)));
    }
    for(int i=1;i<=n;i++) {
        dist_trem[i]=INT_MAX;
        dist_onibus[i]=INT_MAX;
        visitado[i]=false;
    }
    djkstra(trem,dist_trem);
    for(int i=1;i<=n;i++) {
        visitado[i]=false;
    }
    for(int i=1;i<=n;i++) {
        for(int j=i+1;j<=n;j++) {
            pii p;
            p.first=i;
            p.second=j;
            if(!s.count(p)) {
                onibus[i].pb(make_pair(j,1));
                onibus[j].pb(make_pair(i,1));
            }
        }
    }
    djkstra(onibus,dist_onibus);
    if(dist_onibus[n]==INT_MAX||dist_trem[n]==INT_MAX) {
        saida = -1;
    }
    else {
        saida = max(dist_onibus[n],dist_trem[n]);
    }
    printf ("%d", saida);
}