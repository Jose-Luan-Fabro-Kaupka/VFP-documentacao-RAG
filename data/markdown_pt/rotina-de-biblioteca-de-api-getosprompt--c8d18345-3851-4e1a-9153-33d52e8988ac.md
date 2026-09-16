# Rotina de biblioteca de API _GetOSPrompt( )

Retorna o texto de um item de menu especificado. Se o item de menu contém uma definição de tecla de acesso, o caractere e comercial também é retornado.

```foxpro
void _GetOSPrompt(MENUID menuid, ITEMID itemid, char FAR *text)
MENUID menuid;            /* ID of menu from which to get prompt */
MENUID itemuid ;            /* Index (0-based) of menu item. */
char FAR *text;               /* Text of menu command. */
```

# Observações

Pode ser usada para desenvolver aplicações com teclas de acesso independentes de idioma.

Para obter mais informações sobre como criar uma biblioteca de API e integrá-la ao Visual FoxPro, consulte Accessing the Visual FoxPro API.

# Exemplo

O exemplo a seguir retorna o texto do primeiro comando no menu File.

### Código Visual FoxPro

```foxpro
SET LIBRARY TO MENUPROMPT
```

### Código C

```foxpro
#include <pro_ext.h>
void FAR menuprompt(ParamBlk FAR *parm)
{
   char prompt[256] ;
   MenuId men ;

   men = _MenuId(_FILE);
   _GetOSPrompt(men, 0, prompt); //File New...
   _RetChar(prompt);
}
FoxInfo myFoxInfo[] = {
   {"MENUPROMPT", (FPFI) menuprompt, 0, ""}
};
FoxTable _FoxTable = {
   (FoxTable FAR *) 0, sizeof(myFoxInfo)/sizeof(FoxInfo), myFoxInfo
};
```
