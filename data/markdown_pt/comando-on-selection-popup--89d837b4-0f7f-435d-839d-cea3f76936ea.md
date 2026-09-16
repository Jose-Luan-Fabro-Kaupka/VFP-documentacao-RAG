# Comando ON SELECTION POPUP

Especifica um comando que é executado quando você escolhe qualquer item de menu de um menu especificado ou de todos os menus.

```foxpro
ON SELECTION POPUP MenuName | ALL [Command]
```

#### Parâmetros
 **MenuName**
Especifica o menu ao qual o comando é atribuído.
**ALL**
Se você incluir ALL em vez de um nome de menu, o Visual FoxPro executa o comando quando você escolhe um item de menu de qualquer menu.
**Command**
Especifica o comando a executar quando você escolhe um item de menu.

# Observações

Quando você escolhe qualquer item de menu de um menu, o Visual FoxPro executa o comando que você especifica com ON SELECTION POPUP. Ao criar e ativar o menu, coloque ON SELECTION POPUP entre DEFINE POPUP e ACTIVATE POPUP.

Use ON SELECTION BAR para executar um comando quando você escolhe um item de menu específico. ON SELECTION BAR tem precedência sobre ON SELECTION POPUP. Use ON BAR para ativar um menu ou barra de menu quando você escolhe um item de menu específico.

Use ON SELECTION POPUP sem um comando para liberar um comando atribuído a um item de menu com um ON SELECTION POPUP anterior.
