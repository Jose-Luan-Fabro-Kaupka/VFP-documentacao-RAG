# Comando RELEASE POPUPS

Remove um menu específico ou todos os menus da memória.

```foxpro
RELEASE POPUPS [MenuNameList [EXTENDED]]
```

#### Parâmetros
 **MenuNameList**
Especifica os menus a serem liberados da memória. Separe os nomes dos menus com vírgulas. Menus do sistema do Visual FoxPro que aparecem sob a barra de menu do sistema do Visual FoxPro também podem ser liberados. Para liberar um menu do sistema do Visual FoxPro, inclua o nome interno do menu do sistema (_MFILE, _MEDIT, _MDATA e assim por diante). Use SET SYSMENU TO DEFAULT para restaurar a barra de menu do sistema padrão e os menus do sistema.
**EXTENDED**
Libera um menu, seus itens e todos os comandos associados a ON SELECTION POPUP e ON SELECTION BAR.

# Observações

Um menu ativo deve ser desativado com DEACTIVATE POPUP antes de poder ser liberado da memória.

Se RELEASE POPUPS for emitido sem argumentos adicionais, todos os menus definidos pelo usuário são removidos da memória.
