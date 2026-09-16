# Rotina de biblioteca de API _GetItemCmdKey( )

Copia a cadeia de caracteres do atalho de teclado exibido para o item de menu especificado para o buffer apontado pelo parâmetro text.

```foxpro
int _GetItemCmdKey(MENUID menuid, ITEMID itemid, char FAR *text)
MENUID menuid;            /* Menu identifier. */
ITEMID itemid;            /* Menu item identifier. */
char FAR *text;            /* Where to store the shortcut string. */
```

# Observações

_GetItemCmdKey( ) retorna o código de teclado interno do atalho de teclado. Se não houver atalho de teclado para o item de menu especificado, _GetItemCmdKey( ) retornará 0.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria um menu com três itens, configurando um atalho de teclado para cada item. Ele usa _GetItemCmdKey( ) para exibir as teclas de atalho.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO GETICMDK
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
FAR GetItemCmdKeyEx(ParamBlk FAR *parm)
{
   MENUID menuId;
   ITEMID itemId;
   Point loc;
   char FAR *shortcutString;
   int intKeyCode;
   menuId = _GetNewMenuId();
   _NewMenu(MPOPUP, menuId);
   itemId = _GetNewItemId(menuId);
   _NewItem(menuId, itemId, -2, "\\<1st item");
   _SetItemCmdKey(menuId, itemId, altKey | 0x78, "Alt+1");
   itemId = _GetNewItemId(menuId);
   _NewItem(menuId, itemId, -2, "\\<2nd item");
   _SetItemCmdKey(menuId, itemId, altKey | 0x79, "Alt+2");
   itemId = _GetNewItemId(menuId);
   _NewItem(menuId, itemId, -2, "\\<3rd item");
   _SetItemCmdKey(menuId, itemId, altKey | 0x7a, "Alt+3");
   loc.v = 10; loc.h = 20;
   _SetMenuPoint(menuId, loc);
   _ActivateMenu(menuId);
   if ((shortcutString = _Alloca(64)) == 0)
   {
      _DisposeMenu(menuId);
      _Error(182); // "Insufficient memory"
   }
   intKeyCode = _GetItemCmdKey(menuId, _GetItemId(menuId, 0),
      shortcutString);
   _PutStr("\nShortcut string = "); _PutStr(shortcutString);
   _PutStr("\nInternal key code ="); putLong(intKeyCode);
   intKeyCode = _GetItemCmdKey(menuId, _GetItemId(menuId, 1),
      shortcutString);
   _PutStr("\nShortcut string = "); _PutStr(shortcutString);
   _PutStr("\nInternal key code ="); putLong(intKeyCode);
   intKeyCode = _GetItemCmdKey(menuId, _GetItemId(menuId, 2),
      shortcutString);
   _PutStr("\nShortcut string = "); _PutStr(shortcutString);
   _PutStr("\nInternal key code ="); putLong(intKeyCode);
   _Execute("WAIT");
   _DisposeMenu(menuId);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) GetItemCmdKeyEx, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
