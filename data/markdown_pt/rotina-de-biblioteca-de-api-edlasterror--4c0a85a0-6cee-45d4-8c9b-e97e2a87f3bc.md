# Rotina de biblioteca de API _EdLastError( )

_EdLastError( ) retorna o número do erro do erro de editor mais recente associado à janela de edição especificada.

```foxpro
int _EdLastError(WHANDLE wh)
WHANDLE wh;            /* Handle of editing window. */
```

# Exemplo

O exemplo a seguir exibe o código de erro retornado por _EdLastError( ) após várias operações do editor. Como erros de editor são reservados para situações graves, como pouca memória, o exemplo a seguir geralmente exibirá um código de erro 0.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDLASTER
= EDLASTERR("x")  && displays _EdLastError() after operations on file "x"
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 10;
   _PutValue(&val);
}
FAR Example(ParamBlk FAR *parm)
{
   char FAR *pFileName;
   WHANDLE wh;
   EDENV EdEnv;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   pFileName = (char FAR *) _HandToPtr(parm->p[0].val.ev_handle);
   pFileName[parm->p[0].val.ev_length] = '\0';
   wh = _EdOpenFile(pFileName, FO_READONLY);
   _HUnLock(parm->p[0].val.ev_handle);
//   Position past end of file
   _EdGetEnv(wh, &EdEnv);
   _EdSetPos(wh, EdEnv.length + 128);
   _PutStr("\n_EdLastError() ="); putLong(_EdLastError(wh));
//   _EdCopy() with no selection
   _EdSetPos(wh, 1);
   _EdCopy(wh);
   _PutStr("\n_EdLastError() ="); putLong(_EdLastError(wh));
//   _EdScrollToSel() with no selection
   _EdScrollToSel(wh, TRUE);
   _PutStr("\n_EdLastError() ="); putLong(_EdLastError(wh));
}
FoxInfo myFoxInfo[] = {
   {"EDLASTERR", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
