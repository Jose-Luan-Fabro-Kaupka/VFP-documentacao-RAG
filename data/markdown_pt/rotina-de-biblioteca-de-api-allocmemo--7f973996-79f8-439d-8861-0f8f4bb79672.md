# Rotina de biblioteca de API _AllocMemo( )

Aloca size bytes de espaço no arquivo memo para um campo e insere o novo número de bloco no registro associado no banco de dados.

```foxpro
long _AllocMemo(Locator FAR *fld, long size)
Locator FAR *fld;            /* Pointer to locator
 that defines the memo field. */
long size;                     /* Size of allocated space in bytes. */
```

# Observações

Quando _AllocMemo( ) é bem-sucedido, retorna a localização no arquivo para começar a gravar; caso contrário, retorna – 1.

> **Cuidado:** Gravar mais de size bytes causa corrupção do arquivo memo.

Se você planeja substituir um campo memo usando métodos diretos, certifique-se de que sua rotina chame _AllocMemo( ) antes de gravar no arquivo memo, mesmo se o novo valor tiver o mesmo comprimento ou for menor que o original. Isso evita problemas em situações multiusuário. _AllocMemo( ) reutiliza o espaço previamente alocado quando é seguro fazer isso.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria novos conteúdos de campo memo.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO ALLOMEMO
CREATE TABLE wMemo (memoField M)
APPEND BLANK
= NewMemo(@MemoField, "Hello, World.")
APPEND BLANK
= NewMemo(@MemoField, "Isn't this fun?")
```

### Código C

```foxpro
#include <pro_ext.h>
FAR newMemo(ParamBlk FAR *parm)
{
   Locator FAR *memoFldLoc;
   FCHAN fchMemo;
   int memoLen;
   long loc;
   if ((fchMemo = _MemoChan(-1)) == -1)
   {
      _UserError("_MemoChan() failed");
   }
   memoFldLoc = &parm->p[0].loc;
   memoLen = parm->p[1].val.ev_length;
   if ((loc = _AllocMemo(memoFldLoc, memoLen)) == -1)
   {
      _UserError("_AllocMemo() failed");
   }
   _FSeek(fchMemo, loc, FS_FROMBOF);
   _HLock(parm->p[1].val.ev_handle);
   _FWrite(fchMemo, _HandToPtr(parm->p[1].val.ev_handle), memoLen);
   _HUnLock(parm->p[1].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"NEWMEMO", (FPFI) newMemo, 2, "R,C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
