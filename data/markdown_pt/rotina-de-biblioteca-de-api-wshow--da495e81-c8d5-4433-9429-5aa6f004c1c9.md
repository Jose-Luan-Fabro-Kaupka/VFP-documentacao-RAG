# Rotina de biblioteca de API _WShow( )

Exibe uma janela oculta na tela.

```foxpro
void _WShow(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Observações

Quando você cria uma janela, ela fica oculta por padrão até que você use _WShow( ) para torná-la visível.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir contém duas rotinas de API. WINOPEN( ) abre uma janela, mas não chama _WShow( ), ilustrando que a janela permanece oculta até que _WShow( ) a exiba na tela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WSHOW
wh = WOPEN()
= WSHOW(wh)
```

### Código C

```foxpro
#include <pro_ext.h>
FAR WOpen(ParamBlk FAR *parm)
{
   _RetInt(_WOpen(2, 2, 20, 70, WEVENT | CLOSE, WINDOW_SCHEME,
      (Scheme FAR *) 0, WO_SYSTEMBORDER), 10);
}
FAR WShow(ParamBlk FAR *parm)
{
   _WShow(parm->p[0].val.ev_long);
}
FoxInfo myFoxInfo[] = {
   {"WOPEN", (FPFI) WOpen, 0, ""},
   {"WSHOW", (FPFI) WShow, 1, "I"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
