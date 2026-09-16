# Rotina de biblioteca API _EdRedo( )

Executa novamente a alteração feita no arquivo na janela de edição especificada que foi desfeita pelo _EdUndo( ) mais recente.

```foxpro
void _EdRedo(WHANDLE wh)
WHANDLE wh;            /* Handle of editing window. */
```

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro. Após inserir uma nova linha, a nova linha é removida usando _EdUndo( ) e então inserida novamente usando _EdRedo( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDREDO
= EDREDO("x")
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
   _EdInsert(wh, "Hello, world\n", _StrLen("Hello, world\n"));
   _Execute("WAIT WINDOW 'New line inserted.  Press any key to undo.'");
   _EdUndo(wh);
   _Execute("WAIT WINDOW 'Insertion undone.  Press any key to redo.'");
   _EdRedo(wh);
}
FoxInfo myFoxInfo[] = {
   {"EDREDO", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
