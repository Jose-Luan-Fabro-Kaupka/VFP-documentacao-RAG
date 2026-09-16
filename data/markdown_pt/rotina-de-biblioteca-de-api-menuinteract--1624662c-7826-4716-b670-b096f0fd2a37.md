# Rotina de biblioteca de API _MenuInteract( )

Define itemid e menuid para indicar qual item de menu foi escolhido, se houver.

```foxpro
int _MenuInteract(MENUID FAR *menuid, ITEMID FAR *itemid)
MENUID FAR *menuid;      /* Pointer to menu identifier. */
ITEMID FAR *itemid;      /* Pointer to menu item identifier. */
```

# Observações

Se o usuário escolher qualquer item de menu, _MenuInteract( ) retornará 1. Se nenhum item for escolhido (por exemplo, se o usuário pressionar ESC), _MenuInteract( ) retornará 0.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria um menu com três itens e exige que o usuário interaja com o menu chamando _MenuInteract( ).

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO MENUINTE
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
