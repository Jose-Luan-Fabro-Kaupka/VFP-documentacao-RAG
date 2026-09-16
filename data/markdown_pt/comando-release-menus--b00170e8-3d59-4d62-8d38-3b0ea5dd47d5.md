# Comando RELEASE MENUS

Remove barras de menu definidas pelo usuário da memória.

```foxpro
RELEASE MENUS [MenuBarNameList [EXTENDED]]
```

#### Parâmetros
 **MenuBarNameList**
Especifica as barras de menu a serem liberadas da memória. Separe os nomes das barras de menu com vírgulas.
**EXTENDED**
Libera uma barra de menu e todos os seus submenus, títulos de menu, itens de menu e todos os comandos ON SELECTION BAR, ON SELECTION MENU, ON SELECTION PAD e ON SELECTION POPUP associados.

# Observações

Uma barra de menu ativa deve primeiro ser desativada com DEACTIVATE MENU antes de poder ser liberada da memória.

Se RELEASE MENUS for emitido sem argumentos adicionais, todas as barras de menu definidas pelo usuário são removidas da memória.
