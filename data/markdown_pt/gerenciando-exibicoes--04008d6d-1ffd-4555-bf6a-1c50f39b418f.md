# Gerenciando exibições

Você pode executar várias tarefas para gerenciar exibições, semelhantes às usadas para gerenciar tabelas, campos e registros, por exemplo:
 - Especificar legendas para campos de exibição.
- Adicionar comentários a exibições e seus campos.
- Especificar valores padrão para campos de exibição.
- Criar regras de validação para campos e registros.
- Criar índices em campos de exibição usando o comando INDEX. Observação: diferentemente dos índices de tabela, os índices criados em exibições não são armazenados e são removidos quando a exibição é fechada. Considere o tamanho do conjunto de resultados antes de criar um índice, pois um conjunto grande pode reduzir o desempenho.
- Criar relacionamentos temporários entre exibições ou entre tabelas e exibições usando SET RELATION. Dica: para melhorar o desempenho, use a exibição como pai e a tabela como filha. Observação: isso é mais eficiente porque o índice estrutural da tabela é mantido continuamente, acessado rapidamente e pode ser usado pelo ambiente de dados para ordenar registros. Já o índice da exibição deve ser recriado a cada ativação e demora mais. Como o índice de uma exibição não faz parte de sua definição, em um ambiente de dados ela não pode ser filha, pois o índice do filho deve existir como parte da definição.

# Nesta seção
 **Abrindo exibições**
Discute como abrir exibições.
**Como: editar exibições**
Descreve como abrir exibições para edição e outras tarefas de gerenciamento.
**Como: renomear exibições (Visual FoxPro)**
Descreve como alterar os nomes das exibições.
**Como: abrir exibições em áreas de trabalho**
Descreve como abrir exibições em áreas de trabalho.
**Definindo propriedades de exibição e conexão**
Fornece uma visão geral da definição de propriedades para exibições e conexões de exibições remotas.
**Como: definir propriedades de campo para exibições**
Descreve como definir várias propriedades de campos.
**Como: adicionar comentários a exibições**
Descreve como adicionar descrições.
**Como: criar valores padrão para campos de exibição**
Descreve como especificar valores padrão.
**Como: criar regras de validação para exibições**
Descreve como criar regras de validação para campos e registros.
**Como: definir intervalos de tempo limite para conexões**
Descreve como definir valores de tempo limite da conexão com o servidor remoto.
**Como: exibir e editar instruções SQL para exibições**
Descreve como exibir e editar a instrução SQL SELECT e as propriedades geradas.
**Como: criar exibições com instruções SQL armazenadas**
Descreve como armazenar a instrução SQL SELECT criada pelo Visual FoxPro e usá-la para criar exibições programaticamente.
**Como: excluir exibições**
Descreve como excluir exibições quando o trabalho com elas terminar.

# Seções relacionadas
 **Exibindo dados em exibições**
Descreve diferentes maneiras de exibir exibições.
**Atualizando dados em exibições**
Descreve como atualizar dados nas exibições e em suas tabelas base.
**Trabalhando com exibições (Visual FoxPro)**
Explica como usar exibições para criar um conjunto de dados atualizável e personalizado para o aplicativo.
