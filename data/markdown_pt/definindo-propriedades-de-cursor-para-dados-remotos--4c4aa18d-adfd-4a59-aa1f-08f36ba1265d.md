# Definindo propriedades de cursor para dados remotos

A tabela a seguir lista as propriedades de cursor do Visual FoxPro que suportam trabalho com views e conjuntos de resultados conectados, agrupadas por categorias de tarefa.
 Propriedades de cursor do Visual FoxPro
| Tarefa | Propriedade | Finalidade |
| --- | --- | --- |
| Definição de cursor de view. | SQL | Contém a instrução SQL da qual o cursor foi criado. |
| Controlar interações entre Visual FoxPro e ODBC. | ConnectHandle | Identificador da conexão remota usada pelo cursor. |
| ConnectName | Nome da conexão usada pelo cursor. | |
| Prepare | Especifica se a query da view é preparada antes de ser executada. | |
| FetchAsNeeded | Especifica se as linhas são buscadas automaticamente durante o loop ocioso ou apenas conforme necessário. | |
| CompareMemo | Especifica se campos Memo e General participam da cláusula WHERE de uma instrução UPDATE, independentemente da configuração da propriedade UpdateType | |
| FetchMemo | Especifica se campos Memo e General são buscados automaticamente com conjuntos de resultados ou buscados posteriormente, sob demanda, quando o campo Memo ou General é aberto. | |
| UseMemoSize | Especifica o tamanho mínimo da coluna (1 a 255) em conjuntos de resultados para os quais as colunas são retornadas em campos Memo. | |
| FetchSize | Especifica o número de linhas buscadas de uma vez do conjunto de resultados remoto. | |
| MaxRecords | Especifica o número máximo de linhas buscadas quando conjuntos de resultados são retornados. | |
| Atualizar dados | SendUpdates* | Especifica se atualizações no cursor são enviadas às tabelas nas quais o cursor se baseia. |
| BatchUpdateCount | Especifica o número de instruções de atualização enviadas ao back end para tabelas em buffer. | |
| Tables* | Lista separada por vírgulas de nomes de tabelas na fonte de dados; usada para definir o escopo das propriedades UpdateNameList e UpdatableFieldsList. | |
| KeyFieldList* | Lista separada por vírgulas de campos do Visual FoxPro que representam a chave primária do conjunto de resultados usado para atualizações. | |
| UpdateNameList* | Lista separada por vírgulas que emparelha campos do Visual FoxPro no cursor com os nomes de tabela e coluna dos campos aos quais você deseja enviar atualizações. | |
| UpdatableFieldList* | Lista separada por vírgulas dos campos do Visual FoxPro para os quais atualizações são enviadas. | |
| Buffering | Especifica o tipo de buffering sendo realizado no cursor. | |
| UpdateType | Especifica se as atualizações devem ocorrer usando comandos UPDATE ou DELETE e depois INSERT. | |
| WhereType | Especifica o que deve ser incluído na cláusula WHERE para atualizações de dados de tabela. | |

* Propriedades que devem ser definidas antes que você possa atualizar dados.

Você usa essas propriedades para controlar a forma como seu aplicativo interage com dados remotos, como estabelecer o número de linhas recuperadas durante a busca progressiva e controlar buffering e atualizações de dados remotos.

# Usando a guia Remote Data na caixa de diálogo Opções

Algumas propriedades de cursor herdam seus valores iniciais do ambiente; outras propriedades só ficam disponíveis no nível do cursor. Algumas propriedades estão disponíveis para cursors que representam views remotas e tabelas conectadas por ODBC ou SQL pass-through.

Você pode controlar algumas configurações de propriedade de cursor e conexão através da guia Remote Data da caixa de diálogo Opções. Quando você exibe a guia Remote Data, os valores na caixa de diálogo representam as configurações de cursor da sessão atual e as configurações padrão globais do Visual FoxPro para a conexão. Quando você altera valores na guia Remote Data e escolhe OK, os novos valores são salvos na sessão atual do cursor e nas configurações padrão globais da conexão. Se você escolher Definir como padrão, os valores são gravados nas configurações de sistema configuráveis em sua máquina. O diagrama a seguir ilustra essas interações.
 Exibir e definir configurações globais e de sessão com a caixa de diálogo Opções

# Definindo propriedades com SQL Pass-Through

Quando você cria um cursor, o cursor herda configurações de propriedade, como UpdateType e UseMemoSize, do cursor de ambiente, ou cursor 0 da sessão atual. Você pode alterar essas configurações de propriedade padrão usando a Função CURSORSETPROP( ) com 0 como número do cursor.

Depois de criar um cursor de view com SQL pass-through, você pode alterar as configurações de propriedade do cursor ativo usando a função CURSORSETPROP( ) para o cursor de view. As alterações feitas com CURSORSETPROP( ) são temporárias: as configurações temporárias para a view ativa desaparecem quando você fecha a view, e as configurações temporárias para o cursor 0 desaparecem quando você fecha a sessão do Visual FoxPro.

As conexões herdam propriedades de forma semelhante. As propriedades padrão para a conexão 0 são herdadas quando você cria e armazena uma conexão nomeada em um banco de dados. Você pode alterar essas configurações de propriedade padrão para a conexão 0 com a Função SQLSETPROP( ) . Depois que a conexão foi criada e está armazenada em um banco de dados, você pode alterar propriedades de conexão com a Função DBSETPROP( ) . Quando você usa uma conexão, as configurações de propriedade armazenadas para a conexão no banco de dados são herdadas pela conexão ativa. Você pode alterar essas propriedades na conexão ativa usando a função SQLSETPROP( ) para o identificador de conexão.

Tanto cursors de view SQL pass-through quanto conexões nomeadas podem usar uma fonte de dados ODBC nomeada. Se você usa uma fonte de dados ODBC em um cursor de view SQL pass-through, a conexão herda propriedades dos padrões da sessão.

O diagrama a seguir ilustra a herança de propriedades para cursors e conexões criados com SQL pass-through. As linhas cinzas representam o fluxo de herança de propriedades; as linhas pretas representam comandos do Visual FoxPro.
 Herança de propriedades de conexão e cursor SQL pass-through (SPT)
