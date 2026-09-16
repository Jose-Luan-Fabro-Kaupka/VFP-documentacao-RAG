# Rotina de biblioteca da API _EdRevert( )

Descarta todas as alterações feitas no arquivo exibido na janela de edição especificada desde que ele foi salvo pela última vez com _EdSave( ).

```foxpro
void _EdRevert(WHANDLE wh)
WHANDLE wh;            /* Handle of editing window. */
```

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro. Depois de algumas edições — inserção de uma nova linha, recuo de duas linhas e exclusão de duas linhas — as alterações são descartadas com _EdRevert( ).

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO EDREVERT
= EDREVERT("x")
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
   _EdSetPos(wh, _EdGetLinePos(wh, 13));
   _EdInsert(wh, "Hello, world\r\n", _StrLen("Hello, world\n"));
   _EdSelect(wh, _EdGetLinePos(wh, 14), _EdGetLinePos(wh, 16));
   _EdIndent(wh, 1);
   _EdSelect(wh, _EdGetLinePos(wh, 9), _EdGetLinePos(wh, 12));
   _EdDelete(wh);
   _EdRevert(wh);
}
FoxInfo myFoxInfo[] = {
   {"EDREVERT", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
