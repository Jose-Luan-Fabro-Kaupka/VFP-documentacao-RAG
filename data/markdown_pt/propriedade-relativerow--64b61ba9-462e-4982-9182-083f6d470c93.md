# Propriedade RelativeRow

Contém a linha ativa na porção visível de um controle Grid. Não disponível em tempo de design e somente leitura em tempo de execução.

```foxpro
Grid.RelativeRow
```

# Valor de retorno
 **nRow**
Tipo de dados numérico. RelativeRow contém o número da linha ativa em um controle Grid.

# Observações

Aplica-se a: Controle Grid

Você pode usar RelativeRow para determinar a posição relativa da linha ativa em uma grade. Por exemplo, se você rolar uma grade para que a primeira linha não esteja mais visível, mas a linha ativa seja a primeira linha visível na grade, RelativeRow é definido como 1.

Para determinar a posição absoluta da linha ativa em uma grade, use a propriedade ActiveRow.
