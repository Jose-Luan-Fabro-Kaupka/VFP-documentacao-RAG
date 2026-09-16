# Rotina de biblioteca de API _PutValue( )

Grava o valor val na posição de saída na janela de saída atual.

```foxpro
void _PutValue(Value FAR *val)
Value FAR *val;            /* Value to display. */
```

# Exemplo

O exemplo a seguir usa _PutValue( ) para exibir seu parâmetro do tipo Character em maiúsculas na tela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO PUTVALUE
= XUPPER("upper")  && displays "UPPER" on screen
```

### Código C

```foxpro
#include "pro_ext.h"
void NullTerminate(Value FAR *cVal)
{
   if (!_SetHandSize(cVal->ev_handle, cVal->ev_length + 1))
   {
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
   _PutValue(&parm->p[0].val);
}
FoxInfo myFoxInfo[] = {
   {"XUPPER", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
