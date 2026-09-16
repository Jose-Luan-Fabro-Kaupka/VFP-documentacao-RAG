# Rotina de biblioteca de API _EdSetEnv( )

Determina várias configurações do editor.

```foxpro
int _EdSetEnv(WHANDLE wh, *EDENV theEdEnv)
WHANDLE wh;            /* Handle of editing window. */
*EDENV theEdEnv;         /* Editor settings. */
```

# Observações

Para a estrutura de *EDENV, consulte _EdGetEnv( ) API Library Routine.

1 é retornado se chamado em uma sessão Command ou Editor; caso contrário, 0 é retornado.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir abre para edição um arquivo especificado por um parâmetro. Após recuar as duas primeiras linhas do arquivo, usa _EdSetEnv( ) para alterar o tamanho de uma tabulação para 6 caracteres e depois para 9 caracteres.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO EDSETENV
= EDSETENV("x")
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Example(ParamBlk FAR *parm)
{
#define pFILENAME ((char FAR *) _HandToPtr(parm->p[0].val.ev_handle))
   WHANDLE wh;
   EDENV EdEnv;
   EDPOS edpos;
   if (!_SetHandSize(parm->p[0].val.ev_handle,
      parm->p[0].val.ev_length+1))
{
      _Error(182); // "Insufficient memory"
   }
   pFILENAME[parm->p[0].val.ev_length] = '\0';
   _HLock(parm->p[0].val.ev_handle);
   wh = _EdOpenFile(pFILENAME, FO_READWRITE);
   _HUnLock(parm->p[0].val.ev_handle);
   _EdGetEnv(wh, &EdEnv);
   _EdSelect(wh, _EdGetLinePos(wh, 1), _EdGetLinePos(wh, 3));
   _EdIndent(wh, 1);
   _Execute("WAIT WINDOW 'Press any key\
      to change tabs to 6 characters.'");
   EdEnv.tabWidth = 6;
   _EdSetEnv(wh, &EdEnv);
   _Execute("WAIT WINDOW 'Press any key \
      to change tabs to 9 characters.'");
   EdEnv.tabWidth = 9;
   _EdSetEnv(wh, &EdEnv);
}
FoxInfo myFoxInfo[] = {
   {"EDSETENV", (FPFI) Example, 1, "C"},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
