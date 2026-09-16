# Rotina de biblioteca de API _WLeftP( )

Retorna a posição na tela em pixels onde a borda esquerda da janela está localizada.

```foxpro
unsigned int _WLeftP(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Observações

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir mostra a posição em pixels da janela ativa.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WLEFTP
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
