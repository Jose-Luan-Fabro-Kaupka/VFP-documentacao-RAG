# Rotina de biblioteca de API _DeActivateMenu( )

Remove um menu da tela.

```foxpro
void _DeActivateMenu(MENUID menuid)
MENUID menuid;            /* Menu identifier. */
```

# Observações

O menu não é liberado da memória e pode ser reativado com _ActivateMenu( ).

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir ativa e desativa um menu várias vezes.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DEACTMEN
```

### Código C

```foxpro
#include <pro_ext.h>
FAR DeActMenuEx(ParamBlk FAR *parm)
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
   _Execute("WAIT WINDOW 'Menu activated'");
   _DeActivateMenu(menuId);
   _Execute("WAIT WINDOW 'Menu deactivated'");
   _ActivateMenu(menuId);
   _Execute("WAIT WINDOW 'Menu activated'");
   _DeActivateMenu(menuId);
   _Execute("WAIT WINDOW 'Menu deactivated'");
   _DisposeMenu(menuId);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) DeActMenuEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
