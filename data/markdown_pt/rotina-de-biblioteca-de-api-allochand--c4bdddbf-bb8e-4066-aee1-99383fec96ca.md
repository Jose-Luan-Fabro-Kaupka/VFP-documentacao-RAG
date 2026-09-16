# Rotina de biblioteca de API _AllocHand( )

Retorna um novo MHANDLE de tamanho hsize.

```foxpro
MHANDLE _AllocHand(unsigned int hsize)
unsigned int hsize;            /* Size of new memory handle in bytes. */
```

# Observações

_AllocHand( ) retorna 0 quando não há memória suficiente para atender à solicitação. A memória alocada com _AllocHand( ) não é inicializada e deve ser liberada após o uso.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

No exemplo a seguir, um caractere é replicado na memória fornecida por _AllocHand( ). A função de API REPLTOMH( ) abaixo retorna o identificador de memória ao Visual FoxPro. No Visual FoxPro, o identificador de memória é passado para funções de API que esperam um argumento de identificador de memória (passado como inteiro, "I").

### Código Visual FoxPro

```foxpro
SET LIBRARY TO ALLOCHAN
mh = REPLTOMH("x", 120)
? MHTOFOX(mh)
? LEN(MHTOFOX(mh))
? MHTOFOX(mh)
= FREEMH(mh)
```

### Código C

```foxpro
#include <pro_ext.h>
//   Replicate char argument to memory allocated with _AllocHand().
//   Return the memory handle to Visual FoxPro.
void FAR replToMH(ParamBlk FAR *parm)
{
   char FAR *rep;
   char c = *(char *) _HandToPtr(parm->p[0].val.ev_handle);
   MHANDLE mh;
   if ((mh = _AllocHand((int) parm->p[1].val.ev_long + 1)) == 0)
   {
      _Error(182);  // "Insufficient memory"
   }
   _HLock(mh);
   rep = _HandToPtr(mh);
   _MemFill(rep, c, (int) parm->p[1].val.ev_long);
   rep[parm->p[1].val.ev_long] = '\0';  // null terminate
   _HUnLock(mh);
   _RetInt(mh, 10);
}
//   Returns characters in memory handle.
//   Argument in call from Visual FoxPro
//   must be a valid Visual FoxPro memory handle.
void FAR MHToFoxString(ParamBlk FAR *parm)
{
   char FAR *string;
   MHANDLE mh = parm->p[0].val.ev_long;
   _HLock(mh);
   string = _HandToPtr(mh);
   _RetChar(string);
   _HUnLock(mh);
}
//   Frees memory handle.  Argument in call from
//   Visual FoxPro must be a valid
//   Visual FoxPro memory handle.
void FAR freeMH(ParamBlk FAR *parm)
{
   _FreeHand((MHANDLE) parm->p[0].val.ev_long);
}
FoxInfo myFoxInfo[] = {
   {"REPLTOMH", (FPFI) replToMH, 2, "C,I"},
   {"MHTOFOX", (FPFI) MHToFoxString, 1, "I"},
   {"FREEMH", (FPFI) freeMH, 1, "I"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
