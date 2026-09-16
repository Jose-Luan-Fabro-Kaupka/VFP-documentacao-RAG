# Rotina de biblioteca de API _Alloca( )

Aloca um bloco de espaço na pilha para a rotina chamadora.

```foxpro
void FAR * _Alloca(unsigned int size)
unsigned int size;            /* Size of stack space to allocate in
bytes. */
```

# Observações

_Alloca( ) retorna um ponteiro para o bloco se o bloco for alocado com sucesso, ou retorna zero se o bloco não for alocado. _Alloca( ) libera a memória automaticamente quando a rotina termina, portanto não é necessária uma rotina de liberação correspondente.

> **Cuidado:** Alguns compiladores C, como o MPW C, não suportam alocação de memória na pilha; chamadas a _Alloca() usando esses compiladores terão resultados imprevisíveis. Em vez disso, use variáveis locais ou chamadas a _AllocHand() e _FreeHand() no seu código para reservar memória.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir duplica a ação da função REPLICATE( ) do Visual FoxPro. A memória usada temporariamente para duplicar o caractere provém de _Alloca( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO ALLOCA
x = xREPLICATE("x", 120)
? x
? LEN(x)
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR allocaEx(ParamBlk FAR *parm)
{
   char FAR *rep;
   char c = *(char *) _HandToPtr(parm->p[0].val.ev_handle);
   rep = _Alloca((int) parm->p[1].val.ev_long + 1);
   _MemFill(rep, c, (int) parm->p[1].val.ev_long);
  rep[parm->p[1].val.ev_long] = '\0';  // null terminate
   _RetChar(rep);
}
FoxInfo myFoxInfo[] =
{
   {"XREPLICATE", (FPFI) allocaEx, 2, "C,I"},
};
FoxTable _FoxTable =
{
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
