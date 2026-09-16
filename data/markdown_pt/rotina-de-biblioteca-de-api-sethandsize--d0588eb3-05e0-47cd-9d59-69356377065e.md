# Rotina de biblioteca de API _SetHandSize( )

Altera a quantidade de memória alocada ao handle do bloco de memória.

```foxpro
unsigned short _SetHandSize(MHANDLE hand, unsigned long size)
MHANDLE hand;            /* Memory block handle. */
unsigned int size;            /* New number of bytes. */
```

# Observações

_SetHandSize( ) retorna True (um inteiro diferente de 0) se a realocação for bem-sucedida, ou False (0) se a realocação falhar. Os dados associados ao MHANDLE são preservados. Se hand for um MHANDLE bloqueado, _SetHandSize( ) falha.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir usa _SetHandSize( ) para alterar a quantidade de memória alocada a um MHANDLE.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO SETHANDS
= HANDTOPTR("Hello, world.") && displays "Hello, world" on screen
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
   NullTerminate(&parm->p[0].val);
   _HLock(parm->p[0].val.ev_handle);
   _PutStr(_HandToPtr(parm->p[0].val.ev_handle));
   _HUnLock(parm->p[0].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"HANDTOPTR", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
