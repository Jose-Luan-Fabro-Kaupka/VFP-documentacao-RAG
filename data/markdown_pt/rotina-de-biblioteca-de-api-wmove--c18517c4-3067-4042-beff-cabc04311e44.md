# Rotina de biblioteca de API _WMove( )

Move a janela especificada para o novo local especificado por pt.

```foxpro
void _WMove(WHANDLE wh, Point pt)
WHANDLE wh;            /* Handle da janela. */
Point pt;                     /* Novo local. */
```

# Observações

O parâmetro pt especifica a posição do canto superior esquerdo da janela em linhas e colunas. A nova posição pode colocar a janela parcial ou completamente fora da tela.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir move a janela ativa diagonalmente 10 linhas para baixo e 10 colunas para a direita.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WMOVE
=WMOVE()
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR WMoveEx(ParamBlk FAR *parm)
{
   WHANDLE wh = _WOnTop();
   Point newPos;
   newPos.v = _WTop(wh)  + 10;
   newPos.h = _WLeft(wh) + 10;
   _WMove(wh, newPos);
}
FoxInfo myFoxInfo[] = {
   {"WMOVE", (FPFI) WMoveEx, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
