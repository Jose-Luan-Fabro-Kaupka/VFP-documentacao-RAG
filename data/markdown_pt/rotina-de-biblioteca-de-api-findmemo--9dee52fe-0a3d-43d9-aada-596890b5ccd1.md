# Rotina de biblioteca de API _FindMemo( )

Retorna o endereço de memória do primeiro caractere no campo memo fld para o registro atual na área de trabalho selecionada.

```foxpro
long _FindMemo(Locator FAR *fld)
Locator FAR *fld;            /* Memo field name. */
```

# Observações

_FindMemo( ) permite obter acesso direto ao conteúdo do campo memo para o registro atual. Quando o campo memo para o registro atual está vazio, ou quando fld não é o nome de um campo memo, _FindMemo( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir recupera o conteúdo de um campo memo para o registro atual. Ele usa FindMemo( ) para encontrar o local do conteúdo do memo para o registro atual dentro do arquivo memo. O exemplo então move o ponteiro do arquivo para este local com _FSeek( ) e armazena o conteúdo do campo memo na memória usando _FRead( _MemoSize( )).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO FINDMEMO
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
