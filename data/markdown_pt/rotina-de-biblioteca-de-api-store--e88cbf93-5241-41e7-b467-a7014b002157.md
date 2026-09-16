# Rotina de biblioteca de API _Store( )

Substitui a variável de memória especificada por loc com o valor val.

```foxpro
int _Store(Locator FAR *loc, Value FAR *val)
Locator FAR *loc;            /* Memory variable locator. */
Value FAR *val;               /* Value to store. */
```

# Observações

Referencie elementos individuais de matriz definindo l_subs para o número de subscritos que você especificou e l_sub1 e l_sub2 para os subscritos reais. O primeiro elemento de uma matriz é numerado como 1. Se loc especificar uma matriz e l_subs for 0, _Store( ) armazena o valor em val em todos os elementos da matriz.

_Store( ) retorna 0 se for bem-sucedido. Se falhar, _Store( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro. Se _Store( ) ficar sem memória ao armazenar em uma matriz, alguns valores de alguns elementos da matriz podem ter sido definidos e outros podem não ter sido.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir converte para maiúsculas um argumento de cadeia de caracteres passado por referência.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO STORE
x = "abc"
= XUPPER(@x)
? x
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR Upper(ParamBlk FAR *parm)
{
      char FAR *pString;
      Value val;
      int i;
//
//   _Load() and _Store are the functions of interest for pass-by-reference.
//
   _Load(&parm->p[0].loc, &val);
//
//   FoxPro doesn't check the type of pass-by-reference arguments, so we do.
//
   if (val.ev_type != 'C') {
      _Error(9); // "Data type mismatch"
   }
  pString = _HandToPtr(val.ev_handle);
   for (i = 0; i < val.ev_length; i++)  {
      if ('a' <= *pString && *pString <= 'z') {
         *pString += ('A' - 'a');
      }
      pString++;
   }
   _Store(&parm->p[0].loc, &val);
   //
   // We need to free the handle that we created with  _LOAD()
   //
   _FreeHand(val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"XUPPER", (FPFI) Upper, 1, "R"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
