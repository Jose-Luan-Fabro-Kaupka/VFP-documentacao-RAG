# Comando ON SELECTION BAR

Especifica um comando que é executado quando você escolhe um item de menu específico.

```foxpro
ON SELECTION BAR nMenuItemNumber OF MenuName   [Command]
```

#### Parâmetros
 **nMenuItemNumber OF MenuName [ Command ]**
Especifica o número da barra do item de menu, o nome do menu e o comando a ser executado para o item de menu especificado.

# Observações

Normalmente, ON SELECTION BAR usa DO para executar um procedimento ou programa. Quando você cria e ativa um menu, coloque ON SELECTION BAR entre DEFINE POPUP e ACTIVATE POPUP.

Você também pode usar ON SELECTION BAR com um menu de sistema do Visual FoxPro.

Use ON SELECTION POPUP para executar um comando quando você escolhe qualquer item de menu em um menu. Use ON BAR para ativar um menu ou barra de menu quando você escolhe um item de menu específico.

Use ON SELECTION BAR nMenuItemNumber OF MenuName sem um comando para liberar um comando atribuído a um item de menu.
