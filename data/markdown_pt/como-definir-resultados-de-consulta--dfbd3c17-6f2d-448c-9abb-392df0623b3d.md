# Como: definir resultados de consulta

Depois de abrir o Query Designer e selecionar a tabela ou view que contém as informações desejadas, você pode definir seus resultados. No mínimo, você precisa selecionar os campos desejados. Você também pode definir seus resultados configurando a ordem em que os campos selecionados aparecem e definindo filtros para selecionar quais registros aparecem.

# Selecionando os campos desejados

Antes de executar uma consulta, você deve selecionar alguns campos para incluir nos resultados. Em alguns casos, você pode querer usar todos os campos da tabela ou view. Em outros, você pode querer focar a consulta em alguns campos selecionados, como campos que deseja incluir em um relatório.

Certifique-se de incluir quaisquer campos que possa querer usar para ordenar ou agrupar os resultados da sua consulta. Ao selecionar os campos, você também pode definir a ordem em que aparecem na saída.

Use a guia Fields no painel inferior do Query Designer para selecionar os campos que deseja incluir nos resultados da sua consulta.

### Para adicionar um campo à saída da consulta
- Selecione o nome do campo e escolha Add . -ou-
- Arraste o nome do campo para a caixa Selected fields.

### Selecionando todos os campos para saída

Você pode selecionar todos os campos por nome ou usar o curinga asterisco. Se você selecionar os campos por nome, os nomes exatos dos campos são incluídos na consulta. Se você executar a consulta depois de adicionar campos à tabela, os novos campos não são incluídos nos resultados.

Se você usar o curinga, o asterisco é incluído na consulta e inclui todos os campos que estão na tabela no momento da consulta. Se a estrutura da tabela mudou desde que a consulta foi criada, os novos campos também aparecem nos resultados da consulta.

### Para adicionar todos os campos disponíveis a uma consulta de uma vez
- Escolha Add All para adicionar campos por nome. -ou-
- Arraste o asterisco no topo da tabela para a caixa Selected fields.

### Exibindo um alias para um campo

Você pode tornar os resultados da sua consulta mais fáceis de ler e entender adicionando uma legenda descritiva a um campo de resultados. Por exemplo, você pode querer exibir a palavra "SumMaxOrd" no topo da coluna de resultados em vez do nome do campo ou expressão, SUM(MaxOrdAmount).

### Para adicionar um alias para um campo
- Na caixa Functions and expressions, digite o nome do campo e, em seguida, digite AS e o alias, como neste exemplo: SUM(maxorderamt) AS SumMaxOrd
- Escolha Add para colocar o campo com o alias na caixa Selected fields.

# Definindo a ordem dos campos de saída

A ordem em que os campos aparecem na guia Fields determina a ordem das colunas de informações na saída da sua consulta.

### Para alterar a ordem das colunas da saída da consulta
- Arraste a caixa de movimentação, localizada à esquerda de um nome de campo, para cima ou para baixo.

Se você quiser alterar a ordem em que as linhas de informações serão ordenadas, use a guia Order By em vez disso.

# Selecionando os registros desejados

Selecionar os registros que deseja encontrar é a etapa fundamental que determina os resultados da sua consulta. Com a guia Filter no Query Designer, você pode formular a cláusula WHERE de uma instrução select para informar ao Visual FoxPro quais registros pesquisar e recuperar.

Você pode querer encontrar um subconjunto específico de dados para incluir em um relatório ou outra saída: por exemplo, todos os clientes com saldos pendentes, todos os clientes em uma região ou código postal específico, e assim por diante. Para ver somente os registros desejados, insira um valor ou intervalo de valores para comparar os registros.

No Visual FoxPro, você usa a guia Filter para especificar qual campo deseja usar para selecionar registros, escolher um critério de comparação e inserir um exemplo do valor com o qual deseja que o campo seja comparado.

### Para especificar um filtro
- Na lista Field Name, escolha um campo que deseja usar como base para selecionar registros. Observação Você não pode usar campos General ou Memo em um filtro.
- Na lista Criteria, escolha o tipo de comparação a usar.
- Insira o critério de comparação na caixa Example. Use aspas somente se a cadeia de caracteres for igual ao nome de um campo em uma tabela na consulta; caso contrário, não coloque cadeias de caracteres entre aspas. Se usar datas, não as coloque entre chaves. Coloque um ponto antes e depois de um literal lógico (.T.). Se você inserir um nome de campo de uma tabela na consulta, o Visual FoxPro o reconhecerá como um campo.
- Se desejar que a capitalização seja ignorada em pesquisas em dados de caractere, selecione o botão Case.

Se desejar inverter o significado de um operador lógico, selecione o botão Not. Por exemplo, se desejar encontrar clientes em todas as regiões exceto Washington, use a expressão de seleção no exemplo a seguir:

```foxpro
Customer.region Not Like WA
```

Para ajustar ainda mais sua pesquisa, você pode adicionar mais filtros na guia Filter, Query and View Designers. Para obter mais informações, consulte "Fine-Tuning Your Search" em Como: personalizar consultas.

Se você estiver usando mais de uma tabela ou view em sua consulta, pode expandir os registros que seleciona pelo tipo de junção que escolher.

# Selecionando um número ou percentual de registros

Se você precisar somente de um certo número ou percentual de registros do conjunto de resultados que sua consulta retorna, pode usar as opções Top na guia Miscellaneous no Query Designer ou View Designer, ou pode adicionar uma cláusula TOP à sua instrução SQL SELECT. Você pode fornecer um número de 1 a 32.767 ou um percentual de 0,01 a 99,99 em uma cláusula TOP. O Visual FoxPro ordena os registros primeiro e depois extrai o número ou percentual superior de registros.

### Para limitar o número de registros a recuperar
- No Query Designer , selecione a guia Miscellaneous.
- Na área Top, desmarque a caixa All para tornar outras opções na área Top disponíveis.
- Escolha uma das seguintes: Na caixa Number of records, digite ou selecione o número máximo de registros que deseja recuperar. -OU- Clique em Percent para alterar a caixa Number of records para Percentage para que você possa digitar ou selecionar o percentual máximo de registros que deseja recuperar.

Por exemplo, se desejar selecionar os 10 principais clientes com os maiores valores de pedido, pode especificar um GROUP BY em CUST_ID para mostrar um registro agregado para cada cliente e ordenar por ORDER_AMT na cláusula ORDER BY. Para obter um verdadeiro TOP 10, você precisa especificar uma ordenação descendente em ORDER_AMT para que os registros com os maiores valores de pedido apareçam primeiro nos resultados. Se você usar uma ordenação ascendente, os registros de resultado são ordenados do menor valor de pedido para o maior. Os registros superiores que você seleciona do conjunto de resultados teriam na verdade os menores valores.

```foxpro
SELECT TOP 10 *;
FROM testdata!customer INNER JOIN testdata!orders ;
ON Customer.cust_id = Orders.cust_id;
GROUP BY Customer.cust_id;
ORDER BY Orders.order_amt DESC
```
