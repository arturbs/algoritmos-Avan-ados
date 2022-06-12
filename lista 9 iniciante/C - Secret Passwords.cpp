// nao consegui sair do problema de tempo do teste 4 em python, tentando em c++
#include<bits/stdc++.h>
using namespace std;
#define sc(a) scanf("%lld",&a)
#define pf(a) printf("%lld\n",a)
#define size1 200050
#define mem(name, value) memset(name, value, sizeof(name))
#define pb push_back

typedef long long ll;
typedef vector <ll> vll;
typedef set <ll> sll;
typedef queue <ll> qll;
typedef map <ll, ll> mll;
typedef pair <ll, ll> pll;
typedef vector <pair <ll , ll> > vpll;
vector <ll> grafo[size1];
bool caracterUsado[size1];
void dfs(ll u)
{
    caracterUsado[u] = true;
    for (ll v : grafo[u]) {
        if(!caracterUsado[v]) dfs(v);
    }
}
int main() {
    ll n, m, tc, num, t = 1;
    sc(num);
    string str;
    for (ll i = 0; i < num; ++i) {
        cin >> str;
        for (ll j = 0; j < str.length(); ++j) {
            grafo[str[j] - 'a'].pb(26 + i);
            grafo[26 + i].pb(str[j] - 'a');
        }
    }
    ll resposta = 0;
    for (ll i = 0; i < num; ++i) {
        if(!caracterUsado[26 + i]){
            resposta++;
            dfs(26 + i);
        }
    }
    pf(resposta);
}