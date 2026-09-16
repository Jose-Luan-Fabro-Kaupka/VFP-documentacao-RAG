# Rotina de biblioteca de API _EdUndo( )

Desfaz a alteração mais recente feita no arquivo na janela especificada.

```foxpro
void _EdUndo(WHANDLE wh)
WHANDLE wh;            /* Handle of editing window. */
```

# Observações

Quando o usuário faz alterações em um arquivo, essas alterações são registradas no buffer de desfazer. _EdUndo( ) pode ser emitido várias vezes para desfazer várias alterações. Você não pode desfazer uma alteração feita antes de emitir _EdSave( ).

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir abre um arquivo especificado por um parâmetro para edição. Após inserir uma nova linha, usa _EdUndo( ) para excluir a linha e, em seguida, chama _EdRedo( ) para restaurar a linha inserida.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDUNDO
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
   _Execute("WAIT WINDOW 'New line inserted.\
      Press any key to undo.'");
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
