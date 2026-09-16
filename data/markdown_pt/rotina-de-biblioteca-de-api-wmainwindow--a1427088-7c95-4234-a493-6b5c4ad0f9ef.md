# Rotina de biblioteca de API _WMainWindow( )

Retorna o WHANDLE da janela principal do Visual FoxPro.

```foxpro
WHANDLE _WMainWindow(void any)
void any;                     /* Pointer. */
```

# Observações

Use a função Rotina de biblioteca de API _WhToHwnd( ) para converter o WHANDLE em um HWND do Windows.

# Exemplo

O exemplo a seguir grava uma mensagem na janela principal do Visual FoxPro.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WMAIN
= EXWMAIN()
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR Example(ParamBlk FAR *parm)
{
   WHANDLE wh = _WMainWindow();
   _WPutStr(wh, "\nThis is the FoxPro main window or desktop.");
}
FoxInfo myFoxInfo[] = {
   {"EXWMAIN", Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
