# Desenvolvendo e modificando bancos de dados em equipes

Além de trabalhar em conjunto com projetos e arquivos de projeto, sua equipe deve ser capaz de compartilhar informações em bancos de dados. Trabalhar com bancos de dados em equipe envolve não apenas as questões de controle de concorrência ordinário para dados em tabelas, mas também a necessidade de compartilhar informações de controle de banco de dados.

Para que vários desenvolvedores trabalhem com um banco de dados ao mesmo tempo, eles devem ser capazes de compartilhar o arquivo de banco de dados (.dbc). No Visual FoxPro, o arquivo .dbc pode ser compartilhado entre desenvolvedores como uma tabela de dados comum. O arquivo .dbc deve, portanto, ser armazenado centralmente com as tabelas que compõem o banco de dados. Os desenvolvedores não devem manter cópias locais de um arquivo .dbc porque as alterações que fazem no banco de dados não serão refletidas nas versões do arquivo de outros desenvolvedores.

Se você precisar alterar o arquivo .dbc, observe as seguintes restrições:
 - Os desenvolvedores não podem modificar o mesmo elemento de banco de dados (como uma estrutura de tabela, view ou conexão) ao mesmo tempo. Quando um desenvolvedor modifica um elemento de banco de dados, o Visual FoxPro bloqueia sua entrada no arquivo .dbc; outros usuários podem ler a entrada (ou seja, podem emitir um comando USE), mas não podem modificá-la (MODIFY STRUCTURE).
- Se um elemento de banco de dados está em uso, você não pode modificar sua estrutura. Por exemplo, se um desenvolvedor tem uma tabela aberta, nenhum outro desenvolvedor pode modificar sua estrutura.
- Se você chamar a função DBSETPROP( ) para alterar as propriedades de um banco de dados, a função coloca um bloqueio de gravação no objeto sendo atualizado. Se houver um conflito de bloqueio, DBSETPROP( ) segue as regras estabelecidas com SET REPROCESS .

# Trabalhando com views e conexões

Views e conexões funcionam de maneira um pouco diferente das tabelas. Quando você está definindo a view pela primeira vez, o Visual FoxPro usa as tabelas em um banco de dados, mas não as bloqueia. No entanto, como as tabelas estão em uso, outros desenvolvedores não podem modificar suas estruturas.

A partir do momento em que você salva uma nova definição de view ou conexão, o Visual FoxPro a bloqueia exclusivamente até que você feche o View Designer ou Connection Designer. Em outras palavras, enquanto você tem a view ou conexão aberta em um designer, ela está bloqueada exclusivamente. Enquanto a view estiver bloqueada, ninguém mais pode modificá-la.

Quando você usa uma view, sua estrutura é armazenada em cache localmente. Isso garante que, se a view for modificada enquanto você a estiver usando — por exemplo, se você chamar REFRESH( ) ou REQUERY( ) — seu formulário ou relatório continue a ser executado corretamente.
