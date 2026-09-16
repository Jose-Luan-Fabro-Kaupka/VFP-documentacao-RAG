# Rotina de biblioteca de API _DisposeMenu( )

Libera o menu especificado e todos os seus itens e libera toda a memória associada a esse menu.

```foxpro
void _DisposeMenu(MENUID menuid)
MENUID menuid;            /* Menu identifier. */
```

# Observações

_DisposeMenu( ) não libera nenhum submenu associado ao menu.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir chama _DisposeMenu( ) depois que o usuário escolhe um item de menu.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO DISPMENU
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
FAR onSelection(long menuId, long itemId)
{
   _PutStr("\nitemId = "); putLong(itemId);
   _DisposeMenu(menuId);
}
FAR activateMenu(ParamBlk FAR *parm)
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
   _OnSelection(menuId, -1, onSelection);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) activateMenu, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
