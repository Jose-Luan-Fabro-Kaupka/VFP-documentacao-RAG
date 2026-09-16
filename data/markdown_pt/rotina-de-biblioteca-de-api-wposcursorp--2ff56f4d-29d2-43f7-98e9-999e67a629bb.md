# Rotina de biblioteca de API _WPosCursorP( )

Posiciona a posição de saída da janela especificada no local especificado em pixels por pt.

```foxpro
void _WPosCursorP(WHANDLE wh, Point pt)
WHANDLE wh;            /* Window handle. */
Point pt;                     /* Location for output position. */
```

# Observações

_WPosCursorP( ) não faz o ponto de inserção aparecer. Normalmente, o ponto de inserção é visível somente quando o Visual FoxPro está aguardando entrada.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria uma janela e desenha um padrão diagonal de Xs nessa janela. Ele posiciona o cursor antes de escrever cada X usando _WPosCursorP( ) e obtém essa mesma posição usando _WGetCursorP( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WPOSCURP
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
   wh = _WOpen(4,4,20,70,0,WINDOW_SCHEME,(Scheme FAR *)0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   for (putPos.v = 10; putPos.v < 100; putPos.v += 10)
   {
      putPos.h = putPos.v;
      _WPosCursorP(wh, putPos);
      _WPutChr(wh, 'X');
      getPos = _WGetCursorP(wh);
      _PutStr("\nCursor position:");
      putLong(getPos.v, 5);
      putLong(getPos.h, 5);
      _Execute("WAIT");
   }
   _WClose(wh);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
