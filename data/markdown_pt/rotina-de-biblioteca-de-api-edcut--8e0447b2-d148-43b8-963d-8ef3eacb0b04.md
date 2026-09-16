# Rotina de biblioteca de API _EdCut( )

Copia a parte selecionada do arquivo na janela de edição especificada para a área de transferência e a exclui da janela especificada.

```foxpro
void _EdCut(WHANDLE wh)
WHANDLE wh;            /* Handle of editing window. */
```

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro, recorta o primeiro caractere para a área de transferência usando _EdCut( ) e cola o caractere após o segundo caractere usando _EdPaste( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDCUT
= EDCUT("x")
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdSelect(wh, 0, 1);
   _EdCut(wh);
   _EdSetPos(wh, 2);
   _EdPaste(wh);
}
FoxInfo myFoxInfo[] = {
   {"EDCUT", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
