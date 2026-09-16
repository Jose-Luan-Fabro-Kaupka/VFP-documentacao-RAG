# Rotina de biblioteca de API _WSendBehind( )

Envia a janela especificada para a posição mais ao fundo na tela.

```foxpro
void _WSendBehind(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Exemplo

O exemplo a seguir cria cinco janelas sobrepostas. _WSendBehind( ) envia cada janela para a posição mais ao fundo, começando pela última janela criada.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WSENDBEH
```

### Código C

```foxpro
#include <pro_ext.h>
FAR WSendBehindEx(ParamBlk FAR *parm)
{
   WHANDLE wh[5];
   int i;
   for (i = 0; i < 5; i++)
   {
      wh[i] = _WOpen(4 + 2*i,4 + 2*i,12 + 2*i,40 + 2*i,WEVENT | CLOSE,
         WINDOW_SCHEME, (Scheme FAR *) 0, WO_SYSTEMBORDER);
      _WShow(wh[i]);
   }
   for (i = 4; i >= 0; i--)
   {
      _Execute("WAIT WINDOW 'Press key to _WSendBehind() next window'");
      _WSendBehind(wh[i]);
   }
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) WSendBehindEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
