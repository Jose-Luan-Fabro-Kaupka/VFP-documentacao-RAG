# Rotina de Biblioteca de API _RetVal( )

Retorna qualquer tipo de dados do Visual FoxPro, exceto Memo.

```foxpro
void _RetVal(Value FAR *val)
Value FAR *val;            /* Pointer to value structure. */
```

# Observações

_RetVal( ) passa uma estrutura Value completa do Visual FoxPro. Você deve chamar _RetVal( ) para retornar uma cadeia de caracteres que contém caracteres nulos incorporados.

Para mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir usa _RetVal( ) para retornar seu parâmetro do tipo Character convertido para maiúsculas.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO RETVAL
? XUPPER("upper")  && returns "UPPER"
```

### Código C

```foxpro
#include "pro_ext.h"
void NullTerminate(Value FAR *cVal)
{
   if (!_SetHandSize(cVal->ev_handle, cVal->ev_length + 1)) {
      _Error(182); // "Insufficient memory"
   }
   ((char FAR *) _HandToPtr(cVal->ev_handle))[cVal->ev_length] = '\0';
}
FAR Example(ParamBlk FAR *parm)
{
   char FAR *pString;
   int i;
   NullTerminate(&parm->p[0].val);
   pString = _HandToPtr(parm->p[0].val.ev_handle);
   for (i = 0; i < parm->p[0].val.ev_length; i++)
   {
      if ('a' <= *pString && *pString <= 'z')
      {
         *pString += ('A' - 'a');
      }
      pString++;
   }
   _RetVal(&parm->p[0].val);
}
FoxInfo myFoxInfo[] = {
   {"XUPPER", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
