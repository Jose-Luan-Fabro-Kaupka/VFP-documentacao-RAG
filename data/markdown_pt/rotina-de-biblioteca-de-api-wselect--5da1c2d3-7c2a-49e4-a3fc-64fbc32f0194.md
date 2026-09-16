# Rotina de biblioteca de API _WSelect( )

Traz a janela especificada para a posição ativa na tela.

```foxpro
void _WSelect(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Exemplo

O exemplo a seguir cria cinco janelas sobrepostas. As janelas são movidas para a posição ativa usando _WSelect( ), começando pela primeira janela criada.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WSELECT
```

### Código C

```foxpro
#include <pro_ext.h>
FAR WSelectEx(ParamBlk FAR *parm)
{
   WHANDLE wh[5];
   int i;
   for (i = 0; i < 5; i++)
   {
      wh[i] = _WOpen(4 + 2*i,4 + 2*i,12 + 2*i,40 + 2*i,WEVENT | CLOSE,
         WINDOW_SCHEME, (Scheme FAR *) 0, WO_SYSTEMBORDER);
      _WShow(wh[i]);
   }
   for (i = 0; i < 5; i++)
   {
      _Execute("WAIT WINDOW 'Press key to _WSelect() next window'");
      _WSelect(wh[i]);
   }
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) WSelectEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
