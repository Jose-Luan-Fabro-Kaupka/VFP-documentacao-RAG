# Rotina de biblioteca de API _WZoom( )

Minimiza ou maximiza a janela especificada ou a retorna ao estado normal.

```foxpro
void _WZoom(WHANDLE wh, int newstate)
WHANDLE wh;            /* Window handle. */
int newstate;                  /* State of window after zoom. */
```

# Observações

Você pode especificar o parâmetro newstate como WZ_MINIMIZE, WZ_NORMAL ou WZ_MAXIMIZE, que são definidos no arquivo PRO_EXT.H.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria e exibe uma janela. Em seguida, chama _WZoom( ) para esta janela com cada parâmetro possível.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WZOOM
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   WHANDLE wh;
   int row, col;
   wh = _WOpen(2,2,20,70,WEVENT | CLOSE,WINDOW_SCHEME,(Scheme FAR *) 0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   _Execute("WAIT WINDOW 'Press any key to minimize window'");
   _WZoom(wh, WZ_MINIMIZED);
   _Execute("WAIT WINDOW 'Press any key to normalize window'");
   _WZoom(wh, WZ_NORMAL);
   _Execute("WAIT WINDOW 'Press any key to maximize window'");
   _WZoom(wh, WZ_MAXIMIZED);
   _Execute("WAIT WINDOW 'Press any key to normalize window'");
   _WZoom(wh, WZ_NORMAL);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
