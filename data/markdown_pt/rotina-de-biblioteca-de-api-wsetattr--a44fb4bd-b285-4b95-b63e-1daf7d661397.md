# Rotina de biblioteca de API _WSetAttr( )

Altera o atributo para o índice de esquema de cores especificado no esquema de cores da janela indicada para o novo atributo attr.

```foxpro
void _WSetAttr(WHANDLE wh, int color, int attr)
WHANDLE wh;            /* Window handle. */
int color;                     /* Color scheme. */
int attr;                     /* Attribute. */
```

# Exemplo

O exemplo a seguir percorre cada cor de cada esquema, usando _WSetAttr( ) para definir a cor da caneta e, em seguida, exibindo algum texto em cada cor.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WSETATTR
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
      wh = _WOpen(2,10,23,70,WEVENT,scheme,(Scheme FAR *)0,
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
