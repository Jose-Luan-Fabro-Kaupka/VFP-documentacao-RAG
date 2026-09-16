# Rotina de biblioteca de API _MemoSize( )

Retorna o comprimento do campo memo especificado no arquivo memo do registro atual.

```foxpro
long _MemoSize(Locator FAR *fld)
Locator FAR *fld;            /* Memo field address. */
```

# Observações

Quando o campo memo do registro atual está vazio, ou quando fld não é um campo memo, _MemoSize( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro.

Para mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir recupera o conteúdo de um campo memo do registro atual. _MemoSize( ) é usado para determinar quanta memória deve ser alocada para um buffer e quantos bytes devem ser lidos do arquivo memo.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO MEMOSIZE
CREATE TABLE WMemo (MemoField M)
APPEND BLANK
REPLACE MemoField WITH "Hello, World."
? GETMEMO(@MemoField)
```

### Código C

```foxpro
#include <pro_ext.h>
FAR FindMemoEx(ParamBlk FAR *parm)
{
   Locator FAR *memoFldLoc;
   FCHAN fchMemo;
   char FAR *memoContents;
   int memoLen;
   long loc;
   if ((fchMemo = _MemoChan(-1)) == -1)
   {
      _UserError("_MemoChan() failed");
   }
   memoFldLoc = &parm->p[0].loc;
   if ((loc = _FindMemo(memoFldLoc)) < 0)
   {
      _UserError("_FindMemo() failed");
   }
   if ((memoLen = _MemoSize(memoFldLoc)) < 0)
   {
      _UserError("_MemoSize() failed");
   }
   if ((memoContents = _Alloca(memoLen + 1)) == 0)
   {
      _Error(182); // "Insufficient memory"
   }
   _FSeek(fchMemo, loc, FS_FROMBOF);
   _FRead(fchMemo, memoContents, memoLen);
   memoContents[memoLen] = '\0';
   _RetChar(memoContents);
}
FoxInfo myFoxInfo[] = {
   {"GETMEMO", (FPFI) FindMemoEx, 1, "R"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
