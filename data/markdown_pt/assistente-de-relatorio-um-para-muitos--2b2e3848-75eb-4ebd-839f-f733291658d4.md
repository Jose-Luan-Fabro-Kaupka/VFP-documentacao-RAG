# Assistente de relatório um-para-muitos

Você pode criar um relatório que agrupa registros de uma tabela pai com registros de uma tabela filha, por exemplo, nomes e endereços de uma tabela Customer e valores e descontos de uma tabela Orders, usando o Assistente de relatório um-para-muitos. Para obter informações sobre como iniciar o Assistente de relatório um-para-muitos, consulte Como: criar relatórios (Visual FoxPro) e Trabalhando com relatórios.

# Etapa 1 - Selecionar campos da tabela pai

Nesta etapa, você escolhe uma tabela livre ou tabela ou exibição de um banco de dados que fornecerá os dados dos campos de controle apresentados no relatório. Isso especifica qual campo da tabela pai ou de controle determina os registros selecionados na tabela filha ou controlada. Você pode selecionar campos de uma única tabela ou exibição somente.

# Etapa 2 - Selecionar campos da tabela filha

Nesta etapa, você escolhe os campos da tabela relacionada. Esta etapa determina quais campos de uma tabela filha ou controlada são exibidos no formulário. Por exemplo, a tabela pai pode conter apenas nomes de clientes, números de ID e endereços, e a tabela filha pode conter informações de pedidos, como números de ID, valor, data, desconto e assim por diante. Um cliente pode ter muitos pedidos.

Você pode selecionar campos de uma única tabela filha ou exibição somente.

# Etapa 3 – Relacionar tabelas

Nesta etapa, você especifica na lista de campos como as tabelas pai e filha estão relacionadas. No exemplo da etapa 2, ambas as tabelas contêm o campo de ID do cliente, então essa é uma forma de relacioná-las. Pode haver outras formas dependendo dos campos disponíveis e do que você deseja relatar.

# Etapa 4 – Classificar registros

Nesta etapa, você pode selecionar na tabela pai os campos na ordem em que deseja classificar os registros. Por exemplo, se você estiver usando dois campos e tiver um campo de primeiro nome e um campo de sobrenome, pode escolher classificar por primeiro nome+sobrenome (como PaulWilson) ou por sobrenome+primeiro nome (como WilsonPaul). A forma de classificação é determinada pela ordem em que você selecionou esses campos.

Se sua tabela já possui um ou mais índices, você pode selecionar a tag de índice, que é listada abaixo dos campos, separada por uma linha, na janela Campos disponíveis.

# Etapa 5 - Escolher estilo do relatório

Nesta etapa, você pode escolher o formato básico do formulário entre os estilos integrados ao assistente. Quando você clica em qualquer um dos estilos, o assistente atualiza o gráfico na lupa como exemplo do estilo.

O botão Opções de resumo permite especificar se o relatório incluirá um ou mais cálculos, como soma ou média, em campos disponíveis.

Você também pode escolher se o relatório será exibido ou impresso em orientação retrato ou paisagem.

# Etapa 6 - Concluir

Nesta etapa, você pode escolher como e quando usar o relatório.
 **Salvar relatório para uso posterior**
Permite salvar o relatório como um arquivo, que você pode abrir depois.
**Salvar relatório e modificar no Designer de relatórios**
Salva o relatório como um arquivo e depois o abre no Designer de relatórios, para que você possa fazer modificações.
**Salvar e imprimir relatório**
Salva o relatório como um arquivo e depois imprime imediatamente.

Se você selecionar Usar configurações de exibição armazenadas no banco de dados, o relatório usa informações do banco de dados.

Se o número de campos selecionados não couber em uma única linha dentro da largura do relatório, os campos serão quebrados para a linha seguinte. Se não desejar que os campos sejam quebrados, desmarque a caixa de seleção Quebrar campos que não cabem. Clique no botão Visualizar para ver o relatório sem sair do assistente.

Depois de salvar o relatório, você pode abri-lo e modificá-lo como qualquer outro relatório no Designer de relatórios.
