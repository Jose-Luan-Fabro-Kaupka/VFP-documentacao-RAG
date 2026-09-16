# Rotina de biblioteca de API _NewItem( )

Adiciona um item com o identificador itemid especificado ao menu especificado por menuid.

```foxpro
int _NewItem(MENUID menuid, ITEMID itemid, ITEMID
beforeid, char FAR *prompt)
MENUID menuid;            /* Menu identifier. */
ITEMID itemid;            /* New item identifier. */
ITEMID beforeid;            /* Identifier of item the new item
 precedes. */
char FAR *prompt;         /* Text for new menu item. */
```

# Observações

O tipo do novo item de menu é automaticamente um título de menu ou uma barra, dependendo do tipo de menu no qual o item está sendo inserido.

O parâmetro beforeid especifica o identificador do item que o novo item deve preceder. Especifique beforeid como – 1 para especificar que o novo item será o primeiro item na lista, ou como -2 para especificar que o item deve ser adicionado ao final da lista. O prompt especifica o texto do novo item de menu. _NewItem( ) retorna 0 se tiver sucesso ao adicionar um item, ou – 1 se não tiver.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir constrói um menu com três itens. Ele usa _NewItem( ) para adicionar cada item ao menu.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO NEWITEM
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
   _NewItem(menuId, itemId, -2, "\\<2nd item");
   itemId = _GetNewItemId(menuId);
   _NewItem(menuId, itemId, -1, "\\<1st item");
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
