# Rotina de biblioteca de API _WGetCursorP( )

Retorna em pixels a posição de saída atual na janela especificada.

```foxpro
Point _WGetCursorP(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Observações

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria uma janela e desenha um padrão diagonal de Xs nesta janela. Ele posiciona o cursor antes de escrever cada X usando _WPosCursorP( ) e obtém essa mesma posição usando _WGetCursorP( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WGETCURP
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
