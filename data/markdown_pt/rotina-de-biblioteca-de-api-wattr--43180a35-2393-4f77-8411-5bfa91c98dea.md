# Rotina de biblioteca de API _WAttr( )

Retorna o byte de atributo para o índice de cor especificado no esquema de cores da janela especificada.

```foxpro
int _WAttr(WHANDLE wh, int color)
WHANDLE wh;            /* Window handle. */
int color;                     /* Color index. */
```

# Exemplo

O exemplo a seguir percorre cada cor de cada esquema de cores, mostrando seu byte de atributo conforme retornado por _WAttr( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WATTR
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
FAR WAttrEx(ParamBlk FAR *parm)
{
   int scheme;
   int color;
   WHANDLE wh;
   int attrib, savePen;
   for (scheme = 0; scheme <= 25; scheme++)
   {
      wh = _WOpen(2, 10, 23, 70, WEVENT, scheme, (Scheme FAR *) 0,
         WO_SYSTEMBORDER);
      for (color = WA_NORMAL; color <= WA_ISSHADOW; color++)
      {
         attrib  = _WAttr(wh, color);
         savePen = _WAttr(_WGetPort(), WA_PENCOLOR);
         _WSetAttr(_WGetPort(), WA_PENCOLOR, attrib);
         _PutStr("\nScheme:"); putLong(scheme, 5);
         _PutStr("; Color:"); putLong(color, 5);
         _PutStr("; Attribute byte:"); putLong(attrib, 5);
         _WSetAttr(_WGetPort(), WA_PENCOLOR, savePen);
      }
      _WClose(wh);
      _Execute("WAIT");
   }
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) WAttrEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
