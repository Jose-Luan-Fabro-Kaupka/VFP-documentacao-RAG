# Processo de Design de Banco de Dados

Se você usar um processo de design de banco de dados estabelecido, poderá criar rapidamente e de forma eficaz um banco de dados bem projetado que forneça acesso conveniente às informações que você deseja. Com um design sólido, você gastará menos tempo construindo o banco de dados e obterá resultados mais rápidos e precisos.

> **Observação:** Os termos "banco de dados" e "tabela" não são sinônimos no Visual FoxPro. O termo banco de dados (arquivo .dbc) refere-se a um banco de dados relacional que é um contêiner de informações sobre uma ou mais tabelas (arquivos .dbf) ou views.

A chave para um design de banco de dados eficaz está em entender exatamente quais informações você deseja armazenar e a forma como um sistema de gerenciamento de banco de dados relacional, como o Visual FoxPro, armazena dados. Para fornecer informações de forma eficiente e precisa, o Visual FoxPro precisa ter os fatos sobre diferentes assuntos organizados em tabelas separadas. Por exemplo, você pode ter uma tabela que armazena fatos apenas sobre funcionários e outra que armazena fatos apenas sobre vendas.

Quando você organiza seus dados de forma apropriada, projeta flexibilidade em seu banco de dados e obtém a capacidade de combinar e apresentar fatos de muitas maneiras diferentes.

Ao projetar um banco de dados, primeiro você divide as informações que deseja manter em assuntos separados e, em seguida, informa ao Visual FoxPro como os assuntos estão relacionados entre si para que o Visual FoxPro possa reunir as informações corretas quando você precisar. Ao manter informações em tabelas separadas, você facilita a organização e a manutenção de seus dados, além de construir um aplicativo de alto desempenho.

Aqui estão as etapas do processo de design de banco de dados. Cada etapa é discutida com mais detalhes em tópicos relacionados.
 - Determine a finalidade do seu banco de dados Saber a finalidade ajudará você a decidir quais fatos deseja que o Visual FoxPro armazene. Para obter mais informações, consulte Analisando Requisitos de Dados .
- Determine as tabelas que você precisa Quando você tem uma finalidade clara para seu banco de dados, pode dividir suas informações em assuntos separados, como "Funcionários" ou "Pedidos". Cada assunto será uma tabela em seu banco de dados. Para obter mais informações, consulte Organizando Requisitos em Tabelas
- Determine os campos que você precisa Decida quais informações deseja manter em cada tabela. Cada categoria de informação em uma tabela é chamada de campo e é exibida como uma coluna quando você navega na tabela. Por exemplo, um campo em uma tabela Funcionários pode ser Last_name; outro pode ser Hire_date. Para obter mais informações, consulte Determinando os Campos que Você Precisa
- Determine os relacionamentos Examine cada tabela e decida como os dados em uma tabela estão relacionados aos dados em outras tabelas. Adicione campos às tabelas ou crie novas tabelas para esclarecer os relacionamentos, conforme necessário. Para obter mais informações, consulte Identificando Relacionamentos
- Refine seu design Analise seu design em busca de erros. Crie as tabelas e adicione alguns registros de dados de exemplo. Veja se você pode obter os resultados desejados de suas tabelas. Faça ajustes no design conforme necessário. Para obter mais informações, consulte Refinando o Design

Não se preocupe se cometer erros ou deixar coisas de fora em seu design inicial. Pense nele como um rascunho que você pode refinar depois. Experimente com dados de exemplo e protótipos de seus formulários e relatórios. Com o Visual FoxPro, é fácil alterar o design do banco de dados enquanto você o está criando. No entanto, torna-se muito mais difícil fazer alterações nas tabelas depois que elas estão preenchidas com dados e depois que você construiu formulários e relatórios. Por esse motivo, certifique-se de ter um design sólido antes de avançar demais na construção do aplicativo.

Você pode usar o Database Designer para definir um conjunto de tabelas e vinculá-las com relacionamentos que persistem sempre que você usa as tabelas.

Dê uma olhada no banco de dados de exemplo. Para abrir o banco de dados no Database Designer, escolha Open no menu File e localize Testdata.dbc no diretório Visual FoxPro ...\Samples\Data.
 O Database Designer mostra os relacionamentos entre tabelas
