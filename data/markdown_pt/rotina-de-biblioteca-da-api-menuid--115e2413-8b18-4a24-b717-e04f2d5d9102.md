# Rotina de biblioteca da API _MenuId( )

Retorna o identificador de menu correspondente ao literal definido pelo sistema para o menu do sistema ou título de menu.

```foxpro
MENUID _MenuId(long literal)
long literal;                  /* System-defined literal. */
```

# Observações

Os literais são definidos no arquivo de inclusão da API PRO_EXT.H.

Para obter mais informações sobre como criar uma biblioteca da API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir adiciona um título de menu ao menu do sistema. Em seguida, anexa a ele um menu suspenso com dois itens. _MenuId( ) é usada para obter o MENUID do menu do sistema.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO MENUID
```

### Código C

```foxpro
#include <pro_ext.h>
MENUID SysMenuId;
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
   // Add new menu title to SYSMENU.
   SysMenuId = _MenuId(_SYSMENU);
   PadId = _GetNewItemId(SysMenuId);
   if (_NewItem(SysMenuId, PadId, _LASTITEM, "\\<Added menu title"))
   {
      _Error(623); /* "Menu item cannot be defined." */
   }
   // Define menu.
   PopupId = _GetNewMenuId();
   if (Error = _NewMenu(MPOPUP, PopupId))
   {
      _Error(-Error);
   }
   Bar1Id = _GetNewItemId(PopupId);
   // WARNING: Call _NewItem() before another _GetNewItemId().
   if (_NewItem(PopupId, Bar1Id, _LASTITEM, "\\<1st item"))
   {
      _Error(623); /* "Menu item cannot be defined." */
   }
   Bar2Id = _GetNewItemId(PopupId);
   if (_NewItem(PopupId, Bar2Id, _LASTITEM, "\\<2nd item"))
   {
      _Error(623); /* "Menu item cannot be defined." */
   }
   // Attach menu to menu title
   _SetItemSubMenu(SysMenuId, PadId, PopupId);
   // Set up selection action.
   _OnSelection(PopupId, -1, onSelection);
}
void FAR ShutDown()
{
   _DisposeItem(SysMenuId, PadId);
   _DisposeMenu(PopupId);
}
FoxInfo myFoxInfo[] = {
   {"STARTUP",   (FPFI) StartUp,   CALLONLOAD,""},
   {"SHUTDOWN",   (FPFI) ShutDown,   CALLONUNLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
