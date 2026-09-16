# Como: exibir registros em ordem decrescente

O Visual FoxPro exibe registros em ordem crescente por padrão. Você pode criar índices decrescentes ou inverter a ordem ao exibir uma tabela.

> **Observação:** Não é possível alterar a ordem com índices binários.

### Para criar índices em ordem decrescente
- Abra o Table Designer e escolha a guia Indexes.
- Na coluna Order do índice, clique na seta para que aponte para baixo.

### Para exibir registros programaticamente em ordem decrescente
- Inclua DESCENDING nos comandos INDEX, SET ORDER, SET INDEX ou USE.

Os comandos também aceitam ASCENDING.

```foxpro
OPEN DATABASE (HOME(2) + 'Data\TestData')
USE Products
INDEX ON Unit_Price TAG Unit_Price DESCENDING
BROWSE
```

Para um índice existente:

```foxpro
USE Products
INDEX ON Unit_Price TAG Unit_Price
```

Exiba-o em ordem decrescente:

```foxpro
USE Products
SET ORDER TO Unit_Price DESCENDING
BROWSE
```
