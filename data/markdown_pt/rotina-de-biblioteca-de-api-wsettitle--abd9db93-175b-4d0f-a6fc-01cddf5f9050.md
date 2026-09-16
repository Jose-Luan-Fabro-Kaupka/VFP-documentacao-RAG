# Rotina de biblioteca de API _WSetTitle( )

Altera o título da janela especificada para title.

```foxpro
void _WSetTitle(WHANDLE wh, char FAR *title)
WHANDLE wh;            /* Window handle. */
char FAR *title;            /* Window title. */
```

# Observações

Para remover um título de uma janela, passe (char FAR *)0 como o novo título.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria uma janela e define seu texto de título com _WSetTitle( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WSETTITL
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   WHANDLE wh;
   char FAR *buffer;
   wh = _WOpen(4,4,20,70,CLOSE | WEVENT,WINDOW_SCHEME,(Scheme FAR *)0,
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
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
