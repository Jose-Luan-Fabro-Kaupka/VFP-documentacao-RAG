# Rotina de biblioteca de API _SetMenuPointP( )

Especifica em pixels a posição na tela do canto superior esquerdo, loc, de um menu.

```foxpro
void _SetMenuPointP(MENUID menuid, Point loc)
MENUID menuid;            /* Menu identifier. */
Point loc;                  /* Position of upper left corner
 of the menu. */
```

# Observações

Normalmente, um menu é posicionado automaticamente com base em seu tamanho e em como o usuário o invocou. Esta rotina é fornecida para substituir o posicionamento automático.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria um menu e depois o ativa em três posições diferentes na tela especificadas por _SetMenuPointP( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO SETMNPTP
```

### Código C

```foxpro
#include <pro_ext.h>
FAR SetMenuPointPEx(ParamBlk FAR *parm)
{
   MENUID menuId;
   ITEMID itemId;
   Point loc;
   menuId = _GetNewMenuId();
   _NewMenu(MPOPUP, menuId);
   itemId = _GetNewItemId(menuId);
   _NewItem(menuId, itemId, -2, "\\<1st item");
   itemId = _GetNewItemId(menuId);
   _NewItem(menuId, itemId, -2, "\\<2nd item");
   itemId = _GetNewItemId(menuId);
   _NewItem(menuId, itemId, -2, "\\<3rd item");
   loc.v = 40; loc.h = 80;
   _SetMenuPointP(menuId, loc);
   _MenuInteract(&menuId, &itemId);
   loc.v = 80; loc.h = 160;
   _SetMenuPointP(menuId, loc);
   _MenuInteract(&menuId, &itemId);
   loc.v = 160; loc.h = 320;
   _SetMenuPointP(menuId, loc);
   _MenuInteract(&menuId, &itemId);
   _DisposeMenu(menuId);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", SetMenuPointPEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
