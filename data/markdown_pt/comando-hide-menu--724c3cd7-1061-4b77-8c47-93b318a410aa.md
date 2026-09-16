# Comando HIDE MENU

Oculta uma ou mais barras de menu definidas pelo usuário ativas.

```foxpro
HIDE MENU MenuBarName1 [, MenuBarName2 ...] | ALL [SAVE]
```

#### Parâmetros
 **MenuBarName1 [, MenuBarName2 ...]**
Especifica o nome da barra de menu ou uma lista de barras de menu (separadas por vírgulas) a serem ocultadas.
**ALL**
Oculta todas as barras de menu definidas.
**SAVE**
Coloca uma imagem de uma barra de menu na tela ou em uma janela. Colocar uma imagem de uma barra de menu na tela é útil durante o desenvolvimento e teste de programas. Imagens de barras de menu podem ser removidas da janela principal do Visual FoxPro ou de uma janela definida pelo usuário com CLEAR.

# Observações

HIDE MENU remove a barra de menu especificada, um conjunto de barras de menu ou todas as barras de menu da janela principal do Visual FoxPro ou de uma janela definida pelo usuário sem remover a definição do menu da memória. Antes que uma barra de menu possa ser ocultada, ela deve primeiro ser criada com DEFINE MENU. Ocultar uma barra de menu não é o mesmo que desativá-la. Quando uma barra de menu é ocultada, ela permanece residente na memória e pode ser exibida na janela principal do Visual FoxPro ou em uma janela definida pelo usuário com ACTIVATE MENU ou SHOW MENU.
