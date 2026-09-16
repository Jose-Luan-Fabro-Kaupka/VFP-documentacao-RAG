# Guia Regras para Atualização, Construtor de RI

Este guia do construtor de Integridade Referencial (RI) especifica as regras a aplicar quando o valor da chave da tabela pai é modificado.
 **Cascade**
Especifica que as alterações nos campos da chave Primary ou Candidate da tabela pai sejam refletidas nas tabelas filhas relacionadas. Se você selecionar esta opção, sempre que alterar qualquer um desses campos na tabela pai, o Microsoft Visual FoxPro alterará automaticamente os valores correspondentes em todos os registros relacionados das tabelas filhas.
**Restrict**
Impede a modificação dos valores dos campos da chave Primary ou Candidate da tabela pai, evitando registros órfãos na tabela filha.
**Ignore**
Permite atualizar registros na tabela pai mesmo que existam registros relacionados na tabela filha.
**Referential Integrity Grid**
Parent Table exibe o nome da tabela na relação de banco de dados que contém o índice primário ou candidato. Child Table exibe o nome da tabela filha na relação. Update exibe as regras de atualização de integridade referencial da relação. Os valores possíveis são Cascade, Restrict ou Ignore. Você pode alterar as configurações selecionando o campo, que exibirá uma lista suspensa com as opções. Delete exibe as regras de exclusão de integridade referencial da relação. Os valores possíveis são Cascade, Restrict ou Ignore. Insert exibe as regras de inserção de integridade referencial da relação, também com os valores Cascade, Restrict ou Ignore. Parent Tag exibe o nome da tag do índice Primary ou Candidate da tabela pai. Child Tag exibe o nome da tag do índice da tabela filha.
