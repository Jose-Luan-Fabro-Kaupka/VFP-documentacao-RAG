# Guia Rules for Inserting, RI Builder

Esta guia no Referential Integrity (RI) builder especifica regras a serem aplicadas quando um novo registro é inserido ou um registro existente é atualizado na tabela filha.
 **Restrict**
Impede que você adicione registros na tabela filha para os quais não existam registros correspondentes na tabela pai. Se você selecionar Restrict Insert para um relacionamento, uma tentativa de adicionar registros na tabela filha gera um erro se não houver registro pai correspondente.
**Ignore**
Permite inserir registros na tabela filha independentemente de haver um registro correspondente na tabela pai.
**Referential Integrity Grid**
Parent Table exibe o nome da tabela na relação do banco de dados que contém o índice primário ou candidato. Child Table exibe o nome da tabela filha na relação do banco de dados. Update exibe as regras de atualização de integridade referencial para a relação. Os valores possíveis são Cascade, Restrict ou Ignore. Você pode alterar as configurações selecionando o campo, o que apresentará uma lista suspensa das opções. Delete exibe as regras de exclusão de integridade referencial para a relação. Os valores possíveis são Cascade, Restrict ou Ignore. Você pode alterar as configurações selecionando o campo, o que apresentará uma lista suspensa das opções. Insert exibe as regras de inserção de integridade referencial para a relação. Os valores possíveis são Cascade, Restrict ou Ignore. Você pode alterar as configurações selecionando o campo, o que apresentará uma lista suspensa das opções. A coluna de grade Parent Tag exibe o nome da tag do índice Primary ou Candidate na tabela pai. A coluna de grade Child Tag exibe o nome da tag do índice na tabela filha.
