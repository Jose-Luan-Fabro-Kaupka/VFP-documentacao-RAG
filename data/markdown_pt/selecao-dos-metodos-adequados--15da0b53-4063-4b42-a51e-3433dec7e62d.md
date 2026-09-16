# Seleção dos métodos adequados

Você pode usar exibições remotas, SQL pass-through ou ambos para criar um aplicativo cliente/servidor. Combine os dois para obter resultados eficientes: use exibições para a maioria das necessidades de gerenciamento de dados e SQL pass-through para ampliar os recursos do aplicativo.

# Uso de exibições

As exibições podem ser o método principal para desenvolver um aplicativo cliente/servidor robusto. Exibições remotas permitem selecionar apenas os dados necessários de um servidor remoto em um cursor local do Visual FoxPro, que pode então ser usado para exibir e atualizar os dados remotos. Uma exibição é basicamente um conjunto de resultados de uma instrução SQL SELECT.

As exibições são persistentes: sua definição é armazenada em um banco de dados. As definições possuem propriedades que podem ser configuradas e personalizadas para o cursor de exibição ativo. Exibições são a melhor ferramenta para definir um conjunto de resultados atualizável.

Você pode usar exibições locais para criar um protótipo e depois usar um Upsizing Wizard para transformá-las em exibições remotas. Para obter mais informações, consulte Upsizing de bancos de dados do Visual FoxPro.

Se os usuários precisarem usar dados em trabalho móvel, use exibições offline. Elas tornam os dados portáteis, permitindo trabalhar com uma cópia armazenada dos dados de origem e atualizá-la durante viagens. Ao se reconectar ao servidor, o aplicativo pode mesclar facilmente as alterações offline nas tabelas de origem.

Você também pode usar essa tecnologia para permitir que usuários locais trabalhem "offline" e mesclem as atualizações posteriormente. Para obter mais informações, consulte Manipulação de dados offline.

# Uso de SQL pass-through

A tecnologia SQL pass-through oferece acesso direto a um servidor remoto por meio das funções SQL pass-through do Visual FoxPro. Elas fornecem acesso e controle adicionais além das exibições. Por exemplo, permitem definir dados no servidor remoto, definir propriedades do servidor e acessar procedimentos armazenados.

SQL pass-through é a melhor ferramenta para criar conjuntos de resultados somente leitura e usar qualquer outra sintaxe SQL nativa. Ao contrário de uma exibição, que é um resultado de SQL SELECT, SQL pass-through permite enviar qualquer conteúdo ao servidor com a função SQLEXEC( ). A tabela a seguir lista as funções SQL pass-through.
 Funções SQL pass-through
| SQLCANCEL( ) | SQLCOLUMNS( ) | SQLCOMMIT( ) |
| --- | --- | --- |
| SQLCONNECT( ) | SQLDISCONNECT( ) | SQLEXEC( ) |
| SQLGETPROP( ) | SQLMORERESULTS( ) | SQLPREPARE( ) |
| SQLROLLBACK( ) | SQLSETPROP( ) | SQLSTRINGCONNECT( ) |
| SQLTABLES( ) | | |

Você pode criar cursores com SQL pass-through. Embora ofereça acesso mais direto ao servidor, ele é menos persistente que as exibições. As definições de exibições ficam armazenadas no banco de dados, enquanto os cursores criados com SQL pass-through existem apenas durante a sessão atual. Para obter mais informações, consulte Aprimoramento de aplicativos com a tecnologia SQL pass-through.

# Combinação de exibições e SQL pass-through

O paradigma mais eficiente para criar um aplicativo cliente/servidor do Visual FoxPro combina as duas tecnologias. Como as exibições são fáceis de criar e oferecem buffering e atualização automáticos, use-as na maioria das tarefas de gerenciamento de dados. Use SQL pass-through para tarefas específicas no servidor remoto, como definição de dados e criação e execução de procedimentos armazenados.
