# Rotina de biblioteca API _EdDelete( )

Exclui a parte selecionada do arquivo na janela de edição especificada.

```foxpro
void _EdDelete(WHANDLE wh)
WHANDLE wh;            /* Handle of editing window. */
```

# Observações

Se nada estiver selecionado, _EdDelete( ) exclui o caractere na posição atual do ponto de inserção.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro e exclui o primeiro caractere no arquivo usando _EdDelete( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDDELETE
= EDDELETE("x")
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   int retValue;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdSelect(wh, 0, 1);
   _EdDelete(wh);
}
FoxInfo myFoxInfo[] = {
   {"EDDELETE", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
