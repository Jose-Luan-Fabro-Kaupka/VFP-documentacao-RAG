# Rotina de biblioteca de API _EdCloseFile( )

Fecha tanto a janela de edição especificada quanto o arquivo exibido na janela.

```foxpro
int _EdCloseFile(WHANDLE wh, int option)
WHANDLE wh;            /* Handle of editing window. */
int option;                  /* Closing options. */
```

# Observações

O parâmetro option pode ser um dos seguintes:
 Valores do parâmetro option
| int | resultado |
| --- | --- |
| 0 | Salvar imediatamente. |
| 1 | Salvar após confirmação na caixa de diálogo. |
| 2 | Abrir caixa de diálogo Save As. |

_EdCloseFile( ) retorna um dos seguintes:
 Valores de retorno de _EdCloseFile( )
| int | significado |
| --- | --- |
| 1 | Cancelar sem salvar arquivo. |
| 0 | Salvar e fechar arquivo. |
| – 1 | Descartar alterações e fechar arquivo. |

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir abre para edição um único arquivo especificado por um parâmetro, exclui um caractere e fecha a sessão de edição três vezes. Na primeira vez, a rotina chama _EdCloseFile( ) com a opção "Immediately save", na segunda vez com a opção "Save after dialog box" e na terceira vez com a opção "Open Save As dialog box". Cada vez, a rotina mostra o valor de retorno de _EdCloseFile( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDCLOSE
= EDCLOSE("x")
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 5;
   _PutValue(&val);
}
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   int retValue;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   // Open, delete a character, close "save without asking"
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdSelect(wh, 0, 1);
   _EdDelete(wh);
   retValue = _EdCloseFile(wh, 0); // save without asking
   _PutStr("\n_EdCloseFile() ="); putLong(retValue);
   // Open, delete a character, close "save with asking"
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdSelect(wh, 0, 1);
   _EdDelete(wh);
   retValue = _EdCloseFile(wh, 1); // save with asking
   _PutStr("\n_EdCloseFile() ="); putLong(retValue);
   // Open, delete a character, close "save as"
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdSelect(wh, 0, 1);
   _EdDelete(wh);
   retValue = _EdCloseFile(wh, 2); // save as
   _PutStr("\n_EdCloseFile() ="); putLong(retValue);
}
FoxInfo myFoxInfo[] = {
   {"EDCLOSE", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
