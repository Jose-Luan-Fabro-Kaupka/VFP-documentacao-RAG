# Rotina de biblioteca de API _WHeight( )

Retorna o número de linhas na área de conteúdo da janela especificada.

```foxpro
unsigned int _WHeight(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Exemplo

O exemplo a seguir mostra a altura e a largura em linhas e colunas da janela ativa.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WHEIGHT
=WDIMEN()
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n, int width)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = width;
   _PutValue(&val);
}
void FAR Example(ParamBlk FAR *parm)
{
   WHANDLE wh = _WOnTop();
   _PutStr("\nheight ="); putLong(_WHeight(wh), 5);
   _PutStr("\nwidth  ="); putLong(_WWidth(wh), 5);
}
FoxInfo myFoxInfo[] = {
   {"WDIMEN", (FPFI) Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
