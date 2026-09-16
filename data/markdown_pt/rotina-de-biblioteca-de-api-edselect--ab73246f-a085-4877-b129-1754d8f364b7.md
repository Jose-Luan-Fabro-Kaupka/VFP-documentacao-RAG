# Rotina de biblioteca de API _EdSelect( )

Seleciona o intervalo entre as duas posições de deslocamento especificadas, inclusive, do arquivo na janela de edição designada.

```foxpro
void _EdSelect(WHANDLE wh, EDPOS startPos, EDPOS endPos)
WHANDLE wh;            /* Handle of editing window. */
EDPOS startPos;         /* Beginning offset position of selection. */
EDPOS endPos;         /* Ending offset position of selection. */
```

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro, seleciona o primeiro caractere do arquivo usando _EdSelect( ), copia a seleção para a área de transferência usando _EdCopy( ) e a cola após o segundo caractere usando _EdPaste( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDSELECT
= EDCOPY("x")
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
   _EdCopy(wh);
   _EdSetPos(wh, 2);
   _EdPaste(wh);
}
FoxInfo myFoxInfo[] = {
   {"EDCOPY", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
