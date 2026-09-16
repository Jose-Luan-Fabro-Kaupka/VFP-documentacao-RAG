# Rotina de biblioteca de API _GetNewItemId( )

Retorna um identificador disponível para uso como identificador de item no menu especificado.

```foxpro
ITEMID _GetNewItemId(MENUID menuid)
MENUID menuid;            /* Menu identifier. */
```

# Observações

Cada item de um menu deve ter um identificador exclusivo nesse menu.

Depois de usar _GetNewItemId( ), adicione o novo item ao menu com _NewItem( ) antes de usar _GetNewItemId( ) novamente. Se você não adicionar o item ao menu, chamadas posteriores a _GetNewItemId( ) retornarão o mesmo ITEMID.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria um menu com três itens. Antes que cada item seja adicionado ao menu, um ITEMID exclusivo é gerado pela chamada a _GetNewItemId( ).

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO GETNWIID
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
