# Rotina de biblioteca de API _StrLen( )

Retorna o comprimento em bytes da cadeia de caracteres terminada em nulo especificada.

```foxpro
int _StrLen(char FAR *string)
char FAR *string;            /* String to be measured. */
```

# Exemplo

O exemplo a seguir é semelhante à função LEN( ) do Visual FoxPro, mas não pode manipular cadeias de caracteres com '\0' incorporado.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO STRLEN
? STRLEN("Hello") && returns 5
```

### Código C

```foxpro
#include <pro_ext.h>
void NullTerminate(Value FAR *cVal)
{
   if (!_SetHandSize(cVal->ev_handle, cVal->ev_length + 1)) {
      _Error(182); // "Insufficient memory"
   }
   ((char FAR *) _HandToPtr(cVal->ev_handle))[cVal->ev_length] = '\0';
}
FAR Example(ParamBlk FAR *parm)
{
   NullTerminate(&parm->p[0].val);
   _HLock(parm->p[0].val.ev_handle);
   _RetInt(_StrLen(_HandToPtr(parm->p[0].val.ev_handle)), 10);
   _HUnLock(parm->p[0].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"STRLEN", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
