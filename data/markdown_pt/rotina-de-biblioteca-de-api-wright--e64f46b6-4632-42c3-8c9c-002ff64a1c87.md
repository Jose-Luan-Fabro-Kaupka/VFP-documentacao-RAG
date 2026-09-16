# Rotina de biblioteca de API _WRight( )

Retorna a coluna na tela onde a borda direita da janela especificada está localizada.

```foxpro
unsigned int _WRight(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Exemplo

O exemplo a seguir mostra a posição da janela ativa.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WRIGHT
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
