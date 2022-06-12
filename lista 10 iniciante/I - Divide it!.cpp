//não consegui fazer em python, não passava por tempo no teste 3

/*
em python 

from collections import deque
casos = int(input())
for x in range(casos):
    numero = int(input())
    pre = {}
    pre[1] = 1
    fila = deque([1])
    while fila:
        if numero in pre:
            break
        v = float(fila.pop())
        if(2*v not in pre and 2*v <= numero and (2*v).is_integer()):
            num = int(2*v)
            fila.append(num)
            pre[num] = v
        if((3*v)/2 not in pre and (3*v)/2 <= numero and ((3*v)/2).is_integer()):
            num = int((3*v)/2)
            fila.append(num)
            pre[num] = v
        if((5*v)/4 not in pre and (5*v)/4 <= numero and ((5*v)/4).is_integer()):
            num = int((5*v)/4)
            fila.append(num)
            pre[num] = v
    cont = 0
    if numero not in pre:
        print(-1)
    else:
        x = numero
        while x != 1:
            x = pre[x]
            cont += 1
        print (cont)

*/

#include <bits/stdc++.h>
using namespace std;
#define LL long long
#define rei(x) scanf("%d",&x)

int main() {
    int casos;
    rei(casos);
    for(int i = 0; i < casos; i++) {
        LL numero;
        cin >> numero;
        int cn2 = 0, cn3 = 0, cn5 = 0;
        while(numero % 2 == 0) {
            numero/=2;
            cn2++;
        }
        while(numero % 3 == 0) {
            numero/=3;
            cn3++;
        }
        while(numero % 5 == 0) {
            numero/=5;
            cn5++;
        }
        if(numero != 1) {
            puts("-1");
        }
        else {
            int saida;
            saida = cn2 + cn5 * 3 + cn3 * 2;
            cout << saida << endl;
        }
    }
    return 0;
}