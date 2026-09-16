# Rotina de biblioteca API _EdSetPos( )

Move o ponto de inserção para a posição de deslocamento especificada no arquivo na janela de edição especificada, desmarcando qualquer texto selecionado.

```foxpro
void _EdSetPos(WHANDLE wh, EDPOS thePos)
WHANDLE wh;            /* Handle of editing window. */
EDPOS thePos;               /* Specified offset position. */
```

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro. Usando _EdSetPos( ), define o ponto de inserção na posição 19 do arquivo. Chama _EdGetPos( ) e insere algum texto para verificar se o ponto de inserção foi definido.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDSETPOS
= EDSETPOS('x')
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 6;
   _PutValue(&val);
}
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   EDPOS edpos;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdSetPos(wh, 19);
   _PutStr("\n_EdSetPos(wh, 19)");
   edpos = _EdGetPos(wh);
   _PutStr("\n_EdGetPos(wh) ="); putLong(edpos);
   _EdInsert(wh, "*** Inserted at EDPOS = 19 ***",
      _StrLen("*** Inserted at EDPOS = 19 ***"));
}
FoxInfo myFoxInfo[] = {
   {"EDSETPOS", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
