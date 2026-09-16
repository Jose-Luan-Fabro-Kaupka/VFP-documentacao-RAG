# Rotina de biblioteca de API _EdInsert( )

Insere o número especificado de bytes, começando com o endereço TEXT * especificado, no ponto de inserção.

```foxpro
void _EdInsert(WHANDLE wh, TEXT *theStr, unsigned long Bytes)
WHANDLE wh;            /* Handle of editing window. */
TEXT *theStr;               /* Address of beginning of insertion
 text. */
unsigned long Bytes;         /* Number of bytes to insert. */
```

# Exemplo

O exemplo a seguir abre uma sessão de edição para um arquivo especificado por um parâmetro e insere a linha de texto "Hello, world" como a nova décima quarta linha no arquivo.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDINSERT
= EDINSERT("x")
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1)) {
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdSetPos(wh, _EdGetLinePos(wh, 13));
   _EdInsert(wh, "Hello, world\n", _StrLen("Hello, world\n"));
}
FoxInfo myFoxInfo[] = {
   {"EDINSERT", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
