# Guia Filtro, Designers de Consulta e Exibição

Determina as condições para selecionar registros conforme listadas na cláusula WHERE do comando SELECT - SQL na janela SQL. Você pode carregar e salvar uma consulta ou exibição com uma subconsulta na cláusula WHERE. Este guia aparece nos Designers de Consulta e Exibição.

Caixa de movimentação

Arraste a caixa de movimentação para mover o item selecionado para cima ou para baixo na grade.
 **Botão Condição**
Clique na seta horizontal de duas pontas para editar o filtro selecionado.
**Nome do campo**
Especifica o primeiro campo da condição de filtro. Ao criar uma nova condição de filtro, clique no campo para exibir uma lista suspensa dos campos disponíveis.
**Not**
Inverte a condição para excluir os registros correspondentes.
**Critérios**
Especifica um operador de comparação: Equal (=) especifica que o campo e o valor no campo Exemplo têm o mesmo valor. Like especifica que o campo deve incluir caracteres correspondentes aos do texto no campo Exemplo. Por exemplo, Customer.state Like O corresponde a registros de Ohio, Oklahoma e Oregon. Exactly Like (==) especifica que o campo deve corresponder, caractere por caractere, ao texto no campo Exemplo. Greater Than (>) especifica que o campo deve ser maior que o valor no campo Exemplo. Less Than (<) especifica que o campo deve ser igual ou menor que o valor no campo Exemplo. Greater Than or Equal To (>=) especifica que o campo deve ser igual ou maior que o valor no campo Exemplo. Less Than or Equal To (<=) especifica que o campo deve ser igual ou menor que o valor no campo Exemplo. Is NULL especifica que o campo deve conter um valor nulo. Is True constrói uma cláusula WHERE contendo somente o campo à esquerda quando o campo ou expressão é avaliado como True, pressupondo que resulte em um valor lógico. Between especifica que o campo deve ser maior ou igual ao valor inferior e menor ou igual ao valor superior da condição mostrada na coluna Exemplo. Separe os dois valores do campo Exemplo com AND. O Visual FoxPro cria a consulta com BETWEEN. Por exemplo, Invoices.idate Between 05/10/97 AND 05/12/97 corresponde aos registros de 10, 11 e 12 de maio de 1997. In especifica que o campo deve corresponder a um dos vários valores da lista separada por vírgulas no campo Exemplo. Por exemplo, Customer.name In Al,George,Mary corresponde aos registros em que o nome do cliente é Al, George ou Mary. Exists especifica que os registros retornados contêm o critério do campo Exemplo. Quando a condição de filtro especifica Exists, ela é avaliada como True (.T.), a menos que a subconsulta retorne um conjunto vazio. No exemplo a seguir, Exists retorna todos os clientes que têm um pedido: SELECT Customer.cust_id, Customer.company; FROM testdata!customer; WHERE Exists (select * from orders where customer.cust_id = ; orders.cust_id)
**Exemplo**
Especifica o valor ou texto com o qual você deseja comparar o campo. Para corresponder às maiúsculas e minúsculas do texto do exemplo, use as funções UPPER( ), LOWER( ) e PROPER( ).
**Lógico**
Adiciona uma condição AND ou OR à lista de condições de filtro.
**Pri. (Prioridade)**
Especifica um número de 0 a 99 que indica a prioridade das operações lógicas. O número 0 indica a prioridade mais alta, enquanto 99 indica a mais baixa. Definir prioridades para operações lógicas determina a ordem em que cada operação é realizada. Na prática, o comportamento é semelhante ao uso de parênteses (()) para agrupar operações. Por exemplo, suponha que você especifique prioridade 0 para uma operação lógica, prioridade 1 para uma segunda e prioridade 0 para uma terceira. A primeira e a terceira operações, com prioridade 0, serão realizadas antes da operação com prioridade 1.
**Botão Inserir**
Insere uma condição de filtro em branco acima da condição selecionada.
**Botão Remover**
Remove a condição selecionada da consulta.
