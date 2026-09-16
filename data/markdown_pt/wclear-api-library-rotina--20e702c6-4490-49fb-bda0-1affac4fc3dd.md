# _WClear( ) API Library Rotina

Apaga o conteúdo da janela especificada alterando a área de conteúdo para a cor de fundo padrão.

```foxpro
void _WClear(WHANDLE wh)
WHANDLE wh;            /* Window handle. */
```

# Observações
A posição lógica do cursor permanece inalterada.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Acessando o Visual FoxPro API.

# Exemplo
O exemplo a seguir cria uma janela e a preenche com Xs. Quando o usuário pressiona uma tecla em resposta a um comando WAIT do Visual FoxPro, _WClear( ) limpa a janela.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WCLEAR
```

### C Código

```foxpro
#include <pro_ext.h>
FAR WClearEx(ParamBlk FAR *parm)
{
   WHANDLE wh;
   int row, col;
   wh = _WOpen(2,2,20,70,WEVENT | CLOSE,WINDOW_SCHEME,(Scheme FAR *) 0,
      WO_SYSTEMBORDER);
   _WShow(wh);
   for (row = 0; row < _WHeight(wh); row++)
   {
      for (col = 0; col < _WWidth(wh); col++)
      {
         _WPutChr(wh, 'X');
      }
      _WPutChr(wh, '\n');
   }
   _Execute("WAIT WINDOW 'Press any key to clear window'");
   _WClear(wh);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) WClearEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
