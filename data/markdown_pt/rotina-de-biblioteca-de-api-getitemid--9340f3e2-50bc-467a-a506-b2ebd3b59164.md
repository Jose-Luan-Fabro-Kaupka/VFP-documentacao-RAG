# Rotina de Biblioteca de API _GetItemId( )

Retorna o identificador do item do item especificado no menu especificado.

```foxpro
ITEMID _GetItemId(MENUID menuid, long index)
MENUID menuid;            /* Menu identifier. */
long index;                  /* Menu item number. */
```

# Observações

Você pode usar _GetItemId( ) para reunir identificadores de barra de menu ou menu, para que possa realizar uma operação em todos os itens. _GetItemId( ) retorna 0 quando index excede o número de itens no menu.

Para mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria um menu com três itens. Ele usa _GetItemId( ) para obter o ITEMID de cada item de menu. Depois de remover um item do menu, você pode ver que o ITEMID não é sempre igual ao índice do item.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO GETIID
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
FAR GetItemIdEx(ParamBlk FAR *parm)
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
   _PutStr("\nitemid for index 0 ="); putLong(_GetItemId(menuId, 0));
   _PutStr("\nitemid for index 1 ="); putLong(_GetItemId(menuId, 1));
   _PutStr("\nitemid for index 2 ="); putLong(_GetItemId(menuId, 2));
   _Execute("WAIT WINDOW");
   _DisposeItem(menuId, _GetItemId(menuId, 1));
   _PutStr("\nitemid for index 0 ="); putLong(_GetItemId(menuId, 0));
   _PutStr("\nitemid for index 1 ="); putLong(_GetItemId(menuId, 1));
   _Execute("WAIT WINDOW");
   _DisposeMenu(menuId);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) GetItemIdEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
