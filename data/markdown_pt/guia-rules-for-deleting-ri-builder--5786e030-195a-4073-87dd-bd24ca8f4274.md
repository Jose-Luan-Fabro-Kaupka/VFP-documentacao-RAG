# Guia Rules for Deleting, RI Builder

Esta guia no Referential Integrity (RI) builder especifica regras a serem aplicadas quando um registro na tabela pai é excluído.
 **Cascade**
Especifica que exclusões na tabela pai são refletidas nas tabelas filhas relacionadas. Se você selecionar Cascade Delete para um relacionamento, sempre que excluir registros na tabela pai, os registros na tabela filha relacionada são automaticamente excluídos.
**Restrict**
Impede que você exclua registros na tabela pai que tenham registros relacionados na tabela filha. Se você selecionar Restrict Delete para um relacionamento, uma tentativa de excluir registros na tabela pai gera um erro se houver registros relacionados na tabela filha.
**Ignore**
Permite que você exclua registros na tabela pai, mesmo se houver registros relacionados na tabela filha.
**Referential Integrity Grid**
Parent Table exibe o nome da tabela na relação do banco de dados que contém o índice primário ou candidato. Child Table exibe o nome da tabela filha na relação do banco de dados. Update exibe as regras de atualização de integridade referencial para a relação. Os valores possíveis são Cascade, Restrict ou Ignore. Você pode alterar as configurações selecionando o campo, o que apresentará uma lista suspensa das opções. Delete exibe as regras de exclusão de integridade referencial para a relação. Os valores possíveis são Cascade, Restrict ou Ignore. Você pode alterar as configurações selecionando o campo, o que apresentará uma lista suspensa das opções. Insert exibe as regras de inserção de integridade referencial para a relação. Os valores possíveis são Cascade, Restrict ou Ignore. Você pode alterar as configurações selecionando o campo, o que apresentará uma lista suspensa das opções. A coluna de grade Parent Tag exibe o nome da tag do índice Primary ou Candidate na tabela pai. A coluna de grade Child Tag exibe o nome da tag do índice na tabela filha.
