# Rotina de biblioteca de API _WSize( )

Define novas dimensões da janela especificada para a altura e largura especificadas por h e v no parâmetro pt.

```foxpro
void _WSize(WHANDLE wh, Point pt)
WHANDLE wh;            /* Window handle. */
Point pt;                     /* Position. */
```

# Exemplo

O exemplo a seguir cria uma janela e então expande sua largura e altura.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WSIZE
```

### Código C

```foxpro
#include <pro_ext.h>
FAR WSizeEx(ParamBlk FAR *parm)
{
   WHANDLE wh;
   Point dim;
   wh = _WOpen(2,2,10,10,CLOSE | WEVENT,WINDOW_SCHEME,(Scheme FAR *)0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   dim.v = 8;
//   Grow in width
   for (dim.h = 8; dim.h < 60; dim.h += 4)
   {
      _WSize(wh, dim);
      _Execute("WAIT WINDOW 'Press Any Key To Change Size'");
   }
//   Grow in height
   for (dim.v = 8; dim.v < 20; dim.v += 2)
   {
      _WSize(wh, dim);
      _Execute("WAIT WINDOW 'Press Any Key To Change Size'");
   }
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) WSizeEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
