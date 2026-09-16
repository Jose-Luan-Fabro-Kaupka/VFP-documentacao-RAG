# Rotina de biblioteca de API _SetItemCmdKey( )

Define tanto o atalho de teclado para o item de menu especificado quanto o texto exibido para o atalho de teclado.

```foxpro
void _SetItemCmdKey(MENUID menuid, ITEMID itemid, int key,
 char FAR *text)
MENUID menuid;            /* Menu identifier. */
ITEMID itemid;            /* Menu item identifier. */
int key;                     /* Shortcut key. */
char FAR *text;            /* Displayed text. */
```

# Observações

Se você não deseja exibir um atalho de teclado, passe text como um ponteiro para uma cadeia de caracteres nula. Se você deseja que o sistema gere o texto exibido padrão, passe (char FAR *)0.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir configura um menu com três itens e atribui um atalho de teclado a cada item.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO SETICMDK
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
FAR SetItemCmdKeyEx(ParamBlk FAR *parm)
{
   MENUID menuId;
   ITEMID itemId;
   Point loc;
   menuId = _GetNewMenuId();
   _NewMenu(MPOPUP, menuId);
   itemId = _GetNewItemId(menuId);
   _NewItem(menuId, itemId, -2, "\\<1st item");
   _SetItemCmdKey(menuId, itemId, altKey
0x178, "Alt+1");
   itemId = _GetNewItemId(menuId);
   _NewItem(menuId, itemId, -2, "\\<2nd item");
   _SetItemCmdKey(menuId, itemId, altKey
0x179, "Alt+2");
   itemId = _GetNewItemId(menuId);
   _NewItem(menuId, itemId, -2, "\\<3rd item");
   _SetItemCmdKey(menuId, itemId, altKey
0x17a, "Alt+3");
   loc.v = 10; loc.h = 20;
   _SetMenuPoint(menuId, loc);
   _ActivateMenu(menuId);
   _OnSelection(menuId, -1, onSelection);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) SetItemCmdKeyEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
