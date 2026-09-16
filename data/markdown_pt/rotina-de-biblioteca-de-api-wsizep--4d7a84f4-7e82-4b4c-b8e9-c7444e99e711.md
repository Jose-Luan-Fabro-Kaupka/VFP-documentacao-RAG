# Rotina de biblioteca de API _WSizeP( )

Define as novas dimensões da janela para a altura e a largura especificadas em pixels por h e v no parâmetro pt.

```foxpro
void _WSizeP(WHANDLE wh, Point pt)
WHANDLE wh;            /* Window handle. */
Point pt;                     /* Position. */
```

# Observações

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria uma janela e expande sua largura e depois sua altura.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WSIZEP
```

### Código C

```foxpro
#include <pro_ext.h>
FAR WSizeEx(ParamBlk FAR *parm)
{
   WHANDLE wh;
   Point dim;
   wh = _WOpenP(6,6,20,20,CLOSE | WEVENT,WINDOW_SCHEME,(Scheme FAR *)0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   dim.v = 14;
//   Grow in width
   for (dim.h = 14; dim.h < 480; dim.h += 40)
   {
      _WSizeP(wh, dim);
      _Execute("WAIT");
   }
//   Grow in height
   for (dim.v = 14; dim.v < 240; dim.v += 40)
   {
      _WSizeP(wh, dim);
      _Execute("WAIT WINDOW 'Press Any Key To Change Window Size'");
   }
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", WSizeEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
