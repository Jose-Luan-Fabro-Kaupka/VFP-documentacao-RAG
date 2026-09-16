# Como: usar funções SQL Pass-Through

Seu aplicativo cliente/servidor pode acessar dados do servidor usando:
 - Remote views
- SQL pass-through

Remote views fornecem o método mais comum e mais fácil para acessar e atualizar dados remotos. Os assistentes de upsizing podem criar automaticamente remote views em seu banco de dados como parte do upsizing, ou você pode usar o Visual FoxPro para criar remote views após o upsizing. Para obter mais informações sobre remote views, consulte How to: Create Remote Views.

A tecnologia SQL pass-through permite enviar instruções SQL diretamente para um servidor. Instruções SQL pass-through, porque são executadas no servidor back-end, são maneiras poderosas de melhorar o desempenho de seus aplicativos cliente/servidor. A tabela a seguir compara remote views com SQL pass-through.
 Comparação das tecnologias Remote View e SQL Pass-Through
| Remote View | SQL Pass-Through |
| --- | --- |
| Baseada em uma instrução SQL SELECT. | Baseada em qualquer instrução SQL nativa do servidor, permitindo instruções de definição de dados ou execução de stored procedures em um servidor remoto. |
| Pode ser usada como fonte de dados para controles em tempo de design. | Não pode ser usada como fonte de dados para controles. |
| Não fornece capacidade de executar comandos DDL na fonte de dados. | Fornece método para usar comandos DDL na fonte de dados. |
| Busca um conjunto de resultados. | Busca um ou vários conjuntos de resultados. |
| Fornece gerenciamento de conexão integrado. | Requer gerenciamento de conexão explícito. |
| Fornece informações de atualização padrão integradas para atualizações, inserções e exclusões. | Não fornece informações de atualização padrão. |
| Fornece execução SQL implícita e busca de dados. | Fornece controle explícito de execução SQL e busca de resultados. |
| Não fornece tratamento de transações. | Fornece tratamento de transações explícito. |
| Armazena propriedades persistentemente no banco de dados. | Fornece propriedades temporárias para o cursor SQL pass-through, baseadas nas propriedades da sessão. |
| Emprega busca progressiva assíncrona ao executar SQL. | Suporta totalmente busca assíncrona programática. |

A tecnologia SQL pass-through oferece as seguintes vantagens sobre remote views:
 - Você pode usar funcionalidade específica do servidor, como stored procedures e funções intrínsecas baseadas no servidor.
- Você pode usar extensões ao SQL suportadas pelo servidor, bem como comandos de definição de dados, administração de servidor e segurança.
- Você tem mais controle sobre instruções Update, Delete e Insert de SQL pass-through.
- Você tem mais controle sobre transações remotas. Dica O Visual FoxPro pode lidar com consultas SQL pass-through que retornam mais de um único conjunto de resultados.

Consultas SQL pass-through também têm desvantagens:
 - Por padrão, uma consulta SQL pass-through sempre retorna um instantâneo não atualizável de dados remotos, que é armazenado em um cursor de view ativo. Você pode tornar o cursor atualizável definindo propriedades com a função CURSORSETPROP( ) . Uma remote view atualizável, em contraste, geralmente não requer que você defina propriedades antes de poder atualizar dados remotos, porque as configurações de propriedade são armazenadas no banco de dados com a definição da view.
- Você deve inserir comandos SQL diretamente na janela Command ou em um programa, em vez de usar o View Designer gráfico.
- Você cria e gerencia a conexão com a fonte de dados.

Seja usando remote views ou SQL pass-through, você pode consultar e atualizar dados remotos. Em muitos aplicativos, você usará ambos remote views e SQL pass-through.

# Usando funções SQL Pass-Through

Para usar SQL pass-through para conectar a uma fonte de dados ODBC remota, primeiro chame a função Visual FoxPro SQLCONNECT( ) para criar uma conexão. Em seguida, use as funções SQL pass-through do Visual FoxPro para enviar comandos à fonte de dados remota para execução.

### Para usar funções SQL pass-through do Visual FoxPro
- Confirme a capacidade do sistema de conectar seu computador à fonte de dados. Use um utilitário como ODBC Test para ODBC.
- Estabeleça uma conexão com sua fonte de dados com a função SQLCONNECT( ) ou a função SQLSTRINGCONNECT( ) . Por exemplo, se você estiver conectando o Visual FoxPro à fonte de dados SQL Server sqlremote , pode fazer logon com o seguinte comando: nConnectionHandle = SQLCONNECT('sqlremote','<userid>','<password>') Observação Você também pode usar a função SQLCONNECT() para conectar a uma conexão nomeada.
- Use funções SQL pass-through do Visual FoxPro para recuperar dados em cursors do Visual FoxPro e processar os dados recuperados com comandos e funções padrão do Visual FoxPro. Por exemplo, você pode consultar a tabela authors e examinar o cursor resultante usando este comando: ? SQLEXEC(nConnectionHandle,"select * from authors","mycursorname") BROWSE
- Desconecte da fonte de dados com a função SQLDISCONNECT( ).
