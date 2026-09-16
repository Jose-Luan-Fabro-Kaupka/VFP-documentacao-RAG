# Guia Calculate, caixa de diálogo Report Control Properties (Report Builder)

Permite especificar um cálculo a ser executado em expressões de controle Field e exibir os resultados do cálculo em vez da expressão. Você também pode especificar o ponto em que redefinir o cálculo no relatório.

> **Observação:** Esta guia substitui a funcionalidade da caixa de diálogo nativa do Visual FoxPro Calculate Field Dialog Box quando o Report Builder está ativo.

How to: Perform Calculations in Field Controls

# Tipo de cálculo

Especifica operações de cálculo adicionais que podem ser aplicadas aos valores de uma expressão de controle Field para obter o valor renderizado na saída:

> **Observação:** Cálculos cumulativos são redefinidos dependendo da opção Reset value based on.
 - None (Padrão) Nenhum cálculo adicional é executado. O resultado da expressão Field é passado diretamente ao report engine para saída.
- Count O valor exibido é uma contagem do número de vezes que a expressão foi avaliada para os registros percorridos até o momento. (A expressão Field não é avaliada.)
- Sum O valor exibido é um total acumulado dos valores da expressão Field para os registros percorridos até o momento.
- Average Calcula a média aritmética do valor da expressão Field para cada registro percorrido até o momento e exibe os resultados.
- Lowest O valor exibido é o menor valor da expressão Field avaliada para os registros percorridos até o momento.
- Highest O valor exibido é o maior valor da expressão Field avaliada para os registros percorridos até o momento.
- Std Deviation Calcula a raiz quadrada da variância da expressão Field avaliada para cada registro percorrido até o momento e exibe os resultados.
- Variance Mede o grau em que o valor da expressão Field avaliada varia da média para os registros percorridos até o momento e exibe o resultado.

# Reset based on

Especifica o ponto em que redefinir quaisquer cálculos cumulativos. O valor padrão é "End of Report."

> **Observação:** Se você especificou grupos de dados no relatório, bandas Detail ou expressões de alias de destino para bandas Detail, a lista Reset based on exibe esses itens.
