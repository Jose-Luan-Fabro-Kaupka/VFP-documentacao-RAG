# Comando SET SKIP OF

Habilita ou desabilita um menu, barra de menu, título de menu ou item de menu para menus definidos pelo usuário ou para o menu do sistema do Microsoft Visual FoxPro. Existem várias versões da sintaxe.

```foxpro
SET SKIP OF MENU MenuBarName1 lExpression1
```

```foxpro
SET SKIP OF PAD MenuTitleName OF MenuBarName2 lExpression2
```

```foxpro
SET SKIP OF POPUP MenuName1 lExpression3
```

```foxpro
SET SKIP OF BAR nMenuItemNumber | SystemItemName OF MenuName2
      lExpression4
```

#### Parâmetros
 **MENU MenuBarName1lExpression1**
Habilita ou desabilita a barra de menu do sistema do Visual FoxPro ou a barra de menu definida pelo usuário criada com DEFINE MENU. Por exemplo, a barra de menu do sistema do Visual FoxPro _MSYSMENU pode ser desabilitada com este comando: SET SKIP OF MENU _MSYSMENU .T. Ela pode ser habilitada com este comando: SET SKIP OF MENU _MSYSMENU .F.
**PAD MenuTitleName OF MenuBarName2lExpression2**
Habilita ou desabilita um título de menu do sistema do Visual FoxPro ou um título de menu definido pelo usuário criado com DEFINE PAD. Por exemplo, o título de menu Edit do Visual FoxPro pode ser desabilitado com este comando: SET SKIP OF PAD _MSM_EDIT OF _MSYSMENU .T. O título de menu pode ser habilitado com este comando: SET SKIP OF PAD _MSM_EDIT OF _MSYSMENU .F.
**POPUP MenuName1 lExpression3**
Habilita ou desabilita um menu do sistema do Visual FoxPro ou um menu definido pelo usuário criado com DEFINE POPUP. Por exemplo, o menu Edit do Visual FoxPro pode ser desabilitado com este comando: SET SKIP OF POPUP _MEDIT .T. O menu pode ser habilitado com este comando: SET SKIP OF POPUP _MEDIT .F.
**BAR nMenuItemNumber | SystemItemName OF MenuName2lExpression4**
Habilita ou desabilita um item de menu em um menu do sistema do Visual FoxPro ou um item de menu definido pelo usuário criado com DEFINE BAR. Por exemplo, o comando New no menu File do Visual FoxPro pode ser desabilitado com este comando: SET SKIP OF BAR _MFI_NEW OF _MFILE .T. onde SystemItemName especifica o comando de menu _MFI_NEW , MenuName2 especifica o menu _MFILE , e lExpression4 especifica a expressão lógica .T. . O comando de menu pode ser habilitado com este comando: SET SKIP OF BAR _MFI_NEW OF _MFILE .F. Use nMenuItemNumber para especificar um item de menu criado com DEFINE BAR.

# Observações

Para uma listagem completa dos nomes internos dos componentes do menu do sistema do Visual FoxPro, consulte Nomes do menu do sistema. Você também pode usar SYS(2013) para retornar os nomes internos do menu do sistema.

Se a expressão lógica lExpression for avaliada como verdadeira (.T.), o menu, a barra de menu, o nome do menu ou o item de menu incluído em SET SKIP OF é desabilitado, aparece esmaecido e não pode ser selecionado. Se lExpression for avaliada como falsa (.F.), o menu, a barra de menu, o nome do menu ou o item de menu é habilitado e pode ser selecionado.
