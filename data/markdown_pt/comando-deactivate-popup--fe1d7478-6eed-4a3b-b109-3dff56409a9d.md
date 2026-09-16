# Comando DEACTIVATE POPUP

Desativa um menu criado com DEFINE POPUP.

```foxpro
DEACTIVATE POPUP MenuName1 [, MenuName2 ...] | ALL
```

#### Parâmetros
 **MenuName1 [, MenuName2 ...]**
Especifica os nomes do menu ou dos menus a desativar. Você pode desativar um conjunto de menus incluindo uma lista de nomes de menu separados por vírgulas.
**ALL**
Desativa todos os menus ativos.

# Observações

DEACTIVATE POPUP remove um menu ativo ou um conjunto de menus da janela principal do Visual FoxPro ou de uma janela definida pelo usuário sem remover a definição do menu da memória. Um menu pode ser reativado usando ACTIVATE POPUP e o nome do menu.

Use RELEASE POPUPS com o nome do menu para liberar um menu específico ou um conjunto de menus da memória. Você pode liberar todos os menus da memória com CLEAR POPUPS ou CLEAR ALL.

O controle do programa retorna à linha imediatamente após a linha que ativou o menu, a menos que ACTIVATE POPUP NOWAIT seja usado para ativar o menu.
