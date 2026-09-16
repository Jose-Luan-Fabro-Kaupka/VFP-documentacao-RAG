# Rotina de biblioteca de API _GetItemSubMenu( )

Retorna o identificador do item de menu de um submenu atribuído a um item de menu.

```foxpro
MENUID _GetItemSubMenu(MENUID menuid, ITEMID itemid);
MENUID menuid;            /* Menu identifier */
ITEMID itemid;            /* Menu item identifier*/
```

# Observações

Um submenu é tratado como um menu independente. _GetItemSubMenu( ) retorna o MENUID do submenu atribuído a um item de menu especificado, ou – 1 se não houver submenu atribuído ao item de menu.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir cria um sistema de menu e retorna o ID do submenu.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO GETITEMS
```

### Código C

```foxpro
#include <pro_ext.h>
MENUID SysMenuId, retMenuId;
MENUID PopupId;
ITEMID PadId;
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
}
void FAR StartUp()
{
      ITEMID Bar1Id;
      ITEMID Bar2Id;
    int Error;
//
//   Add new menu title to SYSMENU.
//
  SysMenuId = _MenuId(_SYSMENU);
  PadId = _GetNewItemId(SysMenuId);
   if (_NewItem(SysMenuId, PadId, _LASTITEM, "\\<Added menu title"))
  {
    _Error(623); /* "Menu item cannot be defined." */
  }
//
//   Define menu.
//
  PopupId = _GetNewMenuId();
  if (Error = _NewMenu(MPOPUP, PopupId))
  {
    _Error(-Error);
  }
   Bar1Id = _GetNewItemId(PopupId);
//
//      WARNING: Call _NewItem() before another _GetNewItemId().
//
   if (_NewItem(PopupId, Bar1Id, _LASTITEM, "\\<1st item"))
  {
    _Error(623); /* "Menu item cannot be defined." */
  }
   Bar2Id = _GetNewItemId(PopupId);
   if (_NewItem(PopupId, Bar2Id, _LASTITEM, "\\<2nd item"))
  {
    _Error(623); /* "Menu item cannot be defined." */
  }
//
//   Attach menu to menu title.
//
  _SetItemSubMenu(SysMenuId, PadId, PopupId);
  _PutStr("\nSubMenu Id = "); putLong(PopupId);
//
//  Set up selection action.
//
   retMenuId = _GetItemSubMenu(SysMenuId,PadId);
   _PutStr("\nThis is the return value from  _GetItemSubMenu.  retMenuId = "); putLong(retMenuId);
   _OnSelection(PopupId, -1, onSelection);
}
void FAR ShutDown()
{
  _DisposeItem(SysMenuId, PadId);
  _DisposeMenu(PopupId);
}
FoxInfo myFoxInfo[] =
{
   {"STARTUP",   (FPFI) StartUp,  CALLONLOAD, ""},
   {"SHUTDOWN",  (FPFI) ShutDown, CALLONUNLOAD, ""},
};
FoxTable _FoxTable =
{
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
