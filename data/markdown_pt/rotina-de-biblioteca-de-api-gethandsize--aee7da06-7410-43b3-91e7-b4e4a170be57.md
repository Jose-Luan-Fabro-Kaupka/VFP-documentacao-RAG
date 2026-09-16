# Rotina de biblioteca de API _GetHandSize( )

Retorna o número utilizável de bytes associado a um handle de bloco de memória hand especificado.

```foxpro
unsigned long _GetHandSize(MHANDLE hand)
MHANDLE hand;            /* Handle of memory block. */
```

# Observações

O número utilizável de bytes é sempre maior ou igual ao número de bytes solicitado mais recentemente para este MHANDLE por _AllocHand( ) ou por uma chamada bem-sucedida a _SetHandSize( ).

> **Observação:** _GetHandSize() não causa reorganização de memória.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir aloca blocos de memória de vários tamanhos de 1 a 215 e mostra o valor retornado por _GetHandSize( ) para essas alocações. Observe que o valor retornado por _GetHandSize( ) às vezes é exatamente igual ao tamanho solicitado por _AllocHand( ); geralmente é um pouco maior.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO GETHANDS
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 5;
   _PutValue(&val);
}
void FAR Example(ParamBlk FAR *parm)
{
   MHANDLE mh;
   unsigned int allocSize;
   for (allocSize = 1;; allocSize *= 2)
   {
      if ((mh = _AllocHand(allocSize)) == 0)
      {
         _Error(182);  // "Insufficient memory"
      }
      _PutStr("\n_AllocHand("); putLong(allocSize); _PutStr(")");
      _PutStr("\n_GetHandSize() ="); putLong(_GetHandSize(mh));
      _FreeHand(mh);
      if (allocSize == 32768)
      {
         break;
      }
   }
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
