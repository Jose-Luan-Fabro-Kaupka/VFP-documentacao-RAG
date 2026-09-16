# Rotina de biblioteca API _Release( )

Libera da memória a variável de memória ou matriz especificada.

```foxpro
int _Release(NTI n)
NTI n;                     /* NTI number of variable or array
 to release. */
```

# Observações

_Release( ) retorna 0 se liberar com sucesso a variável de memória ou matriz, ou um inteiro cujo valor absoluto é um número de erro do Visual FoxPro se falhar.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir libera uma variável de memória cujo nome é fornecido como um argumento de caracteres. _NameTableIndex( ) é usado para encontrar o NTI da variável.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO RELEASE
x = 123
= XRELEASE("x")
```

### Código C

```foxpro
#include <pro_ext.h>
FAR ReleaseEx(ParamBlk FAR *parm)
{
   NTI nti;
   char FAR *name;
   int exitCode;
   Locator loc;
   // Null terminate character string, name of variable
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   name = (char FAR *) _HandToPtr(parm->p[0].val.ev_handle);
   name[parm->p[0].val.ev_length] = '\0';
   if ((nti = _NameTableIndex(name)) == -1)
   {
      _HUnLock(parm->p[0].val.ev_handle);
      _UserError("Cannot find variable in name table.");
   }
   _HUnLock(parm->p[0].val.ev_handle);
   if (_FindVar(nti, -1, &loc))
   {
      _PutStr("\nVariable exists prior to _Release().");
   }
   if ((exitCode =_Release(nti)) < 0)
   {
      _Error(-exitCode);
   }
   _HLock(parm->p[0].val.ev_handle);
   name = (char FAR *) _HandToPtr(parm->p[0].val.ev_handle);
   name[parm->p[0].val.ev_length] = '\0';
   if ((nti = _NameTableIndex(name)) != -1)
   {
      _PutStr("\n_NameTableIndex() still finds variable \
         after it is released.");
   }
   _HUnLock(parm->p[0].val.ev_handle);
   if (!_FindVar(nti, -1, &loc))
   {
      _PutStr("\nVariable does not exist after _Release().");
   }
}
FoxInfo myFoxInfo[] = {
   {"XRELEASE", (FPFI) ReleaseEx, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
