# Usando Rushmore Query Optimization para acelerar o acesso a dados

Para ajudá-lo a otimizar o desempenho de seus aplicativos, o Visual FoxPro inclui a tecnologia de acesso a dados Rushmore Query Optimization. Usando a tecnologia Rushmore, você pode executar certas operações complexas de tabela centenas ou até milhares de vezes mais rápido do que sem ela.

# Compreendendo a tecnologia Rushmore Query Optimization

A tecnologia Rushmore Query Optimization é uma técnica de acesso a dados que usa índices Visual FoxPro padrão para otimizar o acesso a dados. Você pode usar Rushmore com qualquer índice Visual FoxPro, incluindo índices FoxPro 1.x (.idx), índices compactos (.idx) e índices compostos (.cdx).

Tanto índices .cdx quanto .idx compactos usam uma técnica de compressão que produz índices com até um sexto do tamanho de índices no formato antigo não compactados. O Visual FoxPro pode processar um índice compactado mais rapidamente porque requer menos acesso a disco e porque mais do índice pode ser armazenado em buffer na memória. Embora a Rushmore Query Optimization, como outras técnicas de acesso a arquivos, se beneficie do tamanho menor de índices compactos, também funciona muito bem com índices em formatos mais antigos.

Quando o Visual FoxPro processa tabelas muito grandes em computadores com apenas a quantidade mínima de RAM, o Rushmore pode não encontrar memória suficiente para operar. Nesse caso, o Visual FoxPro pode exibir uma mensagem de aviso ("Not enough memory for optimization"). Embora seu programa funcione corretamente e não perca dados, a consulta não se beneficiará da otimização Rushmore.

Em sua forma mais simples, Rushmore acelera o desempenho de comandos de tabela única usando cláusulas FOR que especificam conjuntos de registros em termos de índices existentes. Além disso, Rushmore pode acelerar a operação de certos comandos como LOCATE Command e INDEX Command. Para uma lista completa de comandos otimizáveis, consulte a próxima seção, "Using Rushmore Query Optimization with Tables."

Comandos SQL do Visual FoxPro usam Rushmore como ferramenta básica na otimização de consultas multi-tabela, usando índices existentes e até criando novos índices ad hoc para acelerar consultas.

# Usando Rushmore Query Optimization com tabelas

Use Rushmore para otimizar o acesso a dados de acordo com o número de tabelas envolvidas. Quando você acessa tabelas únicas, pode aproveitar Rushmore em qualquer lugar em que uma cláusula FOR apareça. Quando você acessa várias tabelas, consultas SELECT - SQL substituem todas as otimizações Rushmore. Em um comando SQL, o Visual FoxPro decide o que é necessário para otimizar uma consulta e faz o trabalho por você. Você não precisa abrir tabelas ou índices. Se o SQL decidir que precisa de índices, cria índices temporários para seu próprio uso.

### Para usar Rushmore Query Optimization
- Para acessar dados de uma única tabela, use uma cláusula FOR em um comando como AVERAGE , BROWSE ou LOCATE , ou use comandos SQL para atualizar tabelas. Para uma lista completa de comandos que usam a cláusula FOR, consulte a tabela abaixo. -or-
- Para acessar dados de mais de uma tabela, use os comandos SELECT - SQL , DELETE - SQL e UPDATE - SQL .

A tabela a seguir lista comandos que usam cláusulas FOR. Rushmore é projetado para que sua velocidade seja proporcional ao número de registros recuperados.
 Comandos potencialmente otimizáveis com cláusulas FOR
| AVERAGE | BLANK |
| --- | --- |
| BROWSE | CALCULATE |
| CHANGE | COPY TO |
| COPY TO ARRAY | COUNT |
| DELETE | DISPLAY |
| EDIT | EXPORT TO |
| INDEX | JOIN WITH |
| LABEL | LIST |
| LOCATE | RECALL |
| REPLACE | REPLACE FROM ARRAY |
| REPORT | SCAN |
| SET DELETED | SET FILTER |
| SORT TO | SUM |
| TOTAL TO | |

Se você usar uma cláusula de escopo além de uma expressão de cláusula FOR otimizável, o escopo deve ser definido como ALL ou REST para aproveitar o Rushmore. As cláusulas de escopo NEXT ou RECORD desabilitam Rushmore. Como o escopo padrão é ALL para a maioria dos comandos, Rushmore funciona quando você omite a cláusula de escopo.

Rushmore pode usar quaisquer índices abertos, exceto índices filtrados e UNIQUE.

> **Observação:** Para desempenho ideal, não defina a ordem da tabela.

Criar índice ou tags define automaticamente a ordem. Se quiser aproveitar ao máximo Rushmore com um conjunto de dados grande que deve estar em uma ordem específica, emita SET ORDER Command para desativar o controle de índice e use o comando SORT Command .

### Indexando efetivamente para Rushmore Query Optimization

Rushmore não pode aproveitar todos os índices. Se você usar uma cláusula FOR no comando INDEX Command , Rushmore não pode usar o índice para otimização. For example, because it contains a FOR clause, this statement cannot be optimized, `INDEX ON ORDNUM FOR DISCOUNT > 10 TAG ORDDISC`.

Da mesma forma, Rushmore não pode usar um índice criado com uma condição NOT. For example, the this expression can be optimized, `INDEX ON DELETED() TAG DEL`,But this one cannot, `INDEX ON NOT DELETED() TAG NOTDEL`.

No caso especial em que você deseja excluir registros excluídos de uma consulta, usando um índice, como no primeiro exemplo anterior, acelerará operações quando você tiver definido SET DELETED como ON.

### Otimização Rushmore e páginas de código

O Visual FoxPro não usa índices de caractere existentes para tabelas criadas com uma página de código que não seja a atual. Em vez disso, o Visual FoxPro constrói índices temporários para garantir resultados corretos. Isso pode resultar em não otimização de SQL ou outros comandos. Para evitar isso, certifique-se de que a página de código Visual FoxPro atual retornada por CPCURRENT( ) Function corresponda à página de código da tabela retornada por CPDBF( ) Function. This requires either changing the current Visual FoxPro code page, or changing the table's code page. For information about specifying the current Visual FoxPro code page, see Understanding Code Pages in Visual FoxPro. For information about specifying the code page for a table, see How to: Specify the Code Page of a .dbf File. If you cannot change either the Visual FoxPro codepage or the table codepage to match, you can force optimization to work as it did in Visual FoxPro 8 and prior versions using the SET ENGINEBEHAVIOR Command with either 80 or 70 as a parameter.

### Operando sem Rushmore Query Optimization

Operações de recuperação de dados prosseguem sem otimização Rushmore nas seguintes situações:
 - Quando Rushmore não pode otimizar as expressões de cláusula FOR em um comando potencialmente otimizável.
- Quando um comando que poderia se beneficiar do Rushmore contém uma cláusula WHILE.
- Quando a memória está baixa. A recuperação de dados continua, mas não é otimizada.

# Desabilitando Rushmore Query Optimization

Embora raramente desejável, você pode desabilitar o Rushmore. Quando você emite um comando que usa Rushmore, o Visual FoxPro determina imediatamente quais registros correspondem à expressão de cláusula FOR. Esses registros são então manipulados pelo comando.

Se um comando potencialmente otimizável modificar a chave de índice na cláusula FOR, o conjunto de registros em que Rushmore está operando pode ficar desatualizado. Nesse caso, você pode desabilitar Rushmore para garantir que tenha as informações mais atuais da tabela.

### Para desabilitar Rushmore para um comando individual
- Use a cláusula NOOPTIMIZE. For example, this LOCATE command is not optimized: LOCATE FOR DueDate < {^1998-01-01} NOOPTIMIZE

Você pode desabilitar ou habilitar Rushmore globalmente para todos os comandos que se beneficiam do Rushmore, com o comando SET OPTIMIZE Command .

### Para desabilitar Rushmore globalmente
- Use o código a seguir: SET OPTIMIZE OFF

### Para habilitar Rushmore globalmente
- Use o código a seguir: SET OPTIMIZE ON

A configuração padrão da otimização Rushmore é ON.

# Otimizando expressões Rushmore

A tecnologia Rushmore depende da presença de uma expressão básica otimizável em uma cláusula FOR ou em uma cláusula SQL WHERE. Uma expressão básica otimizável pode formar uma expressão inteira ou pode aparecer como parte de uma expressão. Você também pode combinar expressões básicas para formar uma expressão complexa otimizável.

### Criando expressões básicas otimizáveis

Uma expressão básica otimizável assume uma das duas formas a seguir:

```foxpro
            eIndex relOp eExp
```

-or-

```foxpro
            eExpr relOp eIndex
```

Uma expressão básica otimizável tem as características a seguir:
 - eIndex corresponde exatamente à expressão na qual um índice é construído.
- eExpr é qualquer expressão e pode incluir variáveis e campos de outras tabelas não relacionadas.
- relOp is one of the following relational operators: <, >, =, <=, >=, <>, #, ==, or !=. You can also use the ISNULL( ) , BETWEEN( ) , or INLIST( ) functions (or their SQL equivalents such as IS NULL, and so on).

Você pode usar BETWEEN( ) ou INLIST( ) nas duas formas a seguir:

```foxpro
BETWEEN(eIndex, eExpr, eExpr)
```

-or-

```foxpro
INLIST(eIndex, eExpr [, eExpr, eExpr, ...])
```

> **Observação:** ISBLANK() e EMPTY() não são otimizáveis pelo Rushmore.

Se você criar os índices `firstname`, `custno`, `UPPER(lastname)`, and `hiredate`, cada uma das expressões a seguir é otimizável:

```foxpro
firstname = "Fred"
custno >= 1000
UPPER(lastname) = "SMITH"
hiredate < {^1997-12-30}
```

Uma expressão otimizável pode conter variáveis e funções que são avaliadas como um valor específico. For example, using the index `addr`, if you issue the command `STORE`"`WASHINGTON AVENUE`"`TO cVar`, then the following statements are also basic optimizable expressions:

```foxpro
ADDR = cVar
ADDR = SUBSTR(cVar,8,3)
```

### Compreendendo quando consultas são otimizadas

É importante compreender quando consultas serão otimizadas e quando não serão. O Visual FoxPro otimiza condições de pesquisa procurando uma correspondência exata entre o lado esquerdo de uma expressão de filtro e uma expressão de chave de índice. Portanto, Rushmore pode otimizar uma expressão somente se você pesquisar contra a expressão exata usada em um índice.

Por exemplo, imagine que você acabou de criar uma tabela e está adicionando o primeiro índice usando um comando como o seguinte:

```foxpro
USE CUSTOMERS
INDEX ON UPPER(cu_name) TAG name
```

O comando a seguir não é otimizável, porque a condição de pesquisa é baseada apenas no campo `cu_name`, não em uma expressão que está indexada:

```foxpro
SELECT * FROM customers WHERE cu_name ="ACME"
```

Em vez disso, você deve criar uma expressão otimizável usando um comando como o seguinte, em que a expressão que você está pesquisando corresponde exatamente a uma expressão indexada:

```foxpro
SELECT * FROM customers WHERE UPPER(cu_name) = "ACME"
```

> **Dica:** Para determinar o nível de otimização Rushmore sendo usado, chame SYS(3054) .

### Combinando expressões básicas otimizáveis

Você pode combinar expressões simples ou complexas com base na cláusula FOR ou WHERE para aumentar a velocidade de recuperação de dados, se as expressões FOR tiverem as características de expressões básicas otimizáveis.

Expressões básicas podem ser otimizáveis. Você pode combinar expressões básicas usando os operadores lógicos AND, OR e NOT para formar uma expressão de cláusula FOR complexa que também pode ser otimizável. An expression created with a combination of optimizable basic expressions is fully optimizable. If one or more of the basic expressions are not optimizable, the complex expression might be partially optimizable or not optimizable at all.

A set of rules determines if an expression composed of basic optimizable or non-optimizable expressions is fully optimizable, partially optimizable, or not optimizable. A tabela a seguir resume as regras de otimização de consulta Rushmore.
 Combinando expressões básicas
| Expressão básica | Operador | Expressão básica | Resultado da consulta |
| --- | --- | --- | --- |
| Otimizável | AND | Otimizável | Totalmente otimizável |
| Otimizável | OR | Otimizável | Totalmente otimizável |
| Otimizável | AND | Não otimizável | Parcialmente otimizável |
| Otimizável | OR | Não otimizável | Not Optimizable |
| Não otimizável | AND | Não otimizável | Not Optimizable |
| Não otimizável | OR | Não otimizável | Not Optimizable |
| — | NOT | Otimizável | Totalmente otimizável |
| — | NOT | Não otimizável | Not Optimizable |

Você pode usar o operador AND para combinar duas expressões otimizáveis em uma expressão totalmente otimizável:

```foxpro
FIRSTNAME = "FRED" AND HIREDATE < {^1997-12-30}      && Optimizable
```

Neste exemplo, o operador OR combina uma expressão básica otimizável com uma expressão que não é otimizável para criar uma expressão que não é otimizável:

```foxpro
FIRSTNAME = "FRED" OR "S" $ LASTNAME      && Not optimizable
```

Usar o operador NOT em uma expressão otimizável cria uma expressão totalmente otimizável:

```foxpro
NOT FIRSTNAME = "FRED"      && Fully optimizable
```

Você também pode usar parênteses para agrupar combinações de expressões básicas.

### Combinando expressões complexas

Assim como você pode combinar expressões básicas, pode combinar expressões complexas para criar uma expressão mais complexa que seja totalmente otimizável, parcialmente otimizável ou não otimizável. You can then combine these more complex expressions to create expressions that again might be fully or partially optimizable, or not optimizable at all. The following table describes the results of combining these complex expressions. These rules also apply to expressions grouped with parentheses.
 Combinando expressões complexas
| Expressão | Operador | Expressão | Resultado |
| --- | --- | --- | --- |
| Totalmente otimizável | AND | Totalmente otimizável | Fully Optimizable |
| Totalmente otimizável | OR | Totalmente otimizável | Fully Optimizable |
| Totalmente otimizável | AND | Parcialmente otimizável | Partially Optimizable |
| Totalmente otimizável | OR | Parcialmente otimizável | Partially Optimizable |
| Totalmente otimizável | AND | Não otimizável | Parcialmente otimizável |
| Totalmente otimizável | OR | Não otimizável | Not Optimizable |
| — | NOT | Totalmente otimizável | Fully Optimizable |
| Parcialmente otimizável | AND | Parcialmente otimizável | Partially Optimizable |
| Parcialmente otimizável | OR | Parcialmente otimizável | Partially Optimizable |
| Parcialmente otimizável | AND | Não otimizável | Parcialmente otimizável |
| Parcialmente otimizável | OR | Não otimizável | Not Optimizable |
| — | NOT | Parcialmente otimizável | Não otimizável |
| Não otimizável | AND | Não otimizável | Not Optimizable |
| Não otimizável | OR | Não otimizável | Not Optimizable |
| — | NOT | Não otimizável | Not Optimizable |

You can combine fully optimizable expressions with the OR operator to create one expression that is also fully optimizable:

```foxpro
* Fully-optimizable expression
(FIRSTNAME = "FRED" AND HIREDATE < {^1997-12-30}) ;
   OR (LASTNAME = "" AND HIREDATE > {^1996-12-30})
```

To create partially optimizable expressions, combine a fully optimizable expression with an expression that is not optimizable. In the following example, the AND operator is used to combine the expressions:

```foxpro
* Partially-optimizable expression
(FIRSTNAME = "FRED" AND HIREDATE < {^1997-12-30}) ;
   AND "S" $ LASTNAME
```

Partially optimizable expressions can be combined to create one expression that is also partially optimizable:

```foxpro
* Partially-optimizable expression
(FIRSTNAME = "FRED" AND "S" $ LASTNAME) ;
   OR (FIRSTNAME = "DAVE" AND "T" $ LASTNAME)
```

Combining expressions that are not optimizable creates an expression that is also not optimizable:

```foxpro
* Expression that is not optimizable
("FRED" $ FIRSTNAME OR "S" $ LASTNAME) ;
   OR ("MAIN" $ STREET OR "AVE" $ STREET)
```
