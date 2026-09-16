# Criação de índice com base em expressões

Você pode aumentar o desempenho do aplicativo criando índices baseados em expressões. As expressões podem variar do simples ao complexo, dependendo das tarefas que você deseja realizar. Você pode realizar diferentes tarefas criando índices com expressões conforme descrito nas seções a seguir:
 - Índices baseados em expressões simples
- Índices baseados em expressões complexas
- Campos com valores nulos em expressões de índice

Você também pode aumentar a velocidade de consultas, relatórios ou outras operações usando expressões de índice que usam a otimização Rushmore. Para obter mais informações, consulte Otimizando aplicativos.

# Índices Baseados em Expressões Simples

Você pode criar índices usando expressões de índice simples, baseadas em um único campo ou na concatenação de dois ou mais campos de caracteres. Você também pode criar expressões de índice contendo campos de outra tabela.

> **Dica:** Se você quiser incluir campos com diferentes tipos de dados em uma expressão de índice, converta quaisquer campos que não sejam caracteres em campos de caracteres, colocando o campo entre a função STR( ).

Por exemplo, suponha que você queira organizar os registros por valor máximo do pedido e depois pelo nome da empresa. O código a seguir converte o campo MaxOrdAmt, que possui o tipo Moeda, para que possa ser concatenado com o campo Empresa, que possui o tipo Caractere:

```foxpro
STR(customer.maxordamt,20,4) + customer.company
```

Para obter mais informações, consulte STR( ) Função.

### Um ou mais campos em expressões de índice

Ao incluir um ou mais campos em uma expressão de índice, você pode executar as seguintes tarefas:
 - Classifique os dados na ordem em que os campos aparecem na expressão do índice. O Visual FoxPro avalia os campos na ordem em que aparecem na expressão. Por exemplo, suponha que você queira visualizar registros em uma tabela de clientes classificada por país, região e cliente ID. A expressão a seguir cria um índice para a tabela de clientes usando um sinal de mais (+) para incluir vários campos: customer.country + customer.region + customer.cust_id
- Evite valores duplicados em tabelas usando um índice primário ou candidato que inclua um ou mais campos. Para obter mais informações sobre como controlar valores duplicados, consulte Valores duplicados em campos.
- Otimize o desempenho e aumente a velocidade de consultas e visualizações com filtros em mais de um campo, incluindo mais de um campo na expressão do índice. Ao incluir campos que mudam menos no início da expressão, a indexação pode ser limitada aos campos cujos valores mudam com mais frequência. Por exemplo, suponha que você queira organizar registros em uma tabela de clientes por país, código postal no país e nome da empresa no código postal. No exemplo a seguir, o campo País aparece no início da lista porque é o que menos muda: cliente.país + cliente.código_postal + cliente.empresa

### Campos de outra tabela em expressões de índiceVocê pode criar uma expressão de índice que se refira a campos em outra tabela, por exemplo, uma que esteja aberta em outra área de trabalho. No entanto, é recomendável armazenar qualquer tag de índice que se refira a mais de uma tabela em um arquivo de índice independente (.idx) em vez do arquivo de índice composto estrutural (.cdx) associado. Quando uma marca de índice de uma tabela se refere a outra tabela, o Visual FoxPro não permite a abertura da tabela associada ao arquivo .cdx até que você abra a outra tabela à qual a marca de índice faz referência.

# Índices baseados em expressões complexas

Você pode criar índices usando expressões complexas, que podem conter constantes, funções do Visual FoxPro, procedimentos armazenados ou funções definidas pelo usuário. Para aproveitar as vantagens do Rushmore Query Optimization, a expressão do índice deve corresponder exatamente aos critérios.

### Funções do Visual FoxPro em expressões de índice

Você pode usar funções do Visual FoxPro em uma expressão de índice.

Por exemplo, você pode usar a função STR( ) para converter um valor numérico em uma sequência de caracteres. Suponha que você queira criar um índice para uma tabela de clientes que combine o campo cliente ID com o campo valor máximo do pedido. Você pode converter o campo MaxOrdAmt de um campo Moeda em um campo Caractere usando o seguinte código:

```foxpro
INDEX ON cust_id + STR(maxordamt, 8, 2) TAG custmaxord
```

Se quiser reduzir o tamanho dos índices para campos com valores inteiros, você pode converter os valores inteiros em uma representação de caracteres binários usando a função BINTOC( ). Você também pode converter os valores binários em valores inteiros usando a função CTOBIN( ).

Se quiser criar um índice para classificar uma tabela em ordem cronológica, você pode usar a função DTOS( ) para converter um campo de data em uma sequência de caracteres. Por exemplo, suponha que você queira acessar uma tabela de funcionários pela data de contratação e funcionário ID. O código de exemplo a seguir cria a expressão de índice que executa esta tarefa:

```foxpro
INDEX ON DTOS(hire_date) + emp_id TAG id_hired
```

Para obter mais informações, consulte Função STR( ), Função BINTOC( ), Função CTOBIN( ) e Função DTOS( ).

### Procedimentos armazenados ou funções definidas pelo usuário em expressões de índice

Você pode aumentar o poder de um índice referenciando um procedimento armazenado ou incluindo uma função defined do usuário (UDF) na expressão do índice.

> **Observação:** Existem certas considerações quando você inclui um UDF em uma expressão de índice. Fazer referência a um procedimento armazenado ou usar UDF em uma expressão de índice aumenta o tempo necessário para criar ou atualizar o índice. Para obter mais informações, consulte Considerações sobre a criação de expressões de índice.

Por exemplo, você pode usar um procedimento armazenado para extrair o nome da rua de um único campo que inclui o número e o nome da rua. Se o número da rua for sempre numérico, o procedimento armazenado poderá retornar a parte do caractere do campo e preencher o campo com espaços conforme necessário para criar uma chave de índice de comprimento constante. Você pode então usar essa chave de índice para acessar os registros na tabela na ordem dos nomes das ruas.

# Campos com valores nulos em expressões de índiceVocê pode criar índices em campos que contenham valores nulos. O Visual FoxPro insere expressões de índice que são avaliadas como nulas (.NULL.) no arquivo de índice composto (.cdx) ou de índice independente (.idx) precedendo as expressões de índice que não são avaliadas como nulas. Portanto, todos os valores nulos aparecem no início do índice.

Por exemplo, os diagramas a seguir demonstram um efeito da indexação de valores nulos. Antes de um índice ser aplicado, o primeiro diagrama mostra que o campo Seguro Social para o terceiro e quinto registros contém valores nulos (.NULL.), que indicam que os números do Seguro Social são desconhecidos ou indisponíveis.
 Valores nulos aparecem no campo SocSec para dois registros.

O código de exemplo a seguir cria um índice usando uma expressão de índice que contém o campo Segurança Social:

```foxpro
INDEX ON SocSec + LastName + FirstName TAG MyIndex
```

Quando o índice que contém o campo Previdência Social é aplicado, a tabela exibe primeiro os registros que contêm valores nulos para números de Previdência Social, classificados por sobrenome em ordem decrescente, seguidos pelos demais registros ordenados por número de Previdência Social.

> **Nota:** Existem duas entradas para Alan Carter. No entanto, como o registro número 5 contém um valor nulo, o registro número 5 é indexado antes do registro número 2.
 Os registros que contêm valores SocSec nulos aparecem primeiro.
