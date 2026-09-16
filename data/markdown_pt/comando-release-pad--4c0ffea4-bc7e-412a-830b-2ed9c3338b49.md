# Comando RELEASE PAD

Remove um título de menu específico ou todos os títulos de menu da memória.

```foxpro
RELEASE PAD MenuTitleName OF MenuBarName | ALL OF MenuBarName
```

#### Parâmetros
 **MenuTitleName OF MenuBarName**
Especifica o título de menu a remover da memória. Você pode remover um título de menu da barra de menus do sistema do Visual FoxPro especificando seu nome em MenuTitleName . Por exemplo, o comando RELEASE PAD _MEDIT OF _MSYSMENU remove o título de menu Edit da barra de menus do sistema do Visual FoxPro.
**ALL OF MenuBarName**
Especifica que todos os títulos de menu em uma barra de menus definida pelo usuário são removidos da memória. A cláusula ALL não pode ser usada para remover títulos de menu da barra de menus do sistema do Visual FoxPro.

# Exemplo

O exemplo a seguir remove o título de menu Window da barra de menus do sistema.

```foxpro
PUSH MENU _MSYSMENU
RELEASE PAD _MSM_WINDO OF _MSYSMENU  && Removes Window menu title
WAIT WINDOW 'Press a key to restore the default menu'
POP MENU _MSYSMENU  && Restore default Visual FoxPro menu system
```
