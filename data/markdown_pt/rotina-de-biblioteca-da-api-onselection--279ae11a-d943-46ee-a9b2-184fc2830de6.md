# Rotina de biblioteca da API _OnSelection( )

Especifica uma rotina a ser executada quando o usuário escolhe o menu e o item especificados.

```foxpro
void _OnSelection(MENUID menuid, ITEMID itemid, FPFI routine)
MENUID menuid;            /* Menu identifier. */
ITEMID itemid;            /* Item identifier. */
FPFI routine;               /* Routine to execute. */
```

# Observações

Se você especificar itemid como –1, a rotina será executada quando o usuário escolher qualquer item do menu. Uma rotina associada a um item individual substitui uma associada ao menu inteiro. Para cancelar uma rotina de seleção de um menu e item especificados, passe (FPFI)0 como parâmetro routine.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Acessando a API do Visual FoxPro.

# Exemplo

O exemplo a seguir cria um menu com três itens. Ele chama _OnSelection( ) com um parâmetro ITEMID igual a –1, indicando que a função USERCHOICE( ) deve ser chamada quando o usuário escolher qualquer item desse menu.

### Código do Visual FoxPro

```foxpro
SET LIBRARY TO ONSELECT
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
FAR activateMenu(ParamBlk FAR *parm)
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
   _OnSelection(menuId, -1, onSelection);
}
FoxInfo myFoxInfo[] = {
   {"ONLOAD", (FPFI) activateMenu, CALLONLOAD, ""},
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
