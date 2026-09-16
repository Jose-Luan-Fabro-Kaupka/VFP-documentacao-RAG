# Como: organizar resultados de consulta

Com a saída da sua consulta definida, você pode agora organizar os registros que aparecem nos seus resultados ordenando e agrupando nos campos de saída. Se desejar, você também pode filtrar os grupos que aparecem nos seus resultados.

# Ordenando Resultados de Consulta

A ordenação determina a ordem em que os registros ou linhas serão classificados quando aparecerem na saída da sua consulta. Por exemplo, você pode classificar registros por State e depois por City, ou classificá-los em ordem ascendente com base no saldo pendente da conta.

Use a guia Order By para definir a ordem de classificação da sua consulta. A ordem de classificação determina a ordem em que as linhas ou registros aparecerão na saída da sua consulta.

Primeiro selecione os campos que deseja usar na caixa Selected Fields e mova-os para a caixa Ordering Criteria. Em seguida, organize os campos na ordem em que deseja que apareçam nos resultados da consulta.

### Para definir critérios de ordenação
- Na caixa Selected fields, selecione um nome de campo.
- Escolha Add.

### Para remover critérios de ordenação
- Selecione um ou mais campos que deseja remover.
- Escolha Remove.

A ordem em que os campos aparecem na caixa Ordering criteria determina a ordem de importância quando os resultados da consulta são classificados. O primeiro campo determina a ordem de classificação primária.

Por exemplo, se o primeiro campo na caixa Ordering criteria é `Customer.region` e o segundo campo na caixa Ordering criteria é `Customer.city`, os resultados serão ordenados por `Customer.region`. Se mais de um registro na tabela de clientes tiver o mesmo valor de campo `region`, esses registros são adicionalmente ordenados por `Customer.city`.

Para ajustar a importância de um campo de ordem de classificação, use o botão à esquerda do campo para arrastar o campo para o local desejado na caixa Ordering criteria.

Você pode classificar em ordem ascendente ou descendente definindo os botões na área Order options. Cada campo de ordenação aparece na caixa Output fields na guia Filter com uma seta para cima ou para baixo ao lado dele, indicando se a classificação nesse campo será feita em ordem ascendente ou descendente.

# Agrupando Resultados de Consulta

O agrupamento consolida ou reúne registros semelhantes em um registro para que você possa realizar cálculos baseados em grupos de registros. Por exemplo, você pode querer encontrar a soma de todos os pedidos para uma região específica. Em vez de olhar todos os registros individualmente, você pode agrupar todos os registros da mesma região em um registro e obter a soma de todos os pedidos dessa região. Para controlar como os registros são agrupados, use a guia Group By no Query Designer.

O agrupamento é mais útil quando usado em conjunto com uma função agregada, como SUM, COUNT, AVG e assim por diante.

Por exemplo, suponha que você deseja ver o valor total em dólares dos pedidos para cada número de ID de cliente na sua tabela de pedidos. Você precisa agrupar todos os registros de pedidos para um determinado ID de cliente em um registro e encontrar a soma dos valores dos pedidos.

Primeiro use a guia Fields para adicionar a expressão SUM(Orders.order_net) à saída da sua consulta, depois use a guia Group By para agrupar os resultados por número de ID de cliente. Os resultados mostram o total líquido de pedidos para cada cliente:

### Para definir opções de agrupamento
- Na guia Fields, digite a expressão na caixa Functions and expressions. -ou- Escolha o botão de diálogo para usar o Expression Builder para inserir uma expressão na caixa Functions and expressions.
- Escolha o botão Add para colocar a expressão na caixa Selected fields.
- Na guia Group By, adicione a expressão para agrupar os resultados.

Você também pode definir um filtro nos resultados agrupados.

# Selecionando os Grupos que Você Deseja

Para definir um filtro em registros agrupados ou consolidados em vez de em registros individuais, escolha Having na guia Group By. Você pode usar um nome de campo, uma função agregada em um nome de campo ou outra expressão na caixa Field Name.

Baseando-se no exemplo anterior, você pode usar a consulta que mostra vendas totais por número de cliente e, em seguida, usar o botão Having para restringir a saída a clientes com mais de US$ 50.000 em pedidos líquidos:

### Para definir uma opção Having em um grupo
- Na guia Group By, escolha Having.
- Na caixa de diálogo Having, selecione uma função e nome de campo no campo Field Name.
- Escolha OK.
