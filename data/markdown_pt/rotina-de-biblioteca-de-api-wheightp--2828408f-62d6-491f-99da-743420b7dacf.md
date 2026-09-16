# Rotina de biblioteca de API _WHeightP( )

Retorna a altura em pixels da área de conteúdo da janela especificada.

```foxpro
unsigned int _WHeightP(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Observações

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir exibe a altura e a largura em pixels da janela ativa.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WHEIGHTP
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
   _PutStr("\nheight ="); putLong(_WHeightP(wh), 5);
   _PutStr("\nwidth  ="); putLong(_WWidthP(wh), 5);
}
FoxInfo myFoxInfo[] = {
   {"WDIMEN", Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
