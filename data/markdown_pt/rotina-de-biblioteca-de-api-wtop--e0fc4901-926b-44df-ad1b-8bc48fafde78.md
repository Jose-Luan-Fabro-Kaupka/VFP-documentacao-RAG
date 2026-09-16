# Rotina de biblioteca de API _WTop( )

Retorna a linha na tela onde o topo da janela está localizado.

```foxpro
unsigned int _WTop(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Exemplo

O exemplo a seguir exibe a posição da linha da janela ativa.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WTOP
=WPOSITION()
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
   _PutStr("\ntop   ="); putLong(_WTop(wh), 5);
   _PutStr("\nleft ="); putLong(_WLeft(wh), 5);
   _PutStr("\nbottom ="); putLong(_WBottom(wh), 5);
   _PutStr("\nright  ="); putLong(_WRight(wh), 5);
}
FoxInfo myFoxInfo[] = {
   {"WPOSITION", (FPFI) Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
