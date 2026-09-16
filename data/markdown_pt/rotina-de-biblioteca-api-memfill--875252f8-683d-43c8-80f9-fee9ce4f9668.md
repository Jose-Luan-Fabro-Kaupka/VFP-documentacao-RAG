# Rotina de Biblioteca API _MemFill( )

Preenche uma área de memória começando no local apontado por ptr com length cópias do byte em character.

```foxpro
void _MemFill(void FAR *ptr, int character, unsigned int length)
void FAR *ptr;               /* Starting point for fill. */
int character;               /* Character for fill. */
unsigned int length;         /* How many bytes to fill. */
```

# Exemplo

O exemplo a seguir usa _MemFill( ) para duplicar a funcionalidade da função REPLICATE( ) do Visual FoxPro.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO MEMFILL
x = xREPLICATE("x", 120)
? x
? LEN(x)
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   char FAR *rep;
   char c = *(char *) _HandToPtr(parm->p[0].val.ev_handle);
   rep = _Alloca((int) parm->p[1].val.ev_long + 1);
   _MemFill(rep, c, (int) parm->p[1].val.ev_long);
  rep[parm->p[1].val.ev_long] = '\0';
   _RetChar(rep);
}
FoxInfo myFoxInfo[] = {
   {"XREPLICATE", (FPFI) Example, 2, "C,I"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
