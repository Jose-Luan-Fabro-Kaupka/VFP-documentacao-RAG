# Rotina de biblioteca de API _MemAvail( )

Determina se há memória suficiente disponível para alocar um handle de memória do tamanho bytes.

```foxpro
BOOL _MemAvail(unsigned long size)
unsigned int size;            /* Size of memory handle in bytes. */
```

# Observações

A função retorna True (um inteiro diferente de 0) se houver memória suficiente disponível, ou False (0) se não houver.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir constrói uma lista encadeada de alocações de handles de memória de 1K até que a memória disponível seja utilizada. Em seguida, libera as alocações e retorna o número de alocações realizadas. _MemAvail( ) é usada para encerrar o primeiro loop while.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO MEMAVAIL
? MEMAVAIL()  && displays approx. memory available in K
```

### Código C

```foxpro
#include <pro_ext.h>
#define ALLOCSIZE 1024
FAR Example(ParamBlk FAR *parm)
{
   int nHandles = 0;
   MHANDLE head = 0, mh;
   while (_MemAvail(ALLOCSIZE))
   {
      mh = _AllocHand(ALLOCSIZE);
      *((MHANDLE *) _HandToPtr(mh)) = head;
      head = mh;
      nHandles++;
   }
   _RetInt(nHandles, 10);
   while (head != 0)
   {
      mh = *((MHANDLE *) _HandToPtr(head));
      _FreeHand(head);
      head = mh;
   }
}
FoxInfo myFoxInfo[] = {
   {"MEMAVAIL", (FPFI) Example, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
