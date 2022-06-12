//errada, wrong answer

#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define pb push_back
#define mp make_pair
#define fr(i, a, b) for(i=a; i<b; i++)
#define min(x, y) ((x) < (y) ? (x) : (y))
#define sz(x) ((ll)x.size())
int i=0;
int t, n, m, k, s, d, u, v, length, pedaco, resposta;
struct node{
	int v, d;
	node(int a, int b){
		v=a; d=b;
	}
};
vector<node> adj[100001], rev[100001];
int da[100001], db[100001];
int main(){
	scanf("%d", &t);
	while(t--){
		scanf("%d%d%d%d%d", &n, &m, &k, &s, &d);
		fr(i, 0, n){
		    db[i]=INT_MAX;
			da[i]=INT_MAX;
			rev[i].clear();
			adj[i].clear();
		}
		fr(i, 0, m){
			scanf("%d%d%d", &u, &v, &length);
			u--; v--;
			adj[u].pb(node(v, length));
			rev[v].pb(node(u, length));
		}
		set<pair<int, int> > q;
		s--; d--;
		q.insert(mp(0, s));
		while(!q.empty()){
			u=q.begin()->second;
			pedaco=q.begin()->first;
			q.erase(q.begin());
			fr(i, 0, sz(adj[u])){
				v=adj[u][i].v;
				length=adj[u][i].d;
				if(pedaco+length<da[v]){
					q.erase(mp(da[v], v));
					da[v]=pedaco+length;
					q.insert(mp(da[v], v));
				}
			}
		}
		q.insert(mp(0, d));
		while(!q.empty()){
			u=q.begin()->second;
			pedaco=q.begin()->first;
			q.erase(q.begin());
			fr(i, 0, sz(rev[u])){
				v=rev[u][i].v;
				length=rev[u][i].d;
				if(pedaco+length<db[v]){
					q.erase(mp(db[v], v));
					db[v]=pedaco+length;
					q.insert(mp(db[v], v));
				}
			}
		}
		resposta=db[s];
		fr(i, 0, k){
			scanf("%d%d%d", &u, &v, &length);
			u--; v--;
			if(da[u]!=INT_MAX && db[v]!=INT_MAX){
				resposta=min(da[u]+length+db[v], resposta);
			}
			if(da[v]!=INT_MAX && db[u]!=INT_MAX){
				resposta=min(da[v]+length+db[u], resposta);
			}
		}
		if(resposta==INT_MAX){
			printf("-1\n");
			continue;
		}
		printf("%d\n", resposta);
	}
}