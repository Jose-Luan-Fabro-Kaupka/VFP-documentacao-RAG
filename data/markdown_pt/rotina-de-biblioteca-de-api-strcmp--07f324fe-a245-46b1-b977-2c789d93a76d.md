# Rotina de biblioteca de API _StrCmp( )

Compara cada byte em duas cadeias de caracteres terminadas em nulo, começando pelo byte mais à esquerda.

```foxpro
int _StrCmp(char FAR *string1, char FAR *string2)
char FAR *string1;         /* First comparison string. */
char FAR *string2;         /* Second comparison string. */
```

# Observações

_StrCmp( ) retorna 0 se string1 e string2 forem iguais, um número positivo se o primeiro byte diferente em string1 for maior que o byte correspondente em string2 ou um número negativo se o primeiro byte diferente em string1 for menor que o byte correspondente em string2.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir usa _StrCmp( ) para comparar duas cadeias de caracteres passadas como parâmetros.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO STRCMP
? STRCMP("Hello, world.", "Hello, world.")  && matches; returns 0
? STRCMP("Hello, world.", "Hello, wurld.")  && no match; returns non-0
```

### Código C

```foxpro
#include <pro_ext.h>
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
   int RetValue;
   NullTerminate(&parm->p[0].val);
   NullTerminate(&parm->p[1].val);
   _HLock(parm->p[0].val.ev_handle);
   _HLock(parm->p[1].val.ev_handle);
   RetValue = _StrCmp(_HandToPtr(parm->p[0].val.ev_handle),
      _HandToPtr(parm->p[1].val.ev_handle));
   _RetInt(RetValue, 10); // does return control here
   _HUnLock(parm->p[0].val.ev_handle);
   _HUnLock(parm->p[1].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"STRCMP", (FPFI) Example, 2, "C,C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
