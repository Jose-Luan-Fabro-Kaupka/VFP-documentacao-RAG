# Rotina de biblioteca de API _FreeHand( )

Libera um identificador de memória hand previamente alocado por meios como _AllocHand( ).

```foxpro
void _FreeHand(MHANDLE hand)
MHANDLE hand;            /* Memory handle. */
```

# Exemplo

O exemplo a seguir aloca 1024 blocos de blocos de memória de 16384 bytes, totalizando 16 MB, liberando cada bloco de memória usando _FreeHand( ) antes de alocar o próximo.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO FREEHAND
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR Example(ParamBlk FAR *parm)
{
   MHANDLE mh;
   int i;
   for (i = 0; i < 1024; i++)
   {
      if ((mh = _AllocHand(16384)) == 0)
      {
         _Error(182);  // "Insufficient memory"
      }
      _FreeHand(mh);
   }
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) Example, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
