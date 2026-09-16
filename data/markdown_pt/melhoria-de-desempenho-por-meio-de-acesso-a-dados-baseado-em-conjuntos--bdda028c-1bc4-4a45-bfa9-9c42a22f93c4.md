# Melhoria de desempenho por meio de acesso a dados baseado em conjuntos

Um dos fatores mais importantes na construção de uma aplicação cliente/servidor rápida e eficiente é minimizar a quantidade de dados que você transfere do servidor. Como aplicações cliente/servidor podem acessar quantidades potencialmente enormes de dados em um servidor remoto, usar técnicas tradicionais de navegação local pode resultar em uma aplicação cliente/servidor lenta. Para acelerar o desempenho, você usa técnicas de acesso a dados baseadas em conjuntos para filtrar a quantidade de dados que você transfere.

# Acessando dados baseados em conjuntos com eficiência

Dados remotos são baseados em conjuntos; você acessa dados remotos selecionando um conjunto de dados de um grande repositório de dados usando instruções SELECT - SQL Command. A diferença mais importante entre construir uma aplicação local tradicional e construir uma aplicação cliente/servidor é o contraste entre técnicas tradicionais de navegação do Visual FoxPro e técnicas de acesso a dados de servidor baseadas em conjuntos.

### Usando técnicas tradicionais de navegação

Na programação tradicional de banco de dados local, você pode acessar quantidades discretas e frequentemente grandes de dados usando o comando GOTO BOTTOM, contra o qual você então consulta. Você pode navegar pelos dados emitindo um comando SET RELATION Command para criar um relacionamento temporário entre duas tabelas e depois emitindo um comando SKIP Command para mover pelos registros relacionados.

Embora esse método de navegação por registros possa ser usado com dados remotos, pode ser ineficiente contra grandes repositórios de dados remotos. Por exemplo, se você criar uma remote view que acessa uma tabela grande em uma fonte de dados remota e depois emitir o comando GO | GOTO Command, você deve aguardar enquanto todos os dados na view são recuperados da fonte de dados, enviados pela rede e carregados no cursor da view do seu sistema local.

### Usando consultas parametrizadas

Uma abordagem mais eficiente para acessar dados remotos é transferir apenas os dados que você precisa e depois reconsultar para obter registros adicionais ou novos específicos. Use uma instrução SELECT baseada em parâmetros para transferir um conjunto específico pequeno de dados e depois acessar novos registros usando a função REQUERY( ) Function para solicitar um novo conjunto de dados.

Você não emite o comando GOTO BOTTOM contra dados de servidor remoto porque isso:
 - Sobrecarregaria desnecessariamente os recursos de rede ao transferir grandes quantidades de dados.
- Tornaria o desempenho da sua aplicação mais lento ao manipular dados desnecessários.
- Potencialmente reduziria a precisão dos dados no cursor local porque alterações nos dados remotos não são refletidas no cursor local até que você reconsulte.

Por exemplo, se você deseja criar uma aplicação cliente/servidor que acessa os pedidos de um cliente específico, crie uma remote view que acessa a tabela Customer. Crie outra remote view que acessa a tabela Orders, mas parametrize a view com base no campo `cust_id`. Depois use o registro de cliente atual como parâmetro para a view da tabela Orders.

Você pode usar o parâmetro para delimitar o conjunto de dados transferido para apenas a quantidade certa de dados. Se você solicitar poucos dados, pode perder desempenho porque terá que reconsultar o servidor remoto com mais frequência. Se você solicitar muitos dados, pode desperdiçar tempo transferindo dados que não usará.

# Escolhendo o melhor design cliente/servidor

Os exemplos a seguir descrevem como obter os benefícios da tecnologia cliente/servidor e evitar as armadilhas de técnicas de programação inadequadas. O primeiro método usa práticas de programação tradicionais para recuperar todos os dados de uma fonte de dados remota em cursors locais que são então relacionados com o comando SET RELATION Command. O segundo, terceiro e quarto métodos adotam técnicas progressivamente mais inteligentes de busca de dados, limitando efetivamente a quantidade de dados transferidos com uma metodologia just-in-time que fornece os dados mais recentes e o tempo de resposta mais rápido em uma rede.

### Usando uma estratégia cliente/servidor não otimizada

Uma aplicação cliente/servidor direta e não otimizada usa técnicas de navegação de dados locais com dados remotos. Por exemplo, se você tem 10 milhões de registros de clientes e 100 milhões de registros de pedidos em uma fonte de dados remota, pode criar uma aplicação ineficiente que transfere todos os registros de Customer e Order para cursors locais. Você poderia então indexar 100 milhões de registros de pedidos, criar um relacionamento temporário entre as tabelas Customer e Orders em seus cursors locais e usar o comando SKIP para navegar pelos registros.

Esse método não é otimizado para desempenho, mas pode, no entanto, ser útil se o lado um for local e o lado muitos for remoto.

### Filtrando o lado muitos

Uma aplicação cliente/servidor ligeiramente melhorada limita o lado muitos do relacionamento, mas recupera todo o lado um para que você possa pular pelos registros. Neste cenário, você cria uma remote view do lado muitos do relacionamento, a tabela Orders, parametrizada no ID do cliente. Você então transfere toda a tabela Customer.

Embora criar uma view parametrizada na tabela Orders seja uma melhoria em relação a transferir todos os pedidos, você ainda recupera informações desnecessárias ao continuar transferindo toda a tabela Customer. A tabela Customer também está cada vez mais desatualizada conforme alterações são feitas por outros usuários no seu sistema. Esse método pode ser benéfico se o lado um do relacionamento contiver um conjunto de dados pequeno.

### Filtrando o lado um

Uma técnica de programação cliente/servidor melhor cria remote views para todos os dados remotos. Você limita o número de registros Customer transferidos para a remote view da tabela Customer usando a instrução SELECT na view para selecionar apenas os clientes de uma região. Você então cria uma remote view do lado muitos do relacionamento, a tabela Orders, parametrizada no ID do cliente.

Este cenário recupera um conjunto menor de registros. Você usa o comando SKIP Command para pular no lado um da relação (a view Customer). Você usa a função REQUERY( ) Function para acessar novos dados no lado muitos (Orders).

Neste exemplo, você limita ou filtra tanto o lado um quanto o lado muitos do relacionamento, e ainda pode usar o comando SKIP para navegar pelos dados filtrados. Este método é recomendado se o lado um do relacionamento, mesmo após ser filtrado, ainda for suficiente para fornecer informações para um conjunto sucessivo de consultas antes de reconsultar o servidor remoto.

### Usando a chave primária para acessar o relacionamento um-para-muitos

O paradigma de programação cliente/servidor mais eficiente abandona o luxo de usar o comando SKIP Command e cria um formulário que solicita entrada ou seleção do ID do cliente, que é então usado como parâmetro para uma remote view da tabela Customer. Este parâmetro também é usado como parâmetro para uma remote view da tabela Orders.

Por exemplo, você poderia criar um formulário um-para-muitos em que as informações do cliente formam o lado um, e um controle Grid exibe o lado muitos do relacionamento. O controle Grid pode ser vinculado ao ID do cliente escolhido no lado um do formulário. Você pode então definir a propriedade MaxRecords da função CURSORSETPROP( ) Function como 1 e usar o seguinte código para preencher o lado um do formulário:

```foxpro
SELECT * FROM customer WHERE customer.cust_id = ?cCust_id
```

Quando os usuários desejam visualizar o registro de um cliente diferente, eles inserem ou selecionam um novo ID de cliente. O formulário reconsulta a fonte de dados pelos pedidos do novo ID de cliente e atualiza o controle Grid com os novos dados de pedidos.

Usando essas técnicas, sua aplicação transfere apenas os dados que você precisa, no momento em que são necessários. Você acelera a resposta na rede limitando a quantidade de dados transferidos e fornece informações mais recentes ao usuário reconsultando a fonte de dados imediatamente antes de exibir as informações solicitadas.

Este método é recomendado quando você deseja acessar o relacionamento um-para-muitos aleatoriamente usando qualquer valor de chave primária. Você pode querer transferir as chaves primárias para um controle, como uma lista suspensa, quando abrir o formulário e depois fornecer um controle que o usuário pode escolher para atualizar a lista de valores de chave primária sob demanda.

### Usando o ambiente de dados em aplicações cliente/servidor

Quando você usa dados remotos em um formulário, inclua as views no ambiente de dados do formulário. Você pode definir a propriedade AutoOpenTables do ambiente de dados como false (.F.) para especificar quando a aplicação atualiza as views com os dados remotos. Defina a propriedade ControlSource para caixas de texto ou outros controles vinculados a dados depois de chamar o método OpenTables do ambiente de dados, normalmente no código associado ao evento Init do formulário. Para obter mais informações, consulte Creating Forms.
