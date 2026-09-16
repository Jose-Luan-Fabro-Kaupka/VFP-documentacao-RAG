# Rotina de biblioteca de API _GetAPIHandle( )

Retorna o handle da FLL atual.

```foxpro
void _GetAPIHandle()
```

# Exemplo

O exemplo a seguir retorna o handle da FLL atual.

### Código Visual FoxPro

```foxpro
SET LIBR TO GETAPIHA.FLL
? GETAPIHAND()
```

### Código C

```foxpro
#include <pro_ext.h>
void getAPIHandle()
{
_RetInt((int) _GetAPIHandle(),15);
}
FoxInfo myFoxInfo[] =
{
   {"GETAPIHAND",  (FPFI) getAPIHandle, 0, ""},
};
FoxTable _FoxTable =
{
   (FoxTable  *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
