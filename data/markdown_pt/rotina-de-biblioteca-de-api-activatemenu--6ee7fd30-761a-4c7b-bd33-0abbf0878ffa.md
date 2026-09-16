# Rotina de biblioteca de API _ActivateMenu( )

Exibe o menu especificado na tela e retorna o controle imediatamente à rotina chamadora.

```foxpro
void _ActivateMenu(MENUID menuid)
MENUID menuid            /* Menu identifier.
```

# Observações

Se você detectar o pressionamento de um botão do mouse ou uma tecla no menu, pode chamar _MenuInteract( ) para determinar qual item de menu o usuário escolheu.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acesso à API do Visual FoxPro.

# Exemplo

O exemplo a seguir constrói um menu com três itens. _ActivateMenu( ) exibe o menu. Este menu é não modal, pois a interação não é forçada como com _MenuInteract( ). Em vez disso, quando o usuário faz uma seleção, a rotina _OnSelection( ) é chamada, o item selecionado é impresso na tela e o menu é descartado.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO ACTIMENU
WAIT WINDOW "Make selection from menu." NOWAIT
SUSPEND
```

### Código C

```foxpro
#include <pro_ext.h>
static MENUID menuId;
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
FAR deactivateMenu(ParamBlk FAR *parm)
{
   _DeActivateMenu(menuId);
   _DisposeMenu(menuId);
}
FAR activateMenu(ParamBlk FAR *parm)
{
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
   {"ONUNLOAD", (FPFI) deactivateMenu, CALLONUNLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
