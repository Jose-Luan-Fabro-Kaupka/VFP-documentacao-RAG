# Configuração das propriedades de exibição e conexão

Ao criar uma exibição, ela herda as configurações de propriedades do cursor de ambiente, que é o cursor 0 da sessão de dados atual. Você pode alterar essas configurações usando CURSORSETPROP( ) com 0 como número do cursor. Depois que a exibição é criada e armazenada em um banco de dados, suas propriedades podem ser alteradas com DBSETPROP( ). Essas alterações são armazenadas de forma persistente no banco de dados.

Ao usar uma exibição, o cursor ativo herda as configurações armazenadas no banco de dados. Você pode alterá-las temporariamente no cursor ativo usando CURSORSETPROP( ). As configurações temporárias da exibição desaparecem quando ela é fechada; as do cursor 0 desaparecem quando a sessão do Visual FoxPro é encerrada.

As conexões herdam propriedades de maneira semelhante. As propriedades padrão da conexão 0 são herdadas ao criar e armazenar uma conexão nomeada em um banco de dados. Você pode alterar essas propriedades padrão com SQLSETPROP( ). Depois que a conexão é criada e armazenada, suas propriedades podem ser alteradas com DBSETPROP( ). Ao usar uma conexão, a conexão ativa herda as configurações armazenadas. Você pode alterá-las usando SQLSETPROP( ) com o identificador da conexão.

Exibições e conexões podem usar uma fonte de dados ODBC nomeada. Se uma fonte ODBC for usada em uma exibição, a conexão herdará propriedades dos padrões da sessão.

O diagrama a seguir ilustra a herança de propriedades de exibições e conexões. As linhas cinzas representam o fluxo de herança; as linhas pretas representam comandos do Visual FoxPro.
 Propriedades de exibição e conexão e sua herança
