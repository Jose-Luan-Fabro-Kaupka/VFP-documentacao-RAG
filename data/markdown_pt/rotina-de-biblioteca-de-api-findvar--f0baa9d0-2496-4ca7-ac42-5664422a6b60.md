# Rotina de biblioteca de API _FindVar( )

Fornece uma maneira de inicializar um Locator para que você possa usar _Store( ) para colocar dados em uma variável de memória ou campo existente.

```foxpro
int _FindVar(NTI nti, int where, Locator FAR *loc)
NTI nti;                     /* NTI number of variable or field. */
int where;                  /* Work area number. */
Locator FAR *loc;            /* Locator. */
```

# Observações

_FindVar( ) preenche o Locator passado com informações sobre uma variável ou campo nomeado nti que existe em uma área de trabalho especificada por where.
 - Se where for – 1, nti é considerado uma variável de memória.
- Se where for 1 – 225, nti é considerado um campo na área de trabalho do número especificado.
- Se where for 0, _FindVar primeiro verifica se nti é uma variável de memória. Se não for uma variável de memória, a área de trabalho atual é verificada quanto a um campo com o NTI especificado.

_FindVar( ) retorna True (um inteiro diferente de 0) se uma variável ou campo nti for encontrado em where; caso contrário, _FindVar( ) retorna False (0).

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir exibe o valor de uma variável Visual FoxPro de uma maneira bem indireta.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO FINDVAR
TestVar= "This is a test"
= QMARK("TestVar")
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
FAR NameTableIndexEx(ParamBlk FAR *parm)
{
   NTI nti;
   char FAR *name;
   Locator loc;
   Value val;
//   Null terminate character string, name of variable
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(parm->p[0].val.ev_handle);
   name = (char FAR *) _HandToPtr(parm->p[0].val.ev_handle);
   name[parm->p[0].val.ev_length] = '\0';
   nti = _NameTableIndex(name);
   _FindVar(nti, 0, &loc);
   _Load(&loc, &val);
   _PutValue(&val);
}
FoxInfo myFoxInfo[] = {
   {"QMARK", (FPFI) NameTableIndexEx, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
