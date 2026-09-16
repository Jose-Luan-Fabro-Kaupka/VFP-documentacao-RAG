# Comando ON PAD

Especifica o menu ou a barra de menu que é ativada quando você escolhe um título de menu específico.

```foxpro
ON PAD MenuTitleName OF MenuBarName1   [ACTIVATE POPUP MenuName
   | ACTIVATE MENU MenuBarName2
```

#### Parâmetros
 **MenuTitleName OF MenuBarName1**
Especifica o título de menu ao qual um menu ou barra de menu é atribuído.
**ACTIVATE POPUP MenuName**
Especifica o menu a ser ativado quando o título de menu é escolhido. Use ON PAD MenuTitleName OF MenuBarName1 sem ACTIVATE POPUP para liberar um menu de um título de menu. Se você especificar a barra de menu do sistema _MSYSMENU para MenuBarName1, MenuName não pode especificar um menu criado com a cláusula PROMPT do comando DEFINE POPUP.
**ACTIVATE MENU MenuBarName2**
Especifica o nome da barra de menu a ser ativada quando o título de menu é escolhido. Use ON PAD MenuTitleName OF MenuBarName1 sem ACTIVATE MENU para liberar uma barra de menu de um nome de menu.

# Observações

Use ON SELECTION PAD para executar um comando quando um título de menu é escolhido.
