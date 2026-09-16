# Rotina de biblioteca de API _WHide( )

Remove uma janela da tela, mas mantém o controle de seu conteúdo para que você possa exibi-la novamente.

```foxpro
void _WHide(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Exemplo

O exemplo a seguir oculta a janela cujo título é passado como argumento.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WHIDE
CREATE TABLE X (X C(10))
BROWSE NOWAIT
WAIT WINDOW "Press A Key To Hide Window"
SET LIBR TO WFINDTIT
= WHIDE("X")
WAIT WINDOW "Window Is Hidden"
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR Example(ParamBlk FAR *parm)
{
//   For readability---
#define pTITLE ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+ 1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   pTITLE[parm->p[0].val.ev_length] = '\0';
   wh = _WFindTitle(pTITLE);
   _HUnLock(parm->p[0].val.ev_handle);
   _WHide(wh);
}
FoxInfo myFoxInfo[] = {
   {"WHIDE", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
