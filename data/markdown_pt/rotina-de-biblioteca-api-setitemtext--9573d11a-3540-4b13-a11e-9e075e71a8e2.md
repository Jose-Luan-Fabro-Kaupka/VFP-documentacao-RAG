# Rotina de biblioteca API _SetItemText( )

Altera o texto exibido para o item de menu especificado.

```foxpro
void _SetItemText(MENUID menuid, ITEMID itemid, char FAR *text)
MENUID menuid;            /* Menu identifier. */
ITEMID itemid;            /* Menu item identifier. */
char FAR *text;            /* Text. */
```

# Observações

O item de menu pode ser um título de menu ou uma barra.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir constrói um menu com três itens. Em seguida, altera o texto do item usando _SetItemText( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO SETITEXT
```

### Código C

```foxpro
#include <pro_ext.h>
FAR SetItemTextEx(ParamBlk FAR *parm)
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
   _Execute("WAIT WINDOW 'Original item text'");
   _SetItemText(menuId, _GetItemId(menuId, 0),
      "This was the 1st item");
   _SetItemText(menuId, _GetItemId(menuId, 1),
      "This was the 2nd item");
   _SetItemText(menuId, _GetItemId(menuId, 2),
      "This was the 3rd item");
   _Execute("WAIT WINDOW 'New item text'");
   _DisposeMenu(menuId);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) SetItemTextEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
