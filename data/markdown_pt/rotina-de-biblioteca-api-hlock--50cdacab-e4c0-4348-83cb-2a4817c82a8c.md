# Rotina de biblioteca API _HLock( )

Bloqueia um handle de memória para impedir que ele se mova se o Visual FoxPro exigir reorganização de memória.

```foxpro
void _HLock(MHANDLE hand)
MHANDLE hand;            /* Memory handle. */
```

# Observações

_HLock( ) não causa reorganização de memória. Desbloqueie o MHANDLE assim que o bloqueio tiver cumprido sua finalidade.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir exibe seu parâmetro de caracteres na tela. Ele usa _HandToPtr( ) para traduzir o handle de memória do parâmetro API para um ponteiro C. Como o Visual FoxPro pode decidir reorganizar a memória durante a chamada a _PutStr( ), para garantir a execução adequada, o exemplo bloqueia o handle de memória com _HLock( ). O exemplo também chama _HUnLock( ) no final, porque o desempenho do Visual FoxPro pode ser afetado negativamente por handles de memória bloqueados.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO HLOCK
= HLOCK("Hello, world.") && displays "Hello, world" on screen
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
   {"HLOCK", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
