# Rotina de biblioteca de API _WBottomP( )

Retorna a posição na tela em pixels onde a parte inferior da janela especificada está localizada.

```foxpro
unsigned int _WBottomP(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Observações

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir exibe a posição da janela ativa.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WBOTTOM
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
   _PutStr("\ntop   ="); putLong(_WTopP(wh), 5);
   _PutStr("\nleft ="); putLong(_WLeftP(wh), 5);
   _PutStr("\nbottom ="); putLong(_WBottomP(wh), 5);
   _PutStr("\nright  ="); putLong(_WRightP(wh), 5);
}
FoxInfo myFoxInfo[] = {
   {"WPOSITION", Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
