# Exemplo de indexação de expressões

Arquivo: ...\Samples\Solution\Db\Index2.scx

Este exemplo de índice mostra várias opções que você pode considerar ao usar um campo de caracteres para representar uma ID exclusiva (geralmente composta de dados numéricos). Uma marca de índice baseada em um campo de caracteres será classificada de acordo com os valores ASCII dos dados, enquanto uma expressão numérica, usando a função VAL( ), será classificada por sequências numéricas. A tabela a seguir mostra a diferença de classificação entre dois índices:

| cExpression | VAL( cExpression ) |
| --- | --- |
| 1 | 1 |
| 11 | 2 |
| 2 | 11 |

> **Observação:** Quando você usa a função VAL( ), todos os valores não numéricos são convertidos em 0.

Ao incorporar a função BINTOC( ), você também pode reduzir consideravelmente o tamanho das marcas de índice.
