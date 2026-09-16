# Organizando requisitos em tabelas

Determinar as tabelas no seu banco de dados pode ser a etapa mais difícil do processo de design de banco de dados. Isso porque os resultados que você deseja do seu banco de dados — os relatórios que deseja imprimir, os formulários que deseja usar e as perguntas que deseja responder — não necessariamente fornecem pistas sobre a estrutura das tabelas que os produzem. Eles dizem o que você deseja saber, mas não como categorizar as informações em tabelas.

Veja o formulário de pedido em Analisando requisitos de dados como exemplo. Ele inclui fatos sobre o cliente — o endereço e o telefone do cliente — junto com fatos sobre o pedido. Este formulário fornece vários fatos que você sabe que deseja armazenar no seu banco de dados. Embora os fatos estejam todos no mesmo formulário, você pode facilmente evitar problemas comuns de integridade de dados armazenando-os em tabelas separadas.

# Armazenar informações uma vez reduz a chance de erro

Por exemplo, se você usar apenas uma tabela para armazenar as informações de um formulário de pedido, suponha que um cliente faça três pedidos diferentes. Você poderia adicionar o endereço e o telefone do cliente ao seu banco de dados três vezes, uma para cada pedido. Mas isso multiplica a chance de erros de entrada de dados.

# A tabela Customer armazena informações de endereço uma vez

Além disso, se o cliente se mudar, você teria que aceitar informações contraditórias ou localizar e alterar cada um dos registros de vendas desse cliente na tabela. É muito melhor criar uma tabela Customer que armazene o endereço do cliente no seu banco de dados uma vez. Então, se você precisar alterar os dados, altera-os apenas uma vez.

# Evitando a exclusão de informações valiosas

Suponha que um novo cliente faça um pedido e depois o cancele. Quando você exclui o pedido da tabela que contém informações sobre clientes e pedidos, excluiria também o nome e o endereço do cliente. Mas você deseja manter esse novo cliente no seu banco de dados para poder enviar a ele seu próximo catálogo. Novamente, é melhor colocar as informações sobre o cliente em uma tabela Customer separada. Dessa forma, você pode excluir o pedido sem excluir as informações do cliente.

Observe as informações que você deseja obter do seu banco de dados e divida-as em assuntos fundamentais que deseja acompanhar, como clientes, funcionários, produtos que você vende, serviços que você fornece e assim por diante. Cada um desses assuntos é candidato a uma tabela separada.

> **Dica:** Uma estratégia para dividir informações em tabelas é examinar fatos individuais e determinar sobre o que cada fato realmente trata. Por exemplo, no formulário de pedido da Tasmanian Traders, o endereço do cliente não trata da venda; trata do cliente. Isso sugere que você precisa de uma tabela separada para clientes. No relatório Products On Order, o telefone do fornecedor não trata do produto em estoque; trata do fornecedor. Isso sugere que você precisa de uma tabela separada para fornecedores.
