# Propriedade RowColChange

Contém um valor que identifica o tipo de movimento de célula feito em uma grade. Somente leitura em tempo de design e em tempo de execução.

```foxpro
Grid.RowColChange
```

# Observações

Aplica-se a: Grid Control

O valor de RowColChange é 0 na abertura e após a atualização de uma grade. Você pode consultar esta propriedade nos eventos AfterRowColChange e BeforeRowColChange para determinar o tipo de alteração que disparou o evento, conforme a tabela a seguir.

| Value | Description |
| --- | --- |
| 0 (default) | Nenhuma alteração. |
| 1 | Alteração de linha |
| 2 | Alteração de coluna |
| 3 | Alteração de linha e coluna |
