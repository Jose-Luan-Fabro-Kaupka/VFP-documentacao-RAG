# Como o Assistente de Migração para SQL Server funciona

O Assistente de Migração para SQL Server torna a migração de um banco de dados do Visual FoxPro para o SQL Server fácil e quase transparente.

O Assistente de Migração para SQL Server exporta dados usando um de dois métodos:
 - Criar um procedimento armazenado que executa inserções de várias linhas.
- Criar uma instrução SQL INSERT para cada linha na tabela e depois executar a instrução.

Criar um procedimento armazenado pode ser muito rápido porque os procedimentos armazenados são pré-compilados e executam rapidamente. No entanto, os procedimentos armazenados não podem aceitar variáveis binárias de comprimento variável como parâmetros.

Se você está exportando dados que deseja armazenar em tabelas do SQL Server e usa tipos de dados text ou image ou tabelas com mais de 250 campos, o Assistente de Migração para SQL Server cria uma instrução SQL INSERT para cada linha na tabela e depois executa a instrução. Se o Assistente de Migração para SQL Server encontrar erros e o número de erros exceder 10 por cento do número de registros na tabela ou 100 registros, o que for maior, o assistente cancela a exportação dessa tabela e salva o número de erros de exportação para o relatório de erros. No entanto, a tabela do servidor exportada não é removida e quaisquer registros exportados com sucesso permanecem na tabela do servidor.

# Arquivos criados pelo Assistente de Migração para SQL Server

O Assistente de Migração para SQL Server cria tabelas para seu próprio uso durante o processo de migração. Esses arquivos são removidos do disco rígido, a menos que ocorra o seguinte:
 - Você escolha produzir um relatório de migração.
- Você deseje salvar o SQL gerado.
- Ocorram erros durante a migração e você escolha salvar as informações de erro.

Se qualquer uma das condições acima for verdadeira, o Assistente de Migração para SQL Server cria um projeto, chamado Report, Report1, Report2 e assim por diante, e um banco de dados, chamado Upsize, Upsize1 e assim por diante, em um subdiretório chamado UPSIZE no diretório definido pelo comando SET DEFAULT para sua sessão do Visual FoxPro. O assistente adiciona as tabelas do banco de dados usadas para produzir o Relatório de Migração, uma tabela para armazenar o SQL gerado e quaisquer tabelas de erro.

A tabela a seguir lista os arquivos de tabela potencialmente criados pelo processo de migração.

| Nome da tabela | Conteúdo | Finalidade |
| --- | --- | --- |
| Errors_uw | Informações sobre qualquer erro que ocorreu durante a migração. | Tabela de relatório |
| Fields_uw | Informações sobre todas as tabelas migradas. | Tabela de relatório |
| Indexes_uw | Informações sobre todos os índices migrados. | Tabela de relatório |
| Misc_uw | Informações diversas de migração. | Tabela de relatório |
| Relations_uw | Informações sobre todas as restrições de integridade referencial armazenadas no banco de dados do Visual FoxPro. | Tabela de relatório |
| Tables_uw | Informações sobre todas as tabelas no banco de dados que você escolheu migrar. | Tabela de relatório |
| Views_uw | Informações sobre as exibições locais redirecionadas para acessar dados remotos. | Tabela de relatório |
| SQL_uw | Um campo memo contendo todo o código SQL gerado pelo Assistente de Migração para SQL Server. | Tabela de script |
| ExportErrors_ table _ name | O Assistente de Migração para SQL Server gera uma tabela contendo os registros que não foram exportados com sucesso para cada tabela que experimenta um erro de exportação de dados durante a migração. | Tabelas de erro de exportação de dados |

> **Observação:** Se o assistente for cancelado durante o processamento ou se o assistente parar por causa de um erro, nenhuma tabela permanece no disco rígido.

> **Dica:** A tabela de script armazenada no disco rígido contém todo o código SQL gerado pelo Assistente de Migração para SQL Server, independentemente de ser executado sem erro no servidor ou não. Se você deseja usar esse código, a melhor abordagem é examinar o SQL gerado, copiar as partes que deseja usar, executar os trechos extraídos de código e repetir o processo para obter os resultados desejados. Você não pode executar o script SQL inteiro como substituto da execução do Assistente de Migração para SQL Server porque o assistente executa etapas adicionais que não são refletidas no código SQL gerado.
