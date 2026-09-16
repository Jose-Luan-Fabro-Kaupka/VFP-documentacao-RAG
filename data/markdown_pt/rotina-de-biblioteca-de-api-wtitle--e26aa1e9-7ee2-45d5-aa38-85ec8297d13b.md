# Rotina de biblioteca de API _WTitle( )

Coloca o título terminado em nulo da janela wh em title.

```foxpro
void _WTitle(WHANDLE wh, char FAR *title)
WHANDLE wh;            /* Window handle. */
char FAR *title;            /* Window title. */
```

# Exemplo

O exemplo a seguir cria e mostra uma janela com título e rodapé. _WTitle( ) recupera o texto do título, que é então exibido na tela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WTITLE
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   WHANDLE wh;
   char FAR *buffer;
   wh = _WOpen(4,4,20,70,CLOSE | WEVENT,WINDOW_SCHEME,(Scheme FAR *) 0,
      WO_SYSTEMBORDER);
   _WSetTitle(wh, "This is a window title");
   _WShow(wh);
   if ((buffer = _Alloca(128)) == 0)
   {
      _Error(182); // "Insufficient memory"
   }
   _WTitle(wh, buffer);
   _PutStr("\nThe window title is \"");
   _PutStr(buffer);
   _PutChr('"');
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
