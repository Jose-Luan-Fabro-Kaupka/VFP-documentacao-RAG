# Relacionamentos Temporários Entre Tabelas

Você pode usar áreas de trabalho e aliases de tabela para criar relacionamentos temporários entre tabelas. Relacionamentos temporários fazem com que o ponteiro de registro em uma tabela, conhecida como tabela filha, siga os movimentos do ponteiro de registro em outra tabela, conhecida como tabela pai. Por exemplo, suponha que você deseja estabelecer um relacionamento entre uma tabela de clientes e uma tabela de pedidos para que, quando você mover o ponteiro de registro na tabela de clientes para um cliente específico, o ponteiro de registro na tabela de pedidos se mova para o registro com o mesmo número de cliente.

Você pode criar diferentes relacionamentos entre tabelas. Por exemplo, em um relacionamento um-para-muitos, você pode selecionar um registro na tabela pai ou no lado "um" do relacionamento e acessar vários registros relacionados na tabela filha ou no lado "muitos" do relacionamento. Para mais informações sobre os relacionamentos que você pode criar, consulte Identifying Relationships.

Normalmente, você define um relacionamento temporário entre tabelas que possuem um campo comum usando uma expressão relacional. A expressão relacional é normalmente a expressão de índice do índice controlador na tabela filha. Portanto, quando você cria um relacionamento entre a tabela pai e o índice da tabela filha, selecionar um registro na tabela pai seleciona apenas os registros na tabela filha cuja chave de índice corresponde à chave de índice do registro pai que você seleciona.

Depois de abrir tabelas e criar relacionamentos, você pode visualizar os aliases e relacionamentos dessas tabelas na janela Data Session.
 Abrir aliases de tabela e relacionamentos temporários na janela Data Session

# Relacionamentos em Tabelas Únicas

Você também pode criar um relacionamento entre registros em uma única tabela, ou uma relação auto-referencial. Este tipo de relacionamento pode ser útil quando você tem todas as informações necessárias em uma única tabela. Por exemplo, suponha que você tenha uma tabela de funcionários. Ao criar um relacionamento auto-referencial na tabela, você pode selecionar registros de funcionários para aqueles funcionários que se reportam a cada gerente conforme você navega para cada registro de gerente na tabela.

# Relacionamentos Entre Tabelas em um Data Environment

Se você estiver usando um formulário para trabalhar com tabelas, pode usar o data environment do formulário para criar e armazenar esses relacionamentos com o formulário. Relacionamentos que você cria no data environment abrem automaticamente quando você executa o formulário. Para informações sobre como criar um data environment, consulte Creating Forms.
