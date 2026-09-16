# Grupos de dados em relatórios

Frequentemente, você deseja examinar dados agrupados com base em um ou mais critérios. Esses critérios são geralmente expressões baseadas em um ou mais campos de tabela, mas podem ser muito mais complexos. Você designa um grupo de dados em um relatório associando uma expressão Group on, seu critério para agrupar os registros, ao relatório.

Para cada conjunto de registros em que a expressão avalia para um valor, você pode designar certas ações que deseja que o Report Engine execute. Essas ações incluem fornecer conteúdo de resumo na saída do relatório e acionar código de programa.

# Usando vários grupos de dados

Grupos de dados são aninhados, o que pode ser útil para organizar dados e totalizar expressões em diferentes níveis. Por exemplo, você pode agrupar registros em um relatório por país criando grupos de dados baseados no campo de nome do país. Você pode então agrupar registros por região dentro de cada país como um grupo aninhado.

Para determinar o nível de aninhamento para um grupo de dados, considere com que frequência o valor da expressão para o grupo de dados pode mudar, depois defina o grupo que muda com mais frequência primeiro. No relatório de exemplo descrito nesta seção, o valor de um campo de país muda com mais frequência do que o valor de um campo de região. Portanto, o país deve ser o grupo externo e a região deve ser o grupo interno.

# Colocando dados em ordem para grupos

Para agrupar registros efetivamente, você deve classificar os registros apropriadamente antes de executar o relatório. Se os registros com o mesmo valor de grupo não aparecem consecutivamente na saída, o Report Engine não pode exibir as informações de resumo ou calcular seus valores relacionados ao grupo.

O layout do relatório não classifica e ordena seus dados de fato. Ele processa registros na mesma ordem em que existem na fonte de dados. Classificação e ordenação devem ser realizadas com uma view, índice ou outra forma de manipulação de dados fora do layout. Por exemplo, se a fonte de dados é uma tabela, seus registros provavelmente não estão na ordem apropriada para agrupamento. Você pode classificar e ordenar os dados definindo um índice apropriado na tabela, usando uma view ordenada no ambiente de dados ou usando uma consulta como fonte de dados para exibir os registros em grupos.

No relatório de exemplo descrito acima, que contém dois níveis de grupo, os registros na fonte de dados devem ser classificados por nome do país e também por estado ou região dentro do país, para aparecer adequadamente na saída. Se a fonte de dados do relatório é uma tabela, você indexa a tabela em uma expressão de chave como `Country + Region`.

> **Observação:** Seu índice pode conter elementos adicionais não necessários pelos grupos de dados em seu relatório. Neste exemplo, sua expressão de índice poderia ser Country + Region +City. Esta ordem forneceria uma lista classificada de cidades nos detalhes que você exibe para cada região.

# Opções de exibição de relatório relevantes para grupos de dados

Ao adicionar grupos de dados, você pode preceder e seguir cada grupo com um cabeçalho e rodapé de grupo, que aparecem no layout do relatório como uma banda Group Header e uma banda Group Footer. Tipicamente, a banda Group Header contém um controle Field para o campo usado pelo grupo. Você também pode adicionar outros controles, como formas ou labels que exibem antes do primeiro registro em um grupo. A banda Group Footer frequentemente contém totais de grupo e outras informações de resumo para o grupo.

Você também pode especificar outras opções para grupos de dados:
 - Imprimindo texto em cabeçalhos e rodapés para identificar grupos específicos.
- Imprimindo cada grupo em uma nova página.
- Reiniciando números de página quando grupos são impressos em uma nova página.

# Acionando código para um grupo de dados

Você pode executar ações programaticamente para cada grupo de dados. Por exemplo, cada vez que uma nova região começa, você poderia inserir um registro em um cursor, com campos para o nome da região e a variável de sistema _PAGENO. Após executar o relatório, você poderia usar este cursor para fornecer um segundo relatório com um índice ou sumário.

Para executar esta tarefa durante a execução do relatório, escreva uma função definida pelo usuário e especifique seu nome como o código a executar durante o evento On entry ou On exit para a banda Group Header.

Para obter mais informações, consulte Como: especificar expressões a avaliar ao processar bandas.
