# Rotina de biblioteca da API _WClose( )

Fecha a janela especificada e libera toda a memória associada a ela.

```foxpro
void _WClose(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Observações

Se a janela estiver sendo exibida na tela, _WClose( ) a removerá da tela.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria e exibe uma janela. Depois que o usuário pressiona uma tecla em resposta a um comando WAIT do Visual FoxPro, _WClose( ) fecha a janela.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO WCLOSE
```

### Código C

```foxpro
#include <pro_ext.h>
FAR Ex(ParamBlk FAR *parm)
{
   WHANDLE wh;
   int row, col;
   Rect r;
   wh = _WOpen(2, 2, 20, 70, 0, WINDOW_SCHEME, (Scheme FAR *) 0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   _Execute("WAIT WINDOW 'Press any key to close window'");
   _WClose(wh);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) Ex, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
