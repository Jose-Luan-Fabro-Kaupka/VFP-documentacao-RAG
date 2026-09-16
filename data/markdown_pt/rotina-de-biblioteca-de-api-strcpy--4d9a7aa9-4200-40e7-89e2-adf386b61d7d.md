# Rotina de biblioteca de API _StrCpy( )

Copia uma cadeia de caracteres terminada em nulo de src para dest.

```foxpro
void _StrCpy(char FAR *dest, char FAR *src)
char FAR *dest;            /* Destination location. */
char FAR *src;               /* Source location. */
```

# Observações

_StrCpy( ) não suporta movimentações sobrepostas. Movimentações sobrepostas são necessárias quando src e dest compartilham alguns bytes. Se movimentações sobrepostas são necessárias, use _MemMove( ).

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir recebe um array do Visual FoxPro do tipo Character. Em seguida, substitui o segundo elemento usando _Store( ).

Antes de chamar MYFUNC( ), o código de exemplo do Visual FoxPro cria um array e o inicializa como tipo Character. MYFUNC( ) passa esse array por referência.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO STRCPY
? STRCPY("Hello", " world")   && returns "Hello world"
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
#define p0 (parm->p[0].val)
#define p1 (parm->p[1].val)
   if (!_SetHandSize(p0.ev_handle, p0.ev_length + p1.ev_length))
      _Error(182); // "Insufficient memory"
   _HLock(p0.ev_handle);
   _HLock(p1.ev_handle);
   ((char FAR *) _HandToPtr(p1.ev_handle))[p1.ev_length] = '\0';
   _StrCpy((char FAR *) _HandToPtr(p0.ev_handle) + p0.ev_length,
      _HandToPtr(p1.ev_handle));
   _RetChar(_HandToPtr(p0.ev_handle));
   _HUnLock(p0.ev_handle);
   _HUnLock(p1.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"STRCPY", (FPFI) Example, 2, "C,C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
