# Rotina de biblioteca de API _DisposeItem( )

Libera da memória o item de menu especificado e libera todo o armazenamento de memória associado a este item.

```foxpro
void _DisposeItem(MENUID menuid, ITEMID itemid)
MENUID menuid;            /* Menu identifier. */
ITEMID itemid;            /* Menu item identifier. */
```

# Observações

_DisposeItem( ) não libera nenhum submenu associado ao item.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria um menu com três itens e usa _DisposeItem( ) para remover dois dos itens.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DISPITEM
```

### Código C

```foxpro
#include <pro_ext.h>
FAR DisposeItemEx(ParamBlk FAR *parm)
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
   _ActivateMenu(menuId);
   _Execute("WAIT WINDOW 'Menu has three items'");
   _DisposeItem(menuId, _GetItemId(menuId, 1));
   _Execute("WAIT WINDOW 'Menu has two items'");
   _DisposeItem(menuId, _GetItemId(menuId, 0));
   _Execute("WAIT WINDOW 'Menu has one item'");
   _DisposeMenu(menuId);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) DisposeItemEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
