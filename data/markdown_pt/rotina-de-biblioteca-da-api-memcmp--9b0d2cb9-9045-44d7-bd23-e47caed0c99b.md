# Rotina de biblioteca da API _MemCmp( )

Compara duas áreas de memória de comprimento em bytes.

```foxpro
int _MemCmp(void FAR *ptr1, void FAR *ptr2, unsigned int length)
void FAR *ptr1;            /* First point to start compare. */
void FAR *ptr2;            /* Second point to start compare. */
unsigned int length;         /* How much to compare in bytes. */
```

# Observações

_MemCmp( ) compara cada byte nas duas áreas, começando com o byte mais à esquerda em cada uma, até que dois bytes não correspondam. _MemCmp( ) retorna 0 se todos os bytes nas áreas correspondem, um número positivo se o primeiro byte não correspondente na primeira área é maior que o byte correspondente na segunda área, ou um número negativo se o primeiro byte não correspondente na segunda área é maior que o byte correspondente na primeira área.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir usa _MemCmp( ) para comparar dois parâmetros de caractere até o comprimento do primeiro byte não correspondente.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO MEMCMP
? MEMCMP("Hello, world.", "Hello, world.")  && returns 0
? MEMCMP("Hello, world.", "Hello, wurld.")  && returns non-0
```

### Código C

```foxpro
#include <pro_ext.h>
#define min(a, b) ((a) < (b) ? (a) : (b))
FAR Example(ParamBlk FAR *parm)
{
   int LenToCmp, RetValue;
   LenToCmp = min(parm->p[0].val.ev_length, parm->p[1].val.ev_length);
   _HLock(parm->p[0].val.ev_handle);
   _HLock(parm->p[1].val.ev_handle);
   RetValue = _MemCmp(_HandToPtr(parm->p[0].val.ev_handle),
      _HandToPtr(parm->p[1].val.ev_handle), LenToCmp);
   _RetInt(RetValue, 10); // does return control here
   _HUnLock(parm->p[0].val.ev_handle);
   _HUnLock(parm->p[1].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"MEMCMP", (FPFI) Example, 2, "C,C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
