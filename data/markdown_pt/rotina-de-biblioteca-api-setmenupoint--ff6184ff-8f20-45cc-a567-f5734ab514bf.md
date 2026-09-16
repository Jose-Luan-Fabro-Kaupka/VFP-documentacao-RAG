# Rotina de biblioteca API _SetMenuPoint( )

Especifica a posição na tela do canto superior esquerdo, loc, de um menu.

```foxpro
void _SetMenuPoint(MENUID menuid, Point loc)
MENUID menuid;            /* Menu identifier. */
Point loc;                  /* Position of upper-left corner
 of the menu. */
```

# Observações

Normalmente, um menu é posicionado automaticamente com base em seu tamanho e em como o usuário o invocou. Esta rotina é fornecida para substituir o posicionamento automático.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

Um menu é criado e depois ativado em três posições diferentes na tela especificadas por _SetMenuPoint( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO SETMNPNT
```

### Código C

```foxpro
#include <pro_ext.h>
FAR SetMenuPointEx(ParamBlk FAR *parm)
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
   loc.v = 10; loc.h = 20;
   _SetMenuPoint(menuId, loc);
   _MenuInteract(&menuId, &itemId);
   loc.v = 15; loc.h = 30;
   _SetMenuPoint(menuId, loc);
   _MenuInteract(&menuId, &itemId);
   loc.v = 20; loc.h = 40;
   _SetMenuPoint(menuId, loc);
   _MenuInteract(&menuId, &itemId);
   _DisposeMenu(menuId);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) SetMenuPointEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
