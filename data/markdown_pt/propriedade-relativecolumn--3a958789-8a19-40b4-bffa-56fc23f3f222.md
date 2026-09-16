# Propriedade RelativeColumn

Especifica a coluna ativa na parte visível de um controle Grid. Não disponível em tempo de design e somente leitura em tempo de execução.

```foxpro
Grid.RelativeColumn[ = nColumn]
```

# Valor de retorno
 **nColumn**
Especifica a coluna ativa em um controle Grid.

# Observações

Aplica-se a: controle Grid

Use a propriedade RelativeColumn para determinar a posição relativa da coluna ativa em uma grade. Por exemplo, se você rolar uma grade de modo que a primeira coluna não esteja mais visível, mas a coluna ativa seja a primeira coluna visível na grade, RelativeColumn é definido como 1. Para determinar a posição absoluta da coluna ativa em uma grade, use a propriedade ActiveColumn.
