# Identificando relacionamentos

Depois de dividir suas informações em tabelas, você precisa de uma forma de informar ao Visual FoxPro como reunir tudo novamente de maneira significativa. Por exemplo, o formulário a seguir inclui informações de várias tabelas.
 O formulário Order Entry usa informações de várias tabelas.

O Visual FoxPro é um sistema de gerenciamento de banco de dados relacional. Isso significa que você armazena dados relacionados em tabelas separadas. Em seguida, você define relacionamentos entre as tabelas e o Visual FoxPro usa os relacionamentos para encontrar informações associadas armazenadas no seu banco de dados.

Por exemplo, suponha que você deseja telefonar para um funcionário com perguntas sobre uma venda que ele realizou. Os números de telefone dos funcionários estão registrados na tabela Employee; as vendas estão registradas na tabela Orders. Quando você informa ao Visual FoxPro qual venda lhe interessa, o Visual FoxPro pode consultar o número de telefone com base no relacionamento entre as duas tabelas. Isso funciona porque Employee_id, a chave primária da tabela Employee, também é um campo na tabela Orders. Na terminologia de banco de dados, o campo Employee_id na tabela Orders é chamado de chave estrangeira, porque faz referência a uma chave primária de uma tabela diferente, ou estrangeira.
 Campo Employee_id como chave primária da tabela Employee e chave estrangeira da tabela Orders

Portanto, para configurar um relacionamento entre duas tabelas — Tabela A e Tabela B — você adiciona a chave primária de uma tabela à outra tabela, de modo que ela apareça em ambas as tabelas. Mas como decidir qual chave primária usar? Para configurar o relacionamento corretamente, você deve primeiro determinar a natureza do relacionamento. Existem três tipos de relacionamentos entre tabelas:
 - Relacionamentos um-para-muitos
- Relacionamentos muitos-para-muitos
- Relacionamentos um-para-um

Os exemplos a seguir apresentam cada tipo de relacionamento e explicam como projetar suas tabelas para que o Visual FoxPro possa associar os dados corretamente. O objetivo de cada exemplo é explicar como você determina os relacionamentos entre suas tabelas e como decide quais campos pertencem às tabelas para dar suporte a esses relacionamentos — não descreve como usar a interface do Visual FoxPro para relacionar tabelas.

# Exemplo

Um relacionamento um-para-muitos é o tipo mais comum de relacionamento em um banco de dados relacional. Em um relacionamento um-para-muitos, um registro na Tabela A pode ter mais de um registro correspondente na Tabela B, mas um registro na Tabela B tem, no máximo, um registro correspondente na Tabela A.

Por exemplo, as tabelas Category e Products no banco de dados Tasmanian Traders têm um relacionamento um-para-muitos.
 Um relacionamento um-para-muitos

Para configurar o relacionamento, você adiciona o campo ou os campos que compõem a chave primária no lado "um" do relacionamento à tabela no lado "muitos" do relacionamento. Você usa uma chave de índice primária ou candidata para o lado "um" do relacionamento e uma chave de índice regular para o lado "muitos". Neste caso, você adicionaria o campo Category_id da tabela Category à tabela Products, porque uma categoria inclui muitos produtos. O Visual FoxPro usa o número de identificação da categoria para localizar a categoria correta para cada produto.

Para obter mais informações, consulte Working with Tables (Visual FoxPro).

# Exemplo

Em um relacionamento muitos-para-muitos, um registro na Tabela A pode ter mais de um registro correspondente na Tabela B, e um registro na Tabela B pode ter mais de um registro correspondente na Tabela A. Esse tipo de relacionamento exige alterações no design do banco de dados antes que você possa especificar corretamente o relacionamento ao Visual FoxPro.

Para detectar relacionamentos muitos-para-muitos entre suas tabelas, é importante examinar ambas as direções do relacionamento. Por exemplo, considere o relacionamento entre pedidos e produtos no negócio Tasmanian Traders. Um pedido pode incluir mais de um produto. Portanto, para cada registro na tabela Orders, pode haver muitos registros na tabela Products. Mas isso não é tudo. Cada produto pode aparecer em muitos pedidos. Portanto, para cada registro na tabela Products, pode haver muitos registros na tabela Orders.
 Um relacionamento muitos-para-muitos

Os assuntos das duas tabelas — pedidos e produtos — têm um relacionamento muitos-para-muitos. Isso apresenta um desafio no design do banco de dados. Para entender o problema, imagine o que aconteceria se você tentasse configurar o relacionamento entre as duas tabelas adicionando o campo Product_id à tabela Orders. Para ter mais de um produto por pedido, você precisaria de mais de um registro na tabela Orders por pedido. Você estaria repetindo informações do pedido repetidamente para cada registro relacionado a um único pedido — um design ineficiente que poderia levar a dados imprecisos. Você encontra o mesmo problema se colocar o campo Order_id na tabela Products — você teria mais de um registro na tabela Products para cada produto. Para resolver esse problema, crie uma terceira tabela que divide o relacionamento muitos-para-muitos em dois relacionamentos um-para-muitos. Essa terceira tabela é chamada de tabela de junção, porque atua como a junção entre duas tabelas. Você coloca a chave primária de cada uma das duas tabelas na tabela de junção.
 A tabela Order_Line_Items cria um vínculo um-para-muitos entre Orders e Products

Uma tabela de junção pode conter apenas as duas chaves primárias das tabelas que ela vincula ou, como na tabela Order_Line_Items, a tabela de junção pode conter informações adicionais.

Cada registro na tabela Order_Line_Items representa um item de linha em um pedido. A chave primária da tabela Order_Line_Items consiste em dois campos — as chaves estrangeiras das tabelas Orders e Products. O campo Order_id sozinho não funciona como chave primária para esta tabela, porque um pedido pode ter muitos itens de linha. O ID do pedido é repetido para cada item de linha em um pedido, portanto o campo não contém valores exclusivos. O campo Product_id sozinho também não funciona, porque um produto pode aparecer em muitos pedidos diferentes. Mas juntos os dois campos na tabela de junção sempre produzem um valor exclusivo para cada registro. A tabela de junção não requer sua própria chave primária.

No banco de dados Tasmanian Traders, as tabelas Orders e Products não estão relacionadas diretamente. Em vez disso, elas estão relacionadas indiretamente por meio da tabela Order_Line_Items. O relacionamento muitos-para-muitos entre pedidos e produtos é representado no banco de dados usando dois relacionamentos um-para-muitos:
 - As tabelas Orders e Order_Line_Items têm um relacionamento um-para-muitos. Cada pedido pode ter mais de um item de linha, mas cada item de linha está conectado a apenas um pedido.
- As tabelas Products e Order_Line_Items têm um relacionamento um-para-muitos. Cada produto pode ter muitos itens de linha associados a ele, mas cada item de linha refere-se a apenas um produto.

# Exemplo

Em um relacionamento um-para-um, um registro na Tabela A pode ter no máximo um registro correspondente na Tabela B, e um registro na Tabela B pode ter no máximo um registro correspondente na Tabela A. Esse tipo de relacionamento é incomum e pode exigir algumas alterações no design do banco de dados.

Relacionamentos um-para-um entre tabelas são incomuns porque, em muitos casos, as informações nas duas tabelas podem simplesmente ser combinadas em uma tabela. Por exemplo, suponha que você criou uma tabela, chamada Ping-Pong Players, para rastrear informações sobre um evento de arrecadação de fundos de Ping-Pong da Tasmanian Traders. Como os jogadores de ping-pong são todos funcionários da Tasmanian Traders, esta tabela tem um relacionamento um-para-um com a tabela Employee no banco de dados Tasmanian Traders.
 Um relacionamento um-para-um

Você poderia adicionar todos os campos da tabela Ping-Pong Players à tabela Employee. Mas a tabela Ping-Pong Players rastreia um evento único, e você não precisará das informações depois que o evento terminar. Além disso, nem todos os funcionários jogam ping-pong, portanto, se esses campos estivessem na tabela Employee, estariam vazios para muitos registros. Por esses motivos, faz sentido criar uma tabela separada.

Quando você detecta a necessidade de um relacionamento um-para-um em seu banco de dados, considere se pode colocar as informações juntas em uma tabela. Por exemplo, na tabela Employee, um funcionário pode ter um gerente, que também é um funcionário. Você pode adicionar um campo para o número de identificação do gerente. Para reunir as informações posteriormente, você pode usar um self-join em sua consulta ou view. Você não precisa de uma tabela separada para resolver o relacionamento um-para-um. Se você não quiser fazer isso por algum motivo, veja como configurar o relacionamento um-para-um entre duas tabelas:
 - Se as duas tabelas têm o mesmo assunto, você provavelmente pode configurar o relacionamento usando o mesmo campo de chave primária em ambas as tabelas.
- Se as duas tabelas têm assuntos diferentes com chaves primárias diferentes, escolha uma das tabelas (qualquer uma) e coloque seu campo de chave primária na outra tabela como chave estrangeira.
