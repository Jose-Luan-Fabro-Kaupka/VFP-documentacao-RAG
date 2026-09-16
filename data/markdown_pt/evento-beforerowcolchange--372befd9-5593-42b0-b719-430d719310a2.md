# Evento BeforeRowColChange

Ocorre quando o usuário altera a linha ou coluna ativa antes que a nova célula receba o foco. Também ocorre antes do evento Valid do objeto atual na coluna da grade e de quaisquer regras no banco de dados. Use NODEFAULT para impedir que a linha e a coluna ativas na grade sejam alteradas.

```foxpro
PROCEDURE Grid.BeforeRowColChange
LPARAMETERS nColIndex
```

#### Parâmetros
 **nColIndex**
Retorna o índice da coluna que está ativa antes da alteração de linha ou coluna.

# Observações

Aplica-se a: Grid Control

BeforeRowColChange é acionado interativamente usando o mouse ou o teclado ou programaticamente, como ao chamar o método ActivateCell.

Você pode consultar a propriedade RowColChange neste evento para determinar o tipo de alteração que acionou o evento.
