# Conceitos básicos de programação

Quando você escreve um programa, pode armazenar dados e manipulá-los com uma série de instruções. Dados e contêineres de armazenamento de dados são os blocos de construção básicos em programas, e você usa comandos, funções e operadores para manipular dados e contêineres de armazenamento de dados.

# Armazenando dados

Os dados com os quais você trabalha podem incluir quantidades de tempo, dinheiro e itens contáveis, bem como datas, nomes, descrições e assim por diante. Cada pedaço de dados é de um certo tipo: pertence a uma categoria de dados que você manipula de maneiras semelhantes. Você poderia trabalhar diretamente com esses dados sem armazená-los, mas perderia a maior parte da flexibilidade e do poder do Visual FoxPro. O Visual FoxPro fornece numerosos contêineres de armazenamento para ampliar sua capacidade de manipular dados facilmente.

Os tipos de dados determinam como os dados são armazenados e como podem ser usados. Você pode multiplicar dois números, mas não pode multiplicar caracteres. Você pode imprimir caracteres em maiúsculas, mas não pode imprimir números em maiúsculas. Alguns dos principais tipos de dados no Visual FoxPro estão listados na tabela a seguir.
 Tipos de dados
| Tipo | Exemplos |
| --- | --- |
| Numeric | 123 3.1415 – 7 |
| Character | "Test String" "123" "01/01/98" |
| Logical | .T. .F. |
| Date DateTime | {^1998-01-01} {^1998-01-01 12:30:00 p} |

### Contêineres de dados

Contêineres de dados permitem executar as mesmas operações em vários pedaços de dados. Por exemplo, você soma as horas que um funcionário trabalhou, multiplica pelo salário por hora e depois deduz os impostos para determinar o valor do pagamento que o funcionário recebeu. Você terá que executar essas operações para cada funcionário e cada período de pagamento. Se armazenar essas informações em contêineres e executar as operações nos contêineres, pode simplesmente substituir os dados antigos por novos dados e executar o mesmo programa novamente. Esta tabela lista alguns dos principais contêineres de dados no Visual FoxPro.

| Tipo | Descrição |
| --- | --- |
| Variáveis | Elementos únicos de dados armazenados na RAM (Random Access Memory) do seu computador. |
| Registros de tabela | Várias linhas de campos predeterminados, cada um dos quais pode conter um pedaço de dados predefinido. As tabelas são salvas no disco. |
| Matrizes | Vários elementos de dados armazenados na RAM. |

# Manipulando dados

Contêineres e tipos de dados fornecem os blocos de construção necessários para manipular dados. As peças finais são operadores, funções e comandos.

### Usando operadores

Operadores unem dados. Aqui estão os operadores mais comuns no Visual FoxPro.

| Operador | Valid Tipos de dados | Exemplo | Resultado |
| --- | --- | --- | --- |
| = | Todos | ? n = 7 | Imprime .T. se o valor armazenado na variável n for 7, .F. caso contrário |
| + | Numeric, Character, Date, DateTime | ? "Fox" + "Pro" | Imprime "FoxPro" |
| ! or NOT | Logical | ? !.T. | Imprime .F. |
| *, / | Numeric | ? 5 * 5 ? 25 / 5 | Imprime 25 Imprime 5 |

> **Observação:** Um ponto de interrogação (?) na frente de uma expressão faz que um caractere de nova linha e os resultados da expressão sejam impressos na janela de saída ativa, que geralmente é a janela principal do Visual FoxPro.

Lembre-se de que você deve usar o mesmo tipo de dados com qualquer operador. As instruções a seguir armazenam dois pedaços de dados numéricos em duas variáveis. As variáveis receberam nomes que começam com `n` para que possamos ver de relance que contêm dados numéricos, mas você poderia nomeá-las com qualquer combinação de caracteres alfanuméricos e sublinhados.

`nFirst = 123`

`nSecond = 45`

As instruções a seguir armazenam dois pedaços de dados de caracteres em duas variáveis. As variáveis receberam nomes que começam com `c` para indicar que contêm dados de caracteres.

`cFirst = "123"`

`cSecond = "45"`

As duas operações a seguir, adição e concatenação, produzem resultados diferentes porque o tipo de dados nas variáveis é diferente.

`? nFirst + nSecond`

`? cFirst + cSecond`

#### Saída

`168`

`12345`

Como `cFirst` é dado de caracteres e `nSecond` é dado numérico, você obtém um erro de incompatibilidade de tipo de dados se tentar o comando a seguir:

`? cFirst + nSecond`

Você pode evitar esse problema usando funções de conversão. Por exemplo, STR( ) retorna o equivalente em caracteres de um valor numérico e VAL( ) retorna o equivalente numérico de uma cadeia de caracteres de números. Essas funções e LTRIM( ), que remove espaços à esquerda, permitem executar as operações a seguir:

`? cFirst + LTRIM(STR(nSecond))`

`? VAL(cFirst) + nSecond`

#### Saída

`12345`

`168`

### Usando comandos

Um comando faz que uma determinada ação seja executada. Cada comando tem uma sintaxe específica, que indica o que deve ser incluído para que o comando funcione. Há também cláusulas opcionais associadas a comandos que permitem especificar com mais detalhes o que você deseja.

Por exemplo, o comando USE permite abrir e fechar tabelas.

| Sintaxe USE | Descrição |
| --- | --- |
| USE | Fecha a tabela na área de trabalho atual. |
| USE customer | Abre a tabela CUSTOMER na área de trabalho atual, fechando qualquer tabela que já estivesse aberta na área de trabalho. |
| USE customer IN 0 | Abre a tabela CUSTOMER na próxima área de trabalho disponível. |
| USE customer IN 0 ; ALIAS mycust | Abre a tabela CUSTOMER na próxima área de trabalho disponível e atribui à área de trabalho um alias de mycust. |

A tabela a seguir mostra alguns exemplos de comandos.

| Comando | Descrição |
| --- | --- |
| DELETE | Marca registros especificados em uma tabela para exclusão. |
| REPLACE | Substitui o valor armazenado no campo do registro por um novo valor. |
| Go | Posiciona o ponteiro de registro em um local específico na tabela. |

# Controlando o fluxo do programa

O Visual FoxPro inclui uma categoria especial de comandos que "envolvem" outros comandos e funções, determinando quando e com que frequência os outros comandos e funções são executados. Esses comandos permitem ramificação condicional e loop, duas ferramentas de programação muito poderosas. O programa a seguir ilustra ramificações condicionais e loops. Esses conceitos são descritos com mais detalhes após o exemplo.

Suponha que você tenha 10.000 funcionários e deseje dar a todos que ganham US$ 30.000 ou mais um aumento de 3 por cento, e a todos que ganham menos de US$ 30.000 um aumento de 6 por cento. O programa de exemplo a seguir realiza essa tarefa.

Este programa assume que uma tabela com um campo numérico chamado `salary` está aberta na área de trabalho atual. Para informações sobre áreas de trabalho, consulte "Using Multiple Tables" em Working with Tables (Visual FoxPro).
 Programa de exemplo para aumentar salários de funcionários
| Código | Comentários |
| --- | --- |
| SCAN | O código entre SCAN e ENDSCAN é executado tantas vezes quantos registros existem na tabela. Cada vez que o código é executado, o ponteiro de registro move para o próximo registro na tabela. |
| IF salary >= 30000.00 REPLACE salary WITH ; salary * 1.03 | Para cada registro, se o salário for maior ou igual a 30.000, substitua esse valor por um novo salário 3% maior. O ponto e vírgula (;) após WITH indica que o comando continua na próxima linha. |
| ELSE REPLACE salary WITH ; salary * 1.06 | Para cada registro, se o salário não for maior ou igual a 30.000, substitua esse valor por um novo salário 6% maior. |
| ENDIF ENDSCAN | Fim da instrução condicional IF. Fim do código executado para cada registro na tabela. |

Este exemplo usa comandos de ramificação condicional e de loop para controlar o fluxo do programa.

### Ramificação condicional

A ramificação condicional permite testar condições e, dependendo dos resultados desse teste, executar operações diferentes. Há dois comandos no Visual FoxPro que permitem ramificação condicional:
 - IF ... ELSE ... ENDIF
- DO CASE ... ENDCASE

O código entre a instrução inicial e a instrução ENDIF ou ENDCASE é executado somente se uma condição lógica for avaliada como true (.T.). No programa de exemplo, o comando IF é usado para distinguir entre dois estados: o salário é US$ 30.000 ou mais, ou não é. Ações diferentes são tomadas dependendo do estado.

No exemplo a seguir, se o valor armazenado na variável `nWaterTemp` for menor que 100, nenhuma ação é tomada:

```foxpro
* set a logical variable to true if a condition is met.
IF nWaterTemp >= 100
   lBoiling = .T.
ENDIF
```

> **Note:** An asterisk at the beginning of a line in a program indicates that the line is a comment. Comentários help the programmer remember what each segment of code is designed to do, but are ignored by Visual FoxPro.

Se houver várias condições possíveis a verificar, um bloco DO CASE ... ENDCASE pode ser mais eficiente e mais fácil de acompanhar do que várias instruções IF.

### Loop

O loop permite executar uma ou mais linhas de código quantas vezes for necessário. Há três comandos no Visual FoxPro que permitem loop:
 - DO WHILE ... ENDDO
- FOR ... ENDFOR
- FOR EACH ... ENDFOR
- SCAN ... ENDSCAN

Use SCAN quando estiver executando uma série de ações para cada registro em uma tabela, como no programa de exemplo descrito. O loop SCAN permite escrever o código uma vez e ter ele executado para cada registro conforme o ponteiro de registro se move pela tabela.

Use FOR quando saber quantas vezes a seção de código precisa ser executada. Por exemplo, você sabe que há um número específico de campos em uma tabela. Como a função FCOUNT( ) do Visual FoxPro retorna esse número, você pode usar um loop FOR para imprimir os nomes de todos os campos na tabela:

```foxpro
FOR nCnt = 1 TO FCOUNT()
   ? FIELD(nCnt)
ENDFOR
```

Use DO WHILE quando desejar executar uma seção de código enquanto uma determinada condição for atendida. Você pode não saber quantas vezes o código terá que ser executado, mas sabe quando deve parar de executar. Por exemplo, suponha que você tenha uma tabela com nomes e iniciais de pessoas e deseje usar as iniciais para procurar pessoas. Você teria um problema na primeira vez que tentasse adicionar uma pessoa que tinha as mesmas iniciais de alguém já na sua tabela.

Para resolver o problema, você poderia adicionar um número às iniciais. Por exemplo, o código de identificação de Michael Suyama poderia ser MS. A próxima pessoa com as mesmas iniciais, Margaret Sun, seria MS1. Se você então adicionasse Michelle Smith à tabela, seu código de identificação seria MS2. Um loop DO WHILE permite encontrar o número correto a acrescentar às iniciais.
 Programa de exemplo com DO WHILE para gerar um ID exclusivo
| Código | Comentários |
| --- | --- |
| nHere = RECNO() | Salva o local do registro. |
| cInitials = LEFT(firstname,1) + ; LEFT(lastname,1) nSuffix = 0 | Obtém as iniciais da pessoa das primeiras letras dos campos firstname e lastname. Estabelece uma variável para manter o número a ser adicionado ao final das iniciais de uma pessoa, se necessário. |
| LOCATE FOR person_id = cInitials | Verifica se há outra pessoa na tabela com as mesmas iniciais. |
| DO WHILE FOUND( ) | Se outro registro na tabela tiver um valor person_id igual a cInitials, a função FOUND( ) retorna true (.T.) e o código no loop DO WHILE é executado. Se nenhuma correspondência for encontrada, a próxima linha de código a ser executada é a linha após ENDDO. |
| nSuffix = nSuffix + 1 cInitials = ; LEFT(cInitials,2); + ALLTRIM(STR(nSuffix)) | Prepara um sufixo novo e o acrescenta ao final das iniciais. |
| CONTINUE | CONTINUE faz que o último comando LOCATE seja avaliado novamente. O programa verifica se o novo valor em cInitials já existe no campo person_id de outro registro. Se sim, FOUND( ) ainda retornará .T. e o código no loop DO WHILE será executado novamente. Se o novo valor em cInitials for realmente exclusivo, FOUND( ) retornará .F. e a execução do programa continua com a linha de código após ENDDO. |
| ENDDO | Fim do loop DO WHILE. |
| GOTO nHere REPLACE person_id WITH cInitials | Retorna ao registro e armazena o código de identificação exclusivo no campo person_id. |

Como você não sabe de antemão quantas vezes encontrará códigos de identificação correspondentes já em uso, usa o loop DO WHILE.
