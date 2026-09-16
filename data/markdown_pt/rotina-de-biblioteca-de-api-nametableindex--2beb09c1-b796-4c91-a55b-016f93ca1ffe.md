# Rotina de biblioteca de API _NameTableIndex( )

Retorna o índice da tabela de nomes que corresponde a um determinado nome ou retorna – 1 se esse nome não estiver na tabela de nomes.

```foxpro
NTI _NameTableIndex(char FAR *name)
char FAR *name;            /* Name. */
```

# Observações

O nome pode ser encontrado na tabela de nomes mesmo que uma variável com o nome name não exista. Para determinar se uma variável com o nome name existe, use _FindVar( ), especificando o índice da tabela de nomes retornado por _NameTableIndex( ) como o parâmetro nti.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir libera uma variável de memória cujo nome é fornecido como um argumento de caractere. Observe que _NameTableIndex( ) encontra o nome da variável depois que ela foi liberada. Portanto, _NameTableIndex( ) é usado em combinação com _FindVar( ) para garantir que a variável de memória esteja atualmente definida.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO NTI
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
   //   Null terminate character string, name of variable
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
