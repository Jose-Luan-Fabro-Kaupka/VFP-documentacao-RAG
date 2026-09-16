# Rotina de biblioteca API _GetNewMenuId( )

Retorna um identificador de menu para uso com outras funções relacionadas a menus.

```foxpro
MENUID _GetNewMenuId(void any)
void any;                     /* Pointer. */
```

# Observações

Cada menu deve ter um identificador exclusivo.

Para obter mais informações sobre como criar uma biblioteca API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir constrói um menu com três itens. Antes que o exemplo possa criar um menu usando _NewMenu( ), ele deve usar _GetNewMenuId( ) para gerar um MENUID exclusivo.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO GETNWMID
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
FAR GetNewItemId(ParamBlk FAR *parm)
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
   _PutStr("\nmenuId ="); putLong(menuId);
   _PutStr("\nitemId ="); putLong(itemId);
   _DisposeMenu(menuId);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) GetNewItemId, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
