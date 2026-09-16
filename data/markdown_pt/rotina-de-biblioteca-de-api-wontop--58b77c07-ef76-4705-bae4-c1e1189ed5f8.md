# Rotina de biblioteca de API _WOnTop( )

Retorna o WHANDLE da janela ativa.

```foxpro
WHANDLE _WOnTop(void any)
void any;                     /* Pointer. */
```

# Observações

Normalmente, as teclas pertencem à janela ativa. As rotinas de manipulador precisam agir adequadamente.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir exibe informações de posição sobre a janela ativa.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WONTOP
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
   {"WPOSITION", Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
