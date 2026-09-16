# Rotina de biblioteca de API _PutStr( )

Exibe uma cadeia de caracteres terminada em nulo na posição de saída na janela de saída atual em seu atributo normal (cor 0).

```foxpro
void _PutStr(char FAR *str)
char FAR *str;               /* String to display. */
```

# Observações

_PutStr( ) trata caracteres especiais, como nova linha, retorno de carro e sino, como caracteres de controle e não os exibe na tela.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir usa _PutStr( ) para exibir seu parâmetro de tipo caractere em letras maiúsculas na tela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO PUTSTR
= XUPPER("upper")  && displays "UPPER" on the screen
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
   _HLock(parm->p[0].val.ev_handle);
   _PutStr(_HandToPtr(parm->p[0].val.ev_handle));
   _HUnLock(parm->p[0].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"XUPPER", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
