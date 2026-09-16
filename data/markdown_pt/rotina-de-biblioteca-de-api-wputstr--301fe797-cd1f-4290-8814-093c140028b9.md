# Rotina de biblioteca de API _WPutStr( )

Exibe uma cadeia de caracteres terminada em nulo na posição de saída na janela especificada e na cor atual.

```foxpro
void _WPutStr(WHANDLE wh, char FAR *theStr)
WHANDLE wh;            /* Window handle. */
char FAR *theStr;               /* String to display. */
```

# Observações

A saída que normalmente faz a janela rolar produz resultados indefinidos em janelas que não têm o atributo AUTOSCROLL definido.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir usa _WPutStr( ) para exibir uma cadeia de caracteres contendo todos os valores de 8 bits (exceto '\0') em uma nova janela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WPUTSTR
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   int i;
   WHANDLE wh;
   char String[256];
   wh = _WOpen(2,2,20,70,WEVENT | CLOSE,WINDOW_SCHEME,(Scheme FAR *) 0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   for (i = 0; i < 255; i++)
      String[i] = i + 1;
   String[255] = '\0';
   _WPutStr(wh, String);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
