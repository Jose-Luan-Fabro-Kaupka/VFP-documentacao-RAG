# Comando HIDE POPUP

Oculta um ou mais menus ativos criados com DEFINE POPUP.

```foxpro
HIDE POPUP MenuName1 [, MenuName2 ...] | ALL [SAVE]
```

#### Parâmetros
 **MenuName1 [, MenuName2 ...]**
Especifica o nome do menu ou uma lista de menus (separados por vírgulas) a serem ocultados.
**ALL**
Oculta todos os menus definidos.
**SAVE**
Coloca uma imagem de um menu na janela principal do Visual FoxPro ou em uma janela definida pelo usuário. Colocar uma imagem de um menu na tela é útil durante o desenvolvimento e teste de programas. Imagens de menu podem ser removidas da janela principal do Visual FoxPro ou de uma janela definida pelo usuário com CLEAR.

# Observações

HIDE POPUP remove o menu especificado, um conjunto de menus ou todos os menus da janela principal do Visual FoxPro ou de uma janela definida pelo usuário sem remover as definições de menu da memória. Antes que um menu possa ser ocultado, ele deve primeiro ser criado com DEFINE POPUP. Ocultar um menu não é o mesmo que desativá-lo. Quando um menu é ocultado, ele permanece residente na memória e pode ser exibido na janela principal do Visual FoxPro ou em uma janela definida pelo usuário com ACTIVATE POPUP ou SHOW POPUP.
