# Rotina de biblioteca de API _WPosCursor( )

Posiciona a posição de saída na janela especificada no local especificado em linhas e colunas por pt.

```foxpro
void _WPosCursor(WHANDLE wh, Point pt)
WHANDLE wh;            /* Window handle. */
Point pt;                     /* Location for the output position. */
```

# Observações

_WPosCursor( ) não faz o ponto de inserção aparecer. Normalmente, o ponto de inserção é visível apenas quando o Visual FoxPro está aguardando entrada.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria uma janela e desenha um padrão diagonal de Xs nessa janela. Ele posiciona o cursor antes de escrever cada X usando _WPosCursor( ) e obtém essa mesma posição usando _WGetCursor( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WPOSCUR
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
      _WPutChr(wh, 'X');
      getPos = _WGetCursor(wh);
      _PutStr("\nCursor position:");
      putLong(getPos.v, 5);
      putLong(getPos.h, 5);
      _Execute("WAIT");
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
