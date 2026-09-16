# Exemplo Print a Percent of Total in a Report

Arquivo: ...\Samples\Solution\Reports\Percent.frx

O relatório de exemplo, Percent.frx, mostra uma forma de calcular e exibir valores no início do relatório antes que todos os registros da fonte de registros tenham sido impressos. Este relatório de exemplo imprime uma porcentagem baseada em um total que geralmente é calculado e impresso no final de um relatório.

O relatório de exemplo usa as tabelas EMPLOYEE e ORDERS em seu Data Environment. Uma variável pública e expressões usando o campo ORDER_AMT são usadas para calcular as porcentagens.

Para classificar os dados adequadamente para o grupo definido no relatório, a propriedade Order em Cursor1 está definida para o índice EMP_ID.

A variável pública, nTotalSales, definida no evento Init de Cursor2, armazena o total de todos os pedidos. A variável é declarada pública para torná-la visível além do código Init de Cursor2.

Um controle de campo na banda Group Footer calcula e exibe a porcentagem para cada funcionário usando a seguinte expressão:

```foxpro
STR(INT((emp_total / nTotalSales)*100)) + " " + "%"
```

Um controle de campo na banda Summary calcula e exibe a porcentagem total para todos os funcionários usando a seguinte expressão:

```foxpro
STR(INT((nTotalSales / nTotalSales)*100)) + " " + "%"
```
