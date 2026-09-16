# Rotina de biblioteca de API _NewMenu( )

Cria um novo menu do tipo de menu especificado.

```foxpro
int _NewMenu(int mtype, MENUID menuid)
int mtype;                  /* Menu type. */
MENUID menuid;            /* Menu identifier. */
```

# Observações

Você pode especificar MPOPUP ou MBAR como o parâmetro mtype. O identificador do menu deve ser exclusivo.

Use _GetNewMenuId( ) para obter um id de menu disponível. _NewMenu( ) retorna 0 se tiver sucesso ao criar um novo menu. Se não for bem-sucedido, _NewMenu( ) retorna um inteiro negativo cujo valor absoluto é um número de erro do Visual FoxPro.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir usa _NewMenu( ) para criar um menu.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO NEWMENU
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
