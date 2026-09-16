# Rotina de biblioteca de API _MemoChan( )

Retorna o canal de arquivo do arquivo memo associado à área de trabalho especificada.

```foxpro
FCHAN _MemoChan(int workarea)
int workarea;               /* Work area number. */
```

# Observações

Se nenhum banco de dados estiver aberto nessa área de trabalho ou se o banco de dados não tiver um arquivo memo, _MemoChan( ) retornará – 1.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir recupera o conteúdo de um campo memo. _MemoChan( – 1) retorna um canal para o arquivo memo da área de trabalho atual. Esse FCHAN é usado como argumento para callbacks de E/S de arquivo de baixo nível da API.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO MEMOCHAN
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
