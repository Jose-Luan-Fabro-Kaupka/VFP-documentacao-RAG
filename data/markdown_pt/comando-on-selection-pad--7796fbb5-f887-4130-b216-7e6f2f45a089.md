# Comando ON SELECTION PAD

Especifica um comando que é executado quando você escolhe um título de menu específico em uma barra de menus.

```foxpro
ON SELECTION PAD MenuTitleName OF MenuBarName [Command]
```

#### Parâmetros
 **MenuTitleName OF MenuBarName**
Especifica o nome do título de menu ao qual o comando é atribuído.
**Command**
Especifica o comando Visual FoxPro a ser executado quando você escolhe o título de menu especificado.

# Observações

Quando você escolhe o título de menu especificado, o Visual FoxPro executa o comando que você especifica com ON SELECTION PAD. Normalmente, ON SELECTION PAD usa DO para executar um procedimento ou programa quando você escolhe um título de menu específico na barra de menus. Ao criar e ativar a barra de menus, coloque ON SELECTION PAD entre DEFINE MENU e ACTIVATE MENU.

Use ON SELECTION MENU para executar um comando quando você escolhe qualquer título de menu em uma barra de menus. Use ON PAD para ativar um menu ou barra de menus quando você escolhe um título de menu específico em uma barra de menus.

Use ON SELECTION PAD sem um comando para liberar um comando atribuído ao título de menu.
