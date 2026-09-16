# Rotina de biblioteca de API _WMoveP( )

Move a janela especificada para um novo local especificado por pt.

```foxpro
void _WMoveP(WHANDLE wh, Point pt)
WHANDLE wh;            /* Window handle. */
Point pt;                     /* New location. */
```

# Observações

O parâmetro pt especifica o local do canto superior esquerdo da janela em pixels. A nova posição pode colocar a janela parcial ou completamente fora da tela.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir move a janela ativa diagonalmente 40 pixels para baixo e 40 pixels para a direita.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO WMOVEP
=WMOVEP()
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR WMovePEx(ParamBlk FAR *parm)
{
   WHANDLE wh = _WOnTop();
   Point newPos;
   newPos.v = _WTopP(wh)  + 40;
   newPos.h = _WLeftP(wh) + 40;
   _WMoveP(wh, newPos);
}
FoxInfo myFoxInfo[] = {
   {"WMOVEP", WMovePEx, 0, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
