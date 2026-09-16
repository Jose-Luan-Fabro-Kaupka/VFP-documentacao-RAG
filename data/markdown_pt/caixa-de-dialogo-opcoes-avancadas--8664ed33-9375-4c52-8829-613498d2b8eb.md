# Caixa de Diálogo Opções Avançadas

Permite ajustar com precisão como os registros são recuperados em uma view ou como as atualizações são feitas no servidor ou nas tabelas de origem. Este comando está disponível apenas com views.

# Informações de Conexão
 **Nome da Conexão/Fonte de dados**
Exibe o nome da conexão ou fonte de dados usada para acessar os dados na view.
**Share Connection**
Especifica que o Visual FoxPro deve usar a mesma conexão para novas views que você criar. Esta opção se aplica apenas a dados remotos (ODBC). Se você já tem uma conexão configurada, pode definir esta opção como Uses Current Connection para novas views.

# Recuperação de Dados
 **Número de Registros a Recuperar de Cada Vez**
Controla quantos registros são retornados de cada vez do servidor ODBC ou da fonte de dados remota. Por exemplo, se você executar uma consulta que retorna 1000 registros e definir esta opção como 100, os primeiros 100 registros serão exibidos quando você executar a view, e os registros restantes serão recuperados em blocos de 100 conforme você continuar navegando pelos resultados. Clicar em All define este valor como –1, indicando que todos os registros devem ser retornados na primeira operação de recuperação.
**Número Máximo de Registros a Recuperar**
Limita o número total de registros retornados por uma view. Clicar em All define este valor para indicar que todos os registros devem ser retornados.
**Usar Memo Quando o Comprimento do Campo Character >=**
Determina quando campos character longos devem ser convertidos em campos Memo na saída da sua view.

# Desempenho
 **Número de Registros para Atualização em Lote**
Especifica o número de registros a atualizar com um único comando. Para obter mais informações, consulte o comando REPLACE e Cláusulas de Escopo.
**Fetch Memo**
Recupera campos Memo da fonte de dados somente quando um campo memo é ativado na saída da view.
**Fetch remote data as needed**
Desabilita a recuperação progressiva e recupera linhas apenas conforme necessário
**Include Memo Fields in WHERE Clause**
Especifica que, quando o Visual FoxPro compara um registro mantido localmente com um no servidor, ele verifica alterações; campos memo devem ser incluídos nesta comparação. Algumas fontes de dados não suportam esta opção; neste caso, incluir um campo memo pode fazer o servidor relatar alterações, mesmo se os registros forem iguais.
**Precompile SQL on Back-end Server**
Especifica que o Visual FoxPro passe a consulta SQL ao servidor para ser compilada antes de ser executada. Se o servidor suportar esta opção, as consultas podem ser executadas substancialmente mais rápido do que se não forem compiladas.
