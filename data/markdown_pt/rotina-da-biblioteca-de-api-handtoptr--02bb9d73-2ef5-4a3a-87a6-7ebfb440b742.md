# Rotina da biblioteca de API _HandToPtr( )

Converte um identificador de memória em um ponteiro FAR (32 bits), que aponta para a memória alocada para esse identificador.

```foxpro
void FAR * _HandToPtr(MHANDLE hand)
MHANDLE hand;            /* Memory handle. */
```

# Observações

O Visual FoxPro pode reorganizar a memória sempre que o controle é passado para ele ou para outra rotina fora do módulo atual.

> **Observação:** _HandToPtr() não causa reorganização da memória. O ponteiro retornado por _HandToPtr() pode se tornar inválido sempre que o controle for devolvido ao Visual FoxPro, a menos que o MHANDLE esteja bloqueado. Não mantenha ponteiros para identificadores de memória desbloqueados entre chamadas de função externa, a menos que esteja documentado que a chamada não causa reorganização da memória.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir exibe seu parâmetro de caracteres na tela. Ele usa _HandToPtr( ) para converter o identificador de memória do parâmetro da API em um ponteiro C.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO HANDTOPT
= HANDTOPTR("Hello, world.")  && displays "Hello, world" on screen
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
