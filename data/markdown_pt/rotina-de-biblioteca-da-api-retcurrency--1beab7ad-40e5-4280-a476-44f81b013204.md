# Rotina de biblioteca da API _RetCurrency( )

Define o valor de retorno da biblioteca como um valor monetário.

```foxpro
void _RetCurrency(CCY money, int width)
CCY money;         /* CCY - LARGE_INTEGER. */
int width;         /* Number of columns to display. */
```

# Observações

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir converte um valor do tipo numérico em um valor do tipo monetário.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO RETCURR
? xntom(100.1)
```

### Código C

```foxpro
#include <pro_ext.h>
#include <math.h>
void FAR retcurr(ParamBlk FAR *parm)
{
   CCY money;
   money.HighPart = (long) (parm->p[0].val.ev_real*10000 / pow(2,32));

   money.LowPart = (unsigned long) ((parm->p[0].val.ev_real - (double) (money.HighPart * pow(2,32)/10000.0)) *10000);

   _RetCurrency(money,25);
}
FoxInfo myFoxInfo[] = {
   {"XNTOM", (FPFI) retcurr, 1, "N"}
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
