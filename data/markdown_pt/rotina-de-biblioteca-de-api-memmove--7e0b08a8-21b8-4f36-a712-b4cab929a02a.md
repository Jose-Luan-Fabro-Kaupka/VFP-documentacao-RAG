# Rotina de biblioteca de API _MemMove( )

Copia length bytes a partir de src para dest.

```foxpro
void _MemMove(void FAR *dest, void FAR *src, unsigned int length)
void FAR *dest;            /* Destination. */
void FAR *src;               /* Starting position. */
unsigned int length;         /* How many bytes to move. */
```

# Observações

Movimentações sobrepostas são realizadas na direção apropriada para evitar corrupção de dados.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir usa _MemMove( ) para implementar uma função de substring. No Visual FoxPro, MEMMOVE(s, n1, n2) retorna a substring de s a partir da posição n1 até a posição n2.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO MEMMOVE
? MEMMOVE("Hello, world.", 8, 10)  && returns "wor"
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
   int SubstrLen;
   MHANDLE bufferHandle;
   char FAR *FirstDest;
   SubstrLen = parm->p[2].val.ev_long - parm->p[1].val.ev_long + 1;
   if ((bufferHandle = _AllocHand(SubstrLen + 1)) == 0)
   {
      _Error(182); // "Insufficient memory"
   }
   _HLock(bufferHandle);
   _HLock(parm->p[0].val.ev_handle);
   FirstDest = (char FAR *) _HandToPtr(parm->p[0].val.ev_handle) +
      parm->p[1].val.ev_long - 1;
   _MemMove(_HandToPtr(bufferHandle), FirstDest, SubstrLen);
   ((char FAR *) _HandToPtr(bufferHandle))[SubstrLen] = '\0';
   _RetChar(_HandToPtr(bufferHandle));
   _HUnLock(bufferHandle);
   _HUnLock(parm->p[0].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"MEMMOVE", (FPFI) Example, 3, "C,I,I"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
