# Rotina de biblioteca de API _CountItems( )

Retorna o número de títulos ou barras de menu no menu especificado.

```foxpro
int _CountItems(MENUID menuid)
MENUID menuid;            /* Menu identifier. */
```

# Exemplo

O exemplo a seguir cria um menu com três itens e chama _CountItems( ) para mostrar que a função retorna corretamente o número de itens no menu. A rotina então descarta os itens de menu e chama _CountItems( ) novamente.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO CNTITEMS
```

### Código C

```foxpro
#include <pro_ext.h>
void putLong(long n)
{
   Value val;
   val.ev_type = 'I';
   val.ev_long = n;
   val.ev_width = 10;
   _PutValue(&val);
}
FAR CountItemsEx(ParamBlk FAR *parm)
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
   _PutStr("\n_CountItems() ="); putLong(_CountItems(menuId));
   _Execute("WAIT");
   _DisposeItem(menuId, _GetItemId(menuId, 1));
   _PutStr("\n_CountItems() ="); putLong(_CountItems(menuId));
   _Execute("WAIT");
   _DisposeItem(menuId, _GetItemId(menuId, 0));
   _PutStr("\n_CountItems() ="); putLong(_CountItems(menuId));
   _Execute("WAIT");
   _DisposeMenu(menuId);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) CountItemsEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
