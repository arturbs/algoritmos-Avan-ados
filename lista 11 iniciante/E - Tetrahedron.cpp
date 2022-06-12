#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007

int dp[4];
int aux[4];
int ciclo;


int main() {
    cin >> ciclo;
    dp[0] = 1;
    dp[2] = 0;
    dp[3] = 0;
    dp[1] = 0;
    
    for (int i = ciclo - 1; i >= 0; i--) {
        for (int j = 0; j < 4; j++) {
            aux[j] = 0;
            for (int l = 0; l < 4; l++) {
                if (j!=l) {
                    aux[j] = (1LL*aux[j] + dp[l]) % MOD;
                }
            }
        }
        
        for (int p = 0; p < 4; p++) {
            dp[p] = aux[p];
        }
    }
    cout<< dp[0]<< endl;
}