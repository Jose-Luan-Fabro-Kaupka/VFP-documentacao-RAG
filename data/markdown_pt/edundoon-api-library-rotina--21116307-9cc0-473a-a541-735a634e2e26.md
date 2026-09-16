# _EdUndoOn( ) API Library Rotina

Permite agrupar uma série de ações como uma única ação para uso com _EdUndo( ) e _EdRedo( ).

```foxpro
void _EdUndoOn(WHANDLE wh, int Grouped)
WHANDLE wh;            /* Window handle. */
int Grouped;                  /* Toggle grouping off. */
```

# Observações
As ações que ocorrem após você passar o parâmetro Grouped como FALSE com _EdUndoOn( ), ou após você emitir _EdUndo( ), não são mais agrupadas como uma única ação.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Acessando o Visual FoxPro API.

# Exemplo
O exemplo a seguir mostra como usar _EdUndoOn( ) para agrupar operações de edição que você pode desfazer como um grupo usando _EdUndo( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDUNDOON
= EDUNDOON("x")  && edit file "x"
```

### C Código

```foxpro
#include <pro_ext.h>
#define TRUE   1
#define FALSE   0
FAR Example(ParamBlk FAR *parm)
{
   char FAR *pFileName;
   WHANDLE wh;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   pFileName = (char FAR *) _HandToPtr(parm->p[0].val.ev_handle);
   pFileName[parm->p[0].val.ev_length] = '\0';
   wh = _EdOpenFile(pFileName, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdUndoOn(wh, TRUE); // start undo group
   _EdSetPos(wh, _EdGetLinePos(wh, 13));
   _EdInsert(wh, "Hello, world\n", _StrLen("Hello, world\n"));
   _EdSelect(wh, _EdGetLinePos(wh, 14), _EdGetLinePos(wh, 16));
   _EdIndent(wh, 1);
   _EdUndoOn(wh, FALSE); // end undo group
   _EdUndoOn(wh, TRUE); // start another undo group
   _EdSelect(wh, _EdGetLinePos(wh, 9), _EdGetLinePos(wh, 12));
   _EdDelete(wh);
   _EdSetPos(wh, _EdGetLinePos(wh, 13));
   _EdInsert(wh, "Hello, world\n", _StrLen("Hello, world\n"));
   _Execute("WAIT WINDOW 'Press any key to undo changes.'");
   _EdUndoOn(wh, TRUE); // undoes to start of undo group
}
FoxInfo myFoxInfo[] = {
   {"EDUNDOON", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
