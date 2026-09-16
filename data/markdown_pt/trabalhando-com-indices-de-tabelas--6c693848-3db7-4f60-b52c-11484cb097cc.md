# Trabalhando com índices de tabelas

Quando você cria uma tabela, o Visual FoxPro cria um arquivo de tabela (.dbf) e, se sua tabela incluir campos memo ou general, o arquivo memo de tabela associado (.fpt). Por padrão, o Visual FoxPro armazena os registros na tabela na ordem em que você os insere. Quando sua aplicação executa operações na tabela, os registros são processados na ordem em que foram inseridos.

Você pode controlar a ordem e aumentar a velocidade do processamento dos registros da tabela criando um índice para a tabela. Um índice não altera a ordem física dos registros armazenados na tabela; em vez disso, fornece um mecanismo eficiente e versátil para acessar registros da tabela. Por exemplo, suponha que você deseje processar registros em uma tabela de clientes por nome da empresa em ordem alfabética. Você pode criar um índice de tabela baseado no campo de nome da empresa para que sua aplicação possa processar registros na ordem especificada pelo índice que você criou. Você também pode adicionar um filtro ao índice para incluir apenas os registros que atendem aos critérios do filtro.

Depois de criar o índice da tabela, você pode definir a ordem dos registros na tabela para o índice, de modo que sua aplicação processe registros na ordem especificada. Além disso, você pode criar índices diferentes para uma tabela para alterar a ordem em que sua aplicação processa registros. Por exemplo, você pode querer organizar uma tabela de clientes por nome do contato para encontrar rapidamente o nome desejado ou por código postal para gerar etiquetas de correspondência pré-ordenadas para envio eficiente. Você pode criar e armazenar diferentes cenários de ordenação para tabelas criando vários índices para a mesma tabela. Você pode usar diferentes tipos de arquivos de índice para armazenar índices, dependendo da frequência de uso.

Você também pode usar índices para criar relacionamentos persistentes entre tabelas em um banco de dados, tornando possível acessar exatamente os registros que deseja. Relacionamentos persistentes entre tabelas de banco de dados são armazenados no arquivo de banco de dados e existem como os relacionamentos padrão quando você usa as tabelas no ambiente de dados.

# Nesta seção
 **Visual FoxPro Index Files**
Descreve diferentes tipos de arquivos de índice do Visual FoxPro para armazenar índices.
**Visual FoxPro Index Types**
Descreve diferentes tipos de índice.
**How to: Create Indexes (Visual FoxPro)**
Descreve como criar índices.
**Index Creation Based on Expressions**
Descreve diferentes tipos de expressões que você pode usar para criar índices.
**Considerations for Creating Index Expressions**
Descreve considerações a lembrar ao criar expressões de índice.
**Indexes Based on Deleted Records**
Discute como índices baseados em registros excluídos melhoram o desempenho de consultas e garantem o uso da otimização de consultas Rushmore.
**How to: Filter Data**
Descreve como adicionar filtros a índices para selecionar registros contendo apenas os dados que você deseja.
**How to: Create Less Frequently Used Indexes**
Descreve como criar índices que você usa raramente ou para uma tarefa especial.
**How to: Set Controlling Indexes**
Descreve como selecionar um índice controlador, ou mestre, para uma tabela.
**How to: Select Indexes at Run Time**
Descreve como o usuário pode alterar a exibição de registros em tempo de execução.
**How to: Display Records in Descending Order**
Descreve como alterar a exibição de registros de ordem ascendente para descendente.
**How to: Enhance the Efficiency of Indexes**
Descreve como melhorar o desempenho de índices, principalmente mantendo os índices atualizados.
**How to: Delete Indexes (Visual FoxPro)**
Descreve como remover índices que você não usa mais.

# Referência
 **User Interface Reference (Visual FoxPro)**
Explica as opções que aparecem em várias caixas de diálogo, janelas e outras interfaces do usuário. Geralmente, esses tópicos aparecem quando você pressiona F1 em uma caixa de diálogo ou janela.
**Language Reference (Visual FoxPro)**
Fornece uma lista de tópicos de referência de linguagem em ordem alfabética.

# Seções relacionadas
 **Working with Data**
Descreve como projetar e construir seu banco de dados para criar aplicações eficazes com índices, tabelas e bancos de dados baseados em seus requisitos de dados.
**Working with Tables (Visual FoxPro)**
Discute como garantir que suas tabelas tenham a estrutura que sua aplicação requer.
**Working with Fields**
Apresenta registros, como visualizá-los e como usá-los para armazenar dados em tabelas.
