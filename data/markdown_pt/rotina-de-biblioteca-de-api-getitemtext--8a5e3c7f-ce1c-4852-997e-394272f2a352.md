# Rotina de biblioteca de API _GetItemText( )

Copia o texto de uma barra de menu ou título de menu para o buffer apontado por text.

```foxpro
void _GetItemText(MENUID menuid, ITEMID itemid, char FAR *text)
MENUID menuid;            /* Menu identifier. */
ITEMID itemid;            /* Menu item identifier. */
char FAR *text;            /* Buffer address for text. */
```

# Observações

O buffer deve ter pelo menos 80 bytes de comprimento.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria um menu com três itens e depois recupera o texto de cada item com _GetItemText( ).

### Código Visual FoxPro

```foxpro
SET LIBRARY TO GETITEXT
```

### Código C

```foxpro
#include <pro_ext.h>
FAR GetItemTextEx(ParamBlk FAR *parm)
{
   MENUID menuId;
   ITEMID itemId;
   Point loc;
   char FAR *itemText;
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
   if ((itemText = _Alloca(80)) == 0)
   {
      _Error(182); // "Insufficient memory"
   }
   _GetItemText(menuId, _GetItemId(menuId, 0), itemText);
   _PutStr("\nItem text of 1st item = "); _PutStr(itemText);
   _GetItemText(menuId, _GetItemId(menuId, 1), itemText);
   _PutStr("\nItem text of 2nd item = "); _PutStr(itemText);
   _GetItemText(menuId, _GetItemId(menuId, 2), itemText);
   _PutStr("\nItem text of 3rd item = "); _PutStr(itemText);
   _Execute("WAIT WINDOW");
   _DisposeMenu(menuId);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) GetItemTextEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
