# Rotina de biblioteca de API _EdOpenFile( )

Abre o arquivo especificado em uma janela, para iniciar uma sessão de edição.

```foxpro
WHANDLE _EdOpenFile(TEXT *filename, int mode)
TEXT *filename;            /* File to open. */
int mode;                     /* Mode option. */
```

# Observações

As seguintes opções de modo estão disponíveis: FO_READONLY, FO_WRITEONLY e FO_READWRITE.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir abre uma sessão de editor para um arquivo especificado por um parâmetro.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDOPEN
= EDOPEN("x")  && opens editor session for file "x"
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
   {
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
}
FoxInfo myFoxInfo[] = {
   {"EDOPEN", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
