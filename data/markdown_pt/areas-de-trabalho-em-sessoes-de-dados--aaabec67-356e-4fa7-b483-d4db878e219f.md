# Áreas de trabalho em sessões de dados

Uma área de trabalho é uma região numerada que identifica uma tabela aberta, seu índice e seus relacionamentos com outras tabelas em uma sessão de dados. Uma sessão de dados é uma representação do ambiente de trabalho dinâmico atual usado por um formulário, form set ou relatório. Quando você usa sessões de dados, o Visual FoxPro fornece automaticamente um ambiente separado para cada instância de um formulário ou form set. Cada sessão de dados contém um conjunto de áreas de trabalho. Para obter mais informações sobre sessões de dados, consulte How to: Use Data Sessions e How to: View Open Tables in Data Sessions.

No Visual FoxPro, você pode abrir e manipular tabelas em 32.767 áreas de trabalho. As áreas de trabalho são tipicamente identificadas em sua aplicação usando um número ou o alias de tabela da tabela aberta na área de trabalho. Para obter mais informações, consulte How to: Open Tables in Work Areas e How to: Close Tables in Work Areas.

Um alias de tabela é um nome que se refere a uma tabela aberta em uma área de trabalho. Usar um alias de tabela ou nome sozinho identifica especificamente a tabela desejada independentemente da área de trabalho em que a tabela está aberta. Você pode usar aliases de tabela na linguagem de programação do Visual FoxPro.

Quando você abre uma tabela, o Visual FoxPro usa automaticamente o nome do arquivo da tabela como alias padrão. O Visual FoxPro também atribui seu próprio alias padrão a uma tabela automaticamente nas seguintes circunstâncias:
 - Quando você abre uma tabela simultaneamente em várias áreas de trabalho chamando o comando USE com a cláusula AGAIN sem especificar um alias ao abrir a tabela em cada área de trabalho.
- Quando existe um conflito entre aliases.

Os aliases padrão que o Visual FoxPro atribui nas primeiras 10 áreas de trabalho são as letras de área de trabalho "A" a "J". Os aliases atribuídos nas áreas de trabalho 11 a 32.767 são W11 a W32767. Você pode usar esses aliases padrão para se referir a uma tabela aberta em uma área de trabalho da mesma forma que qualquer outro alias padrão ou definido pelo usuário. Para obter mais informações, consulte How to: Create and Use Table Aliases.
