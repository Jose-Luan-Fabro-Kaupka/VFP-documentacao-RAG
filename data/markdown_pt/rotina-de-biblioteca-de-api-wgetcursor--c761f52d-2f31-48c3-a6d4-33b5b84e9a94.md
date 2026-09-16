# Rotina de biblioteca de API _WGetCursor( )

Retorna a posição de saída atual na janela especificada.

```foxpro
Point _WGetCursor(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Exemplo

O exemplo a seguir cria uma janela e desenha um padrão diagonal de Xs nessa janela. Ele posiciona o cursor antes de escrever cada X usando _WPosCursor( ) e obtém essa mesma posição usando _WGetCursor( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WGETCURS
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
FAR Example(ParamBlk FAR *parm)
{
   WHANDLE wh;
   Point putPos, getPos;
   wh = _WOpen(4,4,20,70,0,WINDOW_SCHEME,(Scheme FAR *) 0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   for (putPos.v = 2; putPos.v < 14; putPos.v++)
   {
      putPos.h = putPos.v;
      _WPosCursor(wh, putPos);
      getPos = _WGetCursor(wh);
      _WPutChr(wh, 'X');
      _PutStr("\nCursor position:");
      putLong(getPos.v, 5);
      putLong(getPos.h, 5);
      _Execute("WAIT WINDOW");
   }
   _WClose(wh);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
