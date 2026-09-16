# Identificando campos

Aqui estão algumas dicas para determinar seus campos:

# Relacione cada campo diretamente ao assunto da tabela

Um campo que descreve o assunto de uma tabela diferente pertence a essa outra tabela. Mais tarde, quando você definir relações entre suas tabelas, verá como combinar os dados de campos em várias tabelas. Por enquanto, certifique-se de que cada campo em uma tabela descreve diretamente o assunto da tabela. Se você se encontrar repetindo as mesmas informações em várias tabelas, isso é um indício de que há campos desnecessários em algumas das tabelas.

# Não inclua dados derivados ou calculados

Na maioria dos casos, você não quer armazenar o resultado de cálculos em tabelas. Em vez disso, você pode fazer o Visual FoxPro executar os cálculos quando quiser ver o resultado. Por exemplo, o formulário de pedido Tasmanian Traders exibe o preço estendido para cada linha do pedido no banco de dados Tasmanian Traders. No entanto, não há um campo de subtotal Extended Price em nenhuma tabela Tasmanian Traders. Em vez disso, a tabela Order_Line_Items inclui um campo quantity que armazena as unidades em pedido para cada produto individual, bem como o preço unitário de cada item pedido. Usando esses dados, o Visual FoxPro calcula o subtotal cada vez que você imprime um formulário de pedido. O subtotal em si não precisa ser armazenado em uma tabela. Para obter mais informações, consulte Analyzing Data Requirements.

# Inclua todas as informações que você precisa

É fácil deixar passar informações importantes. Volte às informações que você coletou na primeira etapa do processo de design. Examine seus formulários e relatórios em papel para garantir que todas as informações que você exigiu no passado estão incluídas em suas tabelas do Visual FoxPro ou podem ser derivadas delas. Pense nas perguntas que você fará ao Visual FoxPro. O Visual FoxPro pode encontrar todas as respostas usando as informações em suas tabelas? Você identificou campos que armazenarão dados exclusivos, como o ID do cliente? Quais tabelas incluem informações que você combinará em um relatório ou formulário? Para obter mais informações, consulte Using Primary Key Fields e Identifying Relationships.

# Armazene informações em suas menores partes lógicas

Você pode ser tentado a ter um único campo para nomes completos, ou para nomes de produtos, junto com descrições de produtos. Se você combinar mais de um tipo de informação em um campo, é difícil recuperar fatos individuais depois. Tente dividir as informações em partes lógicas; por exemplo, crie campos separados para primeiro e último nome, ou para nome do produto, categoria e descrição.

# Exemplo

Tasmanian Traders vende alimentos especiais importados de todo o mundo. Os funcionários usam um relatório Products On Order para acompanhar os produtos sendo pedidos.
 Relatório para acompanhar o inventário de produtos

O relatório indica que a tabela Products, que contém fatos sobre produtos vendidos, precisa incluir campos para o nome do produto, unidades em estoque e unidades em pedido, entre outros. Mas e os campos para o nome e o telefone do fornecedor? Para produzir o relatório, o Visual FoxPro precisa saber qual fornecedor corresponde a cada produto.
 Rascunho da tabela Supplier contendo campos para nome e telefone do fornecedor

Você pode resolver isso sem armazenar dados redundantes em suas tabelas criando uma tabela Supplier com campos separados para o nome e o telefone do fornecedor. Para obter mais informações, consulte Using Primary Key Fields.
