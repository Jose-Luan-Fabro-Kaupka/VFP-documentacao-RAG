# Melhoria de Desempenho em Updates e Deletes

Você pode acelerar instruções Update e Delete:
 - Adicionando timestamps às suas tabelas remotas.
- Usando a propriedade CompareMemo.
- Usando o modo de transação manual.
- Usando procedimentos armazenados em um servidor remoto.
- Agrupando atualizações em lote.

# Adicionando Timestamps

Você pode melhorar o desempenho ao atualizar, inserir ou excluir dados em uma tabela remota que contém muitos campos adicionando um campo timestamp à tabela remota, se o seu servidor fornecer o tipo de campo Timestamp.

A presença de um campo timestamp em uma tabela remota permite usar a opção de atualização SQL WhereType DB_KEYANDTIMESTAMP do Visual FoxPro. Esta opção economiza tempo de processamento porque o Visual FoxPro compara apenas dois campos na sua view, o campo de chave e o campo timestamp, contra uma tabela remota para detectar conflitos de atualização. Ao comparar apenas dois campos, em vez de todos os campos atualizáveis (com a opção DB_KEYANDUPDATABLE) ou todos os campos modificados (com a opção DB_KEYANDMODIFIED), a opção DB_KEYANDTIMESTAMP reduz o tempo necessário para atualizar dados remotos. Para obter mais informações sobre opções WhereType, consulte Gerenciando Atualizações Usando Views.

> **Observação:** A opção DB_KEYANDTIMESTAMP compara os campos de chave e timestamp apenas quando sua tabela remota contém um campo timestamp. Se você usar a opção DB_KEYANDTIMESTAMP contra uma tabela remota que não contém um campo timestamp, o Visual FoxPro compara apenas os campos de chave.

O Upsizing Wizard pode adicionar automaticamente campos timestamp conforme apropriado às tabelas que você exporta. Para obter mais informações, consulte "Timestamp Columns" em Upsizing Visual FoxPro Databases.

> **Dica:** Se você fizer algo que altere a estrutura da tabela base de uma view, como adicionar um campo timestamp, pode ser necessário recriar a view. Os campos em uma definição de view são armazenados no banco de dados, e quaisquer alterações nas tabelas base de uma view após o uso da view não são refletidas na definição da view até que você recrie a view.

# Excluindo Campos Memo da Cláusula Update WHERE

Quando apropriado, você pode acelerar atualizações impedindo que campos memo da view (campos do tipo Memo, General ou Picture) sejam comparados com suas contrapartes na tabela base. Por padrão, a propriedade CompareMemo é definida como true (.T.), o que inclui automaticamente campos memo na cláusula SQL WHERE gerada quando você cria uma view atualizável. Você pode definir a propriedade CompareMemo como false (.F.) para excluir memos da cláusula SQL WHERE.

# Usando Transações

Para desempenho ideal, use o modo de transação manual e gerencie as transações você mesmo. O modo de transação manual permite controlar quando você confirma um grupo de transações, o que permite ao servidor processar mais instruções rapidamente.

O modo de transação automática é mais demorado, porque por padrão cada instrução de atualização individual é encapsulada em uma transação separada. Este método fornece controle máximo sobre cada instrução de atualização individual, mas também aumenta a sobrecarga.

Você pode melhorar o desempenho no modo de transação automática aumentando a configuração da propriedade BatchUpdateCount na view ou cursor. Quando você usa uma configuração grande de BatchUpdateCount, muitas instruções de atualização são agrupadas em uma única instrução de atualização, que é então encapsulada em uma única transação. No entanto, se qualquer instrução no lote falhar, todo o lote é revertido.

> **Dica:** A propriedade BatchUpdateCount não é suportada por alguns servidores; você deve testar esta propriedade contra cada servidor remoto antes de implantá-la no seu aplicativo.

# Usando Procedimentos Armazenados no Servidor

Você pode criar procedimentos armazenados no servidor, que são pré-compilados e, portanto, executam muito rapidamente. Você pode executar procedimentos armazenados, enviar parâmetros com SQL pass-through e mover processamento adicional para o servidor conforme apropriado para seu aplicativo.

Por exemplo, você pode querer coletar entrada do usuário localmente e depois executar uma consulta SQL pass-through para enviar os dados ao servidor, chamando o procedimento armazenado apropriado. Para fazer isso, você pode querer criar um formulário em um cursor ou matriz local para coletar dados e depois escrever código que constrói uma instrução da Função SQLEXEC( ) usando o nome do procedimento armazenado e os parâmetros a serem fornecidos. Você pode então adicionar este código ao evento Click de um botão de comando intitulado "OK" ou "Commit." Quando o usuário escolhe o botão, a instrução SQLEXEC( ) é executada. Usar procedimentos armazenados em um servidor remoto para atualizar dados remotos pode ser mais eficiente, porque os procedimentos armazenados são compilados no servidor.

# Agrupando Atualizações em Lote

Se seu aplicativo atualiza vários registros, você pode querer agrupar atualizações para que sejam tratadas de forma mais eficiente pela rede e pelo servidor. Instruções Update ou Insert são agrupadas em lote antes de serem enviadas ao servidor, conforme a configuração da propriedade BatchUpdateCount da view. O valor padrão é 1, o que significa que cada registro é enviado ao servidor com uma instrução de atualização. Você pode reduzir o tráfego de rede aumentando o valor para empacotar várias atualizações em uma instrução.

> **Dica:** A propriedade BatchUpdateCount não é suportada por alguns servidores; você deve testar esta propriedade contra cada servidor remoto antes de implantá-la no seu aplicativo.

Para usar este recurso de forma eficiente, a conexão da view deve ser definida para o modo Buffering 5, para buffer de tabela otimista, e as alterações idealmente devem ser limitadas aos mesmos campos em cada linha do cursor. Você pode usar a Função DBSETPROP( ) para definir a propriedade BatchUpdateCount para a definição da view; para alterar o valor para um cursor de view ativo, use a Função CURSORSETPROP( ).

# Otimizando o Desempenho de Updates e Deletes

Você pode usar as seguintes diretrizes para definir propriedades de view e conexão para otimizar o desempenho de updates e deletes. A propriedade BatchSize na sua view tem a maior influência no desempenho.

| Objeto | Propriedade | Configuração | Observações |
| --- | --- | --- | --- |
| View | BatchUpdateCount | 10 – 30 linhas | Defina um valor maior para atualizações de menor tamanho.1 Defina para aumentar o desempenho em até 50%. O padrão é 1. |
| Connection | Asynchronous | (.F.) | Use conexões síncronas para aumentar o desempenho em até 50%, a menos que você deseje poder cancelar instruções SQL durante a execução no servidor. O padrão é síncrono. |
| Connection | WaitTime | N/A | Para aumentar o desempenho no modo assíncrono, use um tempo de espera menor; para reduzir o tráfego de rede, aumente o tempo de espera. |
| Connection | PacketSize | 4K a 12K | Tem pouco efeito no desempenho. |

1 Seu melhor valor também depende da velocidade do seu servidor.

O desempenho real depende muito da configuração do seu sistema e dos requisitos do aplicativo.
