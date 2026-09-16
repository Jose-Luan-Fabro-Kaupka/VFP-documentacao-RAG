# Rotina de biblioteca de API _EdIndent( )

Recua o texto selecionado no arquivo na janela especificada pelo número especificado de tabulações.

```foxpro
void _EdIndent(WHANDLE wh, int tabstops)
WHANDLE wh;            /* Handle of editing window. */
int tabstops;                  /* Number of tab stops. */
```

# Observações

Você pode especificar um número negativo para tabstops para causar um recuo suspenso para a seleção.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir abre uma sessão de edição para um arquivo especificado por um parâmetro e recua as linhas 13 e 15 no arquivo por uma única tabulação.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDINDENT
= EDINDENT("x")
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1)) {
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdSelect(wh, _EdGetLinePos(wh, 12), _EdGetLinePos(wh, 14));
   _EdIndent(wh, 1);
}
FoxInfo myFoxInfo[] = {
   {"EDINDENT", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
