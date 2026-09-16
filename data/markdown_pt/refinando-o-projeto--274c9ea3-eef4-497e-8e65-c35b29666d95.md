# Refinando o projeto

Quando você tiver as tabelas, campos e relações necessários, será hora de examinar o projeto e detectar possíveis falhas restantes.

Você pode encontrar várias armadilhas ao projetar seu banco de dados. Estes problemas comuns podem dificultar o uso e a manutenção dos dados:
 - Você tem uma tabela com muitos campos que não estão todos relacionados ao mesmo assunto? Por exemplo, uma tabela pode conter campos sobre clientes e também informações de vendas. Procure garantir que cada tabela contenha dados sobre apenas um assunto.
- Você tem campos deixados intencionalmente em branco em muitos registros porque não se aplicam a eles? Isso geralmente significa que os campos pertencem a outra tabela.
- Você tem muitas tabelas que contêm os mesmos campos? Por exemplo, tabelas separadas para vendas de janeiro e fevereiro, ou para clientes locais e remotos, nas quais armazena o mesmo tipo de informação. Procure consolidar em uma tabela todas as informações relativas a um único assunto. Talvez também seja necessário adicionar um campo, por exemplo, para identificar a data da venda.

Crie suas tabelas, especifique as relações entre elas e insira alguns registros em cada uma. Veja se consegue usar o banco de dados para obter as respostas desejadas. Crie rascunhos de formulários e relatórios e confira se mostram os dados esperados. Procure duplicações desnecessárias de dados e elimine-as.

Ao testar o banco de dados inicial, você provavelmente descobrirá oportunidades de melhoria. Verifique:
 - Você esqueceu algum campo? Há informações necessárias que não foram incluídas? Em caso afirmativo, elas pertencem às tabelas existentes? Se forem sobre outro assunto, talvez seja necessário criar outra tabela.
- Você escolheu uma boa chave primária para cada tabela? Ao usá-la para pesquisar registros específicos, ela é fácil de lembrar e digitar? Certifique-se de que não será necessário inserir em um campo de chave primária um valor que duplique outro valor desse campo.
- Você insere repetidamente informações duplicadas em uma tabela? Nesse caso, provavelmente deve dividi-la em duas tabelas com uma relação um-para-muitos.
- Você tem tabelas com muitos campos, poucos registros e muitos campos vazios em registros individuais? Nesse caso, considere reprojetar a tabela para que tenha menos campos e mais registros.

À medida que identificar as alterações desejadas, você poderá modificar tabelas e campos para refletir o projeto aprimorado. Para obter informações sobre a modificação de tabelas, consulte Trabalhando com tabelas (Visual FoxPro).

# Exemplo

Cada produto no estoque da Tasmanian Traders pertence a uma categoria geral, como Bebidas, Condimentos ou Frutos do mar. A tabela Products poderia incluir um campo que mostrasse a categoria de cada produto.
 Tabela Products com um campo Category_name

Suponha que, ao examinar e refinar o banco de dados, a Tasmanian Traders decida armazenar uma descrição da categoria junto com seu nome. Se você adicionar um campo Category Description à tabela Products, precisará repetir cada descrição de categoria para cada produto pertencente a ela — o que não é uma boa solução.

Uma solução melhor é tornar Category um novo assunto acompanhado pelo banco de dados, com sua própria tabela e chave primária. Em seguida, você pode adicionar a chave primária da tabela Category à tabela Products como uma chave estrangeira.
 A tabela Category armazena informações de categoria com eficiência

As tabelas Category e Products têm uma relação um-para-muitos: uma categoria pode conter mais de um produto, mas cada produto individual pode pertencer a apenas uma categoria.
