# Guia Tabela, Table Designer

A guia Tabela aparece no Table Designer (Visual FoxPro). Ela contém informações somente leitura sobre a tabela e áreas para definir a regra em nível de registro e o texto de erro de validação, triggers e comentários.

> **Observação:** Se você estiver modificando uma tabela livre, apenas as estatísticas somente leitura da tabela são exibidas nesta guia. Tabelas livres não podem ter regras, triggers ou comentários associados.
 **Name**
Especifica o nome da tabela que está sendo criada ou modificada. Para tabelas de banco de dados, o nome da tabela aparece no Project Manager; não é o nome do arquivo. Nomes longos de até 128 caracteres são suportados.
**Database**
Exibe o nome do banco de dados ao qual a tabela pertence se a tabela não for uma tabela livre. Esta caixa é somente leitura.

# Estatísticas

Exibe informações somente leitura sobre a tabela.
 **Table file**
Exibe o caminho e o nome do arquivo da tabela.
**Records**
Exibe a quantidade de linhas atualmente armazenadas na tabela.
**Fields**
Exibe a quantidade de colunas definidas na estrutura da tabela.
**Length**
Exibe o comprimento da tabela.

# Validação de registro

Define a regra em nível de linha, o texto de erro de validação e um comentário para a tabela. O botão à direita de cada configuração exibe a Caixa de diálogo Expression Builder.
 **Validation Rule**
Especifica uma regra em nível de registro para impor validação de dados.
**Validation Text**
Especifica a mensagem de erro a ser exibida se uma entrada não estiver em conformidade com a regra de validação em nível de registro.

# Triggers

Especifica regras para atualizações, inserções e exclusões.
 **INSERT Trigger**
Especifica uma regra a ser acionada sempre que um registro é inserido ou anexado à tabela. Clique no botão de diálogo para exibir a Caixa de diálogo Expression Builder .
**UPDATE Trigger**
Especifica uma regra a ser acionada sempre que um registro é atualizado na tabela. Clique no botão de diálogo para exibir a Caixa de diálogo Expression Builder .
**DELETE Trigger**
Especifica uma regra a ser acionada sempre que um registro é excluído da tabela. Clique no botão de diálogo para exibir a Caixa de diálogo Expression Builder .
**Table Comment**
Fornece espaço para você digitar um comentário sobre a tabela. O que você digitar aqui aparece como a descrição na parte inferior do Project Manager quando esta tabela é selecionada.
