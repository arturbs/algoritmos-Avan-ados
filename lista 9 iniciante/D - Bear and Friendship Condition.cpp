//nao consegui sair do problema de tempo do teste 11 em python, tentando em c++
#include <bits/stdc++.h>
using namespace std;
#define LL long long
#define rep1(i,x,y) for (int i = x;i <= y;i++)
#define rei(x) scanf("%d",&x)

typedef pair<int, int> pii;
typedef pair<LL, LL> pll;
const int N = 15e4+100;
int n, m;
int arestas[N];
LL contador[N];
LL resposta = 0;
bool visita[N];
int encontra(int x)
{
    if (arestas[x] != x)
        return arestas[x] = encontra(arestas[x]);
    else
        return x;
}
void in()
{
    rei(n), rei(m);
    rep1(i, 1, n)
        arestas[i] = i, contador[i] = 1;
    int x, y;
    rep1(i, 1, m)
    {
        rei(x), rei(y);
        int r1 = encontra(x), r2 = encontra(y);
        if (r1 != r2)
        {
            arestas[r1] = r2;
            contador[r2] += contador[r1];
        }
    }
}
bool ga()
{
    rep1(i, 1, n)
    {
        int t = encontra(i);
        if (visita[t]) continue;
        visita[t] = true;
        resposta += 1LL*contador[t]*(contador[t]-1)/2;
        if (resposta > m)
        {
            return false;
        }
    }
    if (resposta != m)
        return false;
    else
        return true;
}
void saida()
{
    if (ga())
        puts("YES");
    else
        puts("NO");
}
int main()
{
    in();
    saida();
    return 0;
}