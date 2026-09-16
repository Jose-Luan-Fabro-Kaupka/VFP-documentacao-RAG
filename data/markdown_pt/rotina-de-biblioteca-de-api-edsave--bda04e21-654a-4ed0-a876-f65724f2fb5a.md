# Rotina de biblioteca de API _EdSave( )

_EdSave( ) salva o arquivo na janela especificada sem encerrar a sessão de edição.

```foxpro
void _EdSave(WHANDLE wh)
WHANDLE wh;            /* Handle of editing window. */
```

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro. O exemplo insere uma nova linha, recua duas linhas e exclui duas linhas. Após a inserção da nova linha, o exemplo chama _EdSave( ). Depois, após o recuo e a exclusão, o exemplo chama _EdUndo( ) três vezes na tentativa de desfazer toda a edição, mas a inserção feita antes da chamada a _EdSave( ) não pode ser desfeita. O exemplo executa mais duas operações de edição, inserindo duas linhas e excluindo duas linhas, com uma chamada a _EdSave( ) entre elas. Por último, o exemplo chama _EdRevert( ), mas ele também só pode desfazer alterações feitas desde a última _EdSave( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDSAVE
= EDSAVE("x")
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
   _EdSave(wh);
   _EdSelect(wh, _EdGetLinePos(wh, 14), _EdGetLinePos(wh, 16));
   _EdIndent(wh, 1);
   _EdSelect(wh, _EdGetLinePos(wh, 9), _EdGetLinePos(wh, 12));
   _EdDelete(wh);
   _Execute("WAIT WINDOW 'Press any key to undo changes.'");
   _EdUndo(wh);  // undo deletion
   _EdUndo(wh);  // undo indent
   _EdUndo(wh);  // attempt to undo insertion, but can't
   _EdSelect(wh, _EdGetLinePos(wh, 14), _EdGetLinePos(wh, 16));
   _EdIndent(wh, 1);
   _EdSave(wh);
   _EdSelect(wh, _EdGetLinePos(wh, 9), _EdGetLinePos(wh, 12));
   _EdDelete(wh);
   _EdRevert(wh);   // undoes deletion
}
FoxInfo myFoxInfo[] = {
   {"EDSAVE", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
