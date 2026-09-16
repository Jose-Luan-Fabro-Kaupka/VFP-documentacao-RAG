# Caixa de diálogo Calculate Field

Permite selecionar uma operação matemática para criar um campo calculado. Essa caixa de diálogo é exibida quando você escolhe Calculations na caixa de diálogo Report Expression.

> **Observação:** Dependendo da configuração da variável de sistema _REPORTBUILDER, essa caixa de diálogo pode ser substituída por uma interface do usuário alternativa. Para obter mais informações, consulte Variável de sistema _REPORTBUILDER.
 **Reset**
Especifica o ponto no qual redefinir quaisquer cálculos cumulativos. O valor padrão é "End of Report". Observação: se você tiver especificado grupos de dados no relatório, bandas Detail ou expressões de alias de destino para bandas Detail, a lista Reset based on exibirá esses itens.

# Calculate

Especifica operações de cálculo adicionais que podem ser aplicadas aos valores de uma expressão de controle Field para obter o valor renderizado na saída.
 **Nothing**
(Padrão) Nenhum cálculo adicional é realizado. O resultado da expressão Field é passado diretamente ao mecanismo de relatório para saída.
**Count**
O valor exibido é uma contagem do número de vezes que a expressão foi avaliada para os registros percorridos até o momento. (A expressão Field não é avaliada.)
**Sum**
O valor exibido é um total acumulado dos valores da expressão Field para os registros percorridos até o momento.
**Average**
Calcula a média aritmética do valor da expressão Field para cada registro percorrido até o momento e exibe os resultados.
**Lowest**
Exibe o menor valor da expressão para um grupo, página, coluna, relatório ou banda Detail, dependendo da opção selecionada na lista Reset, e usa na expressão o valor do primeiro registro do grupo. Quando um valor menor é encontrado, o valor da expressão muda de acordo.
**Highest**
O valor exibido é o maior valor da expressão Field avaliada para os registros percorridos até o momento.
**Standard deviation**
Calcula a raiz quadrada da variância da expressão Field avaliada para cada registro percorrido até o momento e exibe os resultados.
**Variance**
Mede o grau em que o valor avaliado da expressão Field varia em relação à média dos registros percorridos até o momento e exibe o resultado.
