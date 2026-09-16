# Rotina de biblioteca de API _WFindTitle( )

Retorna o WHANDLE da janela com o título especificado.

```foxpro
WHANDLE _WFindTitle(TEXT *title)
TEXT *title;               /* Window title. */
```

# Exemplo

O exemplo a seguir oculta a janela cujo título é passado como argumento.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WFINDTIT
CREATE TABLE X (X C(10))
BROWSE NOWAIT
SET LIBR TO WFINDTIT
= WHIDE("X")
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR WFindTitleEx(ParamBlk FAR *parm)
{
//   For readability:
#define pTITLE ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
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
   {"WHIDE", (FPFI) WFindTitleEx, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
