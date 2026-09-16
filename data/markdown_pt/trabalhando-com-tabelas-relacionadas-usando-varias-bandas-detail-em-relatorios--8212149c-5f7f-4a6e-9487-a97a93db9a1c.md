# Trabalhando com tabelas relacionadas usando várias bandas Detail em relatórios

REPORT FORM e LABEL FORM são comandos com escopo. Quando você usa qualquer comando com uma cláusula de escopo, pode especificar um intervalo de registros e/ou condições de filtro para os registros nos quais o comando deve atuar. Se você não especificar um escopo explicitamente, cada comando com escopo tem um escopo padrão. Para relatórios e etiquetas, o escopo padrão é `ALL`.

Condições e intervalos de escopo são ordinariamente avaliados em relação a, ou dirigidos por, os registros em uma única área de trabalho. Em relatórios e etiquetas, isso significa que o Report Engine processa a banda detail do layout do seu relatório ou etiqueta uma vez para cada registro no escopo do relatório. Se o seu relatório incluir expressões de grupo, o escopo da banda detail é o conjunto de registros pertencentes à quebra de grupo mais interna. Quando ocorre uma quebra de grupo, o Report Engine pausa no processamento do escopo do relatório, executa outras ações que você especifica e depois continua pelo escopo. Caso contrário, o escopo da banda detail é equivalente ao escopo do relatório.

Ao configurar dados para seu relatório ou etiqueta, você pode relacionar outras tabelas e cursors à área de trabalho selecionada, ou alias de direcionamento do relatório. Junto com o comportamento de escopo padrão do Visual FoxPro, o Report Engine também fornece a capacidade de fazer várias passagens por cada escopo de banda detail baseado nessas relações.

O Report Designer representa essas múltiplas passagens pelo escopo da banda detail mostrando várias bandas detail. Você usa bandas diferentes para exibir informações de tabelas ou cursors que são destinos de relações diferentes.

Consulte a seção sobre Working with Report Bands para informações sobre como ajustar o layout do relatório para indicar quais áreas de trabalho relacionadas são significativas para o processamento de escopo do relatório. Este tópico discute como o Report Engine trata as múltiplas tabelas quando você inclui esses recursos no layout do relatório.

# Usando Target Aliases para representar relações de dados

O alias de destino de uma banda detail refere-se a uma tabela ou view aberta na sessão de dados atual. No Report Designer, as informações de alias de destino podem parecer expressões de quebra de grupo, mas são bem diferentes. Quando um grupo quebra, o ponteiro de registro avança. Quando o Report Engine move para outra banda detail e reavalia o alias de destino, o ponteiro de registro retorna ao início do escopo da banda detail.

### Como o Report Engine valida Target Aliases em tempo de execução

O Report Engine considera o alias de direcionamento do relatório mais o atributo Target alias de cada banda detail para determinar como processar cada banda. Antes de iniciar a execução do relatório, valida quaisquer expressões de alias de destino contidas no relatório. Para ser válido, uma expressão de alias de destino deve avaliar para um dos seguintes:
 - Uma cadeia de caracteres vazia.
- O alias de uma tabela ou view em relação ao alias de direcionamento do relatório.
- O alias de direcionamento do relatório.

O Report Engine avalia quaisquer expressões usadas como aliases de destino no layout do relatório antes de começar a processar o relatório. Se essas expressões não avaliarem para aliases atualmente em uso, ocorre o erro "<alias> not found". Se um alias estiver em uso, deve ser o mesmo que o alias de direcionamento ou estar relacionado ao alias de direcionamento do relatório. Caso contrário, ocorre o erro "<alias> is not related to the current work area".

### Bandas Detail com Target Aliases

O alias de direcionamento de um relatório com tabelas relacionadas é tipicamente o pai em uma ou mais relações de dados. Por exemplo, uma tabela Customer está relacionada a uma tabela Orders e uma tabela Payments.

Um layout de relatório dirigido por esta tabela Customer indica essas relações incluindo uma banda detail com a expressão de alias de destino `"Orders"` e uma segunda banda detail com a expressão de alias de destino `"Payments"`.

> **Importante:** Inclua as aspas em cada expressão de alias de destino, a menos que Orders ou Payments seja uma variável que contenha o nome do alias real.

Para cada banda detail com um alias de destino, o Report Engine permanece no registro pai e processa todos os filhos no alias de destino apropriado relacionado ao registro pai atual. Depois move para a próxima banda e processa o conjunto de filhos na próxima tabela relacionada.

### Bandas Detail sem Target Aliases

Em relatórios com várias tabelas e aliases de destino, você pode usar um alias de destino vazio quando deseja que uma banda seja processada apenas uma vez para cada registro do alias de direcionamento. Esta técnica oferece uma maneira conveniente de fornecer algumas informações de resumo, semelhante a cabeçalhos e rodapés de grupo, mas posicionadas de forma mais flexível na saída do relatório.

Por exemplo, no seu relatório Customer, você pode fornecer um grupo de dados em Customer ID, o que permite fornecer informações sobre o Customer no cabeçalho ou rodapé do grupo. Usando uma banda detail sem alias, posicionada entre as bandas detail de Orders e Payments, você pode fornecer informações adicionais sobre o Customer, como uma cadeia de caracteres exibindo o status atual da conta. Como esta banda não tem alias de destino, seu conteúdo aparecerá apenas uma vez antes que o Report Engine continue para exibir detalhes de Payments.

### Bandas Detail com Target Aliases correspondendo ao Driving Alias

Na maioria dos casos, definir um alias de destino para uma expressão correspondente ao alias de direcionamento de um relatório resulta no mesmo comportamento que um Target alias vazio (a banda é processada uma vez para cada registro no escopo).

No entanto, o Report Engine faz uma exceção importante se você usar esta técnica na primeira banda detail do relatório: se a primeira banda tiver um alias de destino exatamente igual ao alias de direcionamento, ela processa todos os registros no escopo da detail, redefine o ponteiro de registro no alias de direcionamento e depois move para a próxima banda detail.

Usar o alias de direcionamento como alias de destino para a primeira banda fornece uma maneira de processar todos os registros em um grupo ou escopo de relatório atual várias vezes. Também fornece a capacidade de calcular alguns valores para o grupo atual antes de exibir qualquer conteúdo para os registros individuais. Esta técnica é discutida mais adiante na próxima seção, Variables and Calculated Fields for Related Tables.

### Comportamento automático um-para-muitos

Depois de validar quaisquer expressões de alias de destino usadas para suas bandas detail, o Report Engine verifica se você definiu explicitamente alguma propriedade OneToMany no seu DataEnvironment ou, se você estiver abrindo as tabelas por conta própria, se o alias de direcionamento tem relações SET SKIP definidas. Se já houver alguma definida, o Report Engine não alterará seu ambiente. No entanto, se você não definiu nenhuma relação um-para-muitos explicitamente, o Report Engine a configura para seus aliases de destino e a remove ao concluir a execução do relatório. Este comportamento automático um-para-muitos ocorre somente quando você usa pelo menos um alias de destino no relatório.

# Variáveis e campos calculados para tabelas relacionadas

Você pode definir o escopo de campos calculados e variáveis de relatório para cada uma das várias bandas detail em um layout de relatório, associando seus resultados calculados dinamicamente aos aliases de destino em cada banda.

Campos calculados em relatórios e variáveis de relatório em versões do Visual FoxPro anteriores à 9 podiam ser Reset at the end of group(s), end of page ou end of report. O valor Reset at indicava em que ponto do relatório o Report Engine definia esses itens de volta aos valores iniciais, ou em que base seus cálculos eram realizados.

Outra maneira de expressar esta ideia é dizer que campos calculados e variáveis de relatório têm escopo de dados baseado em seus valores Reset. No Visual FoxPro 9, os rótulos Reset at nas caixas de diálogo do Report Designer foram alterados para Reset based on, para esclarecer este comportamento.

Em um relatório com várias bandas detail, você pode definir o escopo de variáveis de relatório e campos calculados baseado em bandas detail e seus aliases de destino associados. Por exemplo, no seu relatório Customer, você poderia definir o escopo de uma variável definida como Count baseado na banda detail com o alias de destino Orders. Esta variável forneceria uma contagem de pedidos para cada Customer. Como está com escopo em uma banda com alias de destino correto, esta variável fornecerá uma contagem correta. Sem expressões de alias de destino, a contagem não seria correta em casos em que o Customer tivesse mais Payments do que Orders.

### Pré-processamento de cálculos de relatório

Como você pode configurar várias bandas detail com o mesmo alias de destino, pode usar uma banda para tratar cálculos de relatório antes de exibir qualquer conteúdo. No exemplo do relatório Customer, você poderia ter duas bandas com o alias de destino Orders. Você poderia redefinir duas variáveis de relatório, OrderTotal e OrderCount, baseadas na primeira banda, mas colocar todas as expressões de relatório exibindo conteúdo da tabela Order na segunda banda. Os cálculos resultantes permitiriam fornecer uma contagem e total de todos os pedidos no cabeçalho detail da segunda banda.

### Usando variáveis de relatório pré-processadas

Quando variáveis de relatório são redefinidas baseadas em uma banda detail, seus valores permanecem corretos depois que o Report Engine para de processar essa banda. Seus valores não são redefinidos até a próxima vez que o Report Engine começa a processar a mesma banda detail (ou seu cabeçalho de banda detail associado, se houver) novamente. Quaisquer resultados calculados nessas variáveis podem ser usados em cálculos adicionais ao exibir informações em bandas de relatório adicionais.

Por exemplo, você poderia usar a variável OrderTotal para exibir um cálculo de percentual do total, para cada pedido na segunda banda Orders. Depois das bandas Orders, você também poderia usar OrderTotal para calcular um saldo acumulado na banda Payments.

### Pré-processamento de variáveis de relatório baseado no alias de direcionamento

Muitas pessoas usam uma instrução SQL-SELECT para produzir um cursor de direcionamento único com campos originados de várias tabelas. Mesmo com um cursor, você ainda pode achá-lo útil configurar várias bandas detail para processar o mesmo cursor várias vezes. Usando o alias de direcionamento como alias de destino para a primeira banda detail em um relatório, você tem a oportunidade de calcular valores como se os valores no alias de direcionamento fossem repetidos em uma tabela separada.
