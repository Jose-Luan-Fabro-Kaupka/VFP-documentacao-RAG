# Evento AfterRowColChange

Ocorre quando o usuário move para outra linha ou coluna no Grid, depois que a nova célula recebe o foco e depois do evento When do objeto na nova linha ou coluna. O evento AfterRowColChange não é disparado a menos que o evento When do objeto na nova linha ou coluna retorne true (.T.).

```foxpro
PROCEDURE Grid.AfterRowColChange
LPARAMETERS nColIndex
```

#### Parâmetros
 **nColIndex**
Retorna o índice da linha ou coluna recém-selecionada.

# Observações

Aplica-se a: Grid Control

AfterRowColChange é disparado de forma interativa pelo mouse ou teclado, ou programaticamente, como ao chamar o método ActivateCell.

Use este evento para sincronizar as duas metades de um grid quando a propriedade SplitBar = .T., adicionando This.Refresh.

Você pode consultar a propriedade RowColChange neste evento para determinar o tipo de alteração que disparou o evento.
