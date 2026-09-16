# Criação de tabelas

Tabelas armazenam dados em formato de linhas e colunas, semelhante a uma planilha. Cada linha representa um registro, e cada coluna representa os campos em cada registro. Tabelas no Visual FoxPro podem existir como tabela livre ou como tabela de banco de dados.

Uma tabela livre é um arquivo de tabela (.dbf) que não está associado a nenhum banco de dados. Uma tabela de banco de dados é um arquivo de tabela associado a um banco de dados. Tabelas de banco de dados podem ter propriedades que tabelas livres não possuem, como regras em nível de campo e de registro, triggers e relacionamentos persistentes. A lista a seguir inclui alguns dos benefícios que tabelas de banco de dados oferecem:
 - Nomes longos para a tabela e para cada campo na tabela.
- Captions e comentários para cada campo da tabela.
- Valores padrão, máscaras de entrada e formato para campos da tabela.
- Classe de controle padrão para campos da tabela.
- Regras em nível de campo e de registro.
- Índices de chave primária e relacionamentos de tabela para suportar regras de integridade referencial.
- Um trigger para cada evento INSERT, UPDATE ou DELETE.

No entanto, tabelas livres são úteis para armazenar informações fora de um banco de dados. Por exemplo, você pode usar tabelas livres para armazenar informações de consulta que vários bancos de dados compartilham. Para obter mais informações sobre os benefícios de associar tabelas a um banco de dados, consulte Databases in Visual FoxPro.

Para visualizar uma tabela de exemplo, abra um dos arquivos de tabela (.dbf) do banco de dados Northwind localizado no diretório Visual FoxPro ...\Samples\Northwind. Para obter mais informações, consulte How to: View Records in Tables.

# Considerações para criação de tabelas

Ao criar tabelas, lembre-se das seguintes considerações:
 - Certifique-se de que o tipo de dados do campo corresponde ao tipo de informação que deseja armazenar.
- Certifique-se de que o campo é largo o suficiente para acomodar as informações que armazena e exibe.
- Defina um número apropriado de casas decimais para campos Numeric ou Float.
- Certifique-se de que campos que podem aceitar valores nulos estão configurados para aceitá-los.
