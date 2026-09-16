# Melhorias na linguagem SQL

O comando SELECT - SQL e outros comandos SQL foram substancialmente aprimorados no Visual FoxPro 9.0. Este tópico descreve os aprimoramentos feitos nesses comandos e novos comandos que afetam o desempenho do SQL.

# Capacidades expandidas

Várias limitações do comando SELECT - SQL foram removidas ou aumentadas no Visual FoxPro 9.0. A tabela a seguir lista as áreas onde as limitações foram removidas ou aumentadas.

| Capacidade | Descrição |
| --- | --- |
| Número de junções e subconsultas em um comando SELECT - SQL | O Visual FoxPro 9.0 remove o limite no número total de cláusulas de junção e subconsultas em um comando SELECT - SQL. O limite anterior era nove. |
| Número de cláusulas UNION em um comando SELECT - SQL | O Visual FoxPro 9.0 remove o limite no número de cláusulas UNION em uma instrução SQL SELECT. O limite anterior era nove. |
| Número de tabelas referenciadas em um comando SELECT - SQL | O Visual FoxPro 9.0 remove o limite no número de tabelas e aliases referenciados em uma instrução SQL SELECT. O limite anterior era 30. |
| Número de argumentos em uma cláusula IN( ) | O Visual FoxPro 9.0 remove o limite de 24 valores na cláusula IN (Value_Set) para a cláusula WHERE. No entanto, o número de valores permanece sujeito à configuração de SYS(3055) - FOR and WHERE Clause Complexity . Para alterações de funcionalidade relativas à cláusula IN, consulte Changes in Functionality for the Current Release . |

# Aprimoramentos de subconsultas

O Visual FoxPro 9.0 fornece mais flexibilidade em subconsultas. Por exemplo, várias subconsultas agora são suportadas. O texto a seguir descreve os aprimoramentos de subconsultas no Visual FoxPro 9.0.

### Múltiplas subconsultas

O Visual FoxPro 9.0 suporta aninhamento de múltiplas subconsultas, com correlação permitida ao pai imediato. Não há limite para a profundidade de aninhamento. No Visual FoxPro 8.0, o erro 1842 (SQL: Subquery nesting is too deep) era gerado quando ocorria mais de um nível de aninhamento de subconsulta.

A seguir está a sintaxe geral para múltiplas subconsultas.

SELECT … WHERE … (SELECT … WHERE … (SELECT …) …) …

#### Exemplos

As consultas de exemplo a seguir, que gerariam um erro no Visual FoxPro 8.0, agora são suportadas no Visual FoxPro 9.0.

```foxpro
CREATE CURSOR MyCursor (field1 I)
INSERT INTO MyCursor VALUES (0)
CREATE CURSOR MyCursor1 (field1 I)
INSERT INTO MyCursor1 VALUES (1)
CREATE CURSOR MyCursor2 (field1 I)
INSERT INTO MyCursor2 VALUES (2)
SELECT * FROM MyCursor T1 WHERE EXISTS ;
   (SELECT * from MyCursor1 T2 WHERE NOT EXISTS ;
   (SELECT * FROM MyCursor2 T3))
*** Another multiple subquery nesting example ***
SELECT * FROM table1 WHERE table1.iid IN ;
   (SELECT table2.itable1id FROM table2 WHERE table2.iID IN ;
   (SELECT table3.itable2id FROM table3 WHERE table3.cValue = "value"))
```

### GROUP BY em uma subconsulta correlacionada

Muitas consultas podem ser avaliadas executando uma subconsulta uma vez e substituindo o valor ou valores resultantes na cláusula WHERE da consulta externa. Em consultas que incluem uma subconsulta correlacionada (também conhecida como subconsulta repetitiva), a subconsulta depende da consulta externa para seus valores. Isso significa que a subconsulta é executada repetidamente, uma vez para cada linha que pode ser selecionada pela consulta externa.

O Visual FoxPro 8.0 não permite usar GROUP BY em subconsulta correlacionada e gera o erro 1828 (SQL: Illegal GROUP BY in subquery). O Visual FoxPro 9.0 remove essa limitação e suporta GROUP BY para subconsultas correlacionadas permitidas a retornar mais de um registro.

A seguir está a sintaxe geral para a cláusula GROUP BY em uma subconsulta correlacionada.

SELECT … WHERE … (SELECT … WHERE … GROUP BY …) …

#### Exemplos

O exemplo a seguir, que geraria um erro no Visual FoxPro 8.0, agora é suportado no Visual FoxPro 9.0.

```foxpro
CLOSE DATABASES ALL
CREATE CURSOR MyCursor1 (field1 I, field2 I, field3 I)
INSERT INTO MyCursor1 VALUES(1,2,3)
CREATE CURSOR MyCursor2 (field1 I, field2 I, field3 I)
INSERT INTO MyCursor2 VALUES(1,2,3)
SELECT * from MyCursor1 T1 WHERE field1;
   IN (SELECT MAX(field1) FROM MyCursor2 T2 ;
   WHERE T2.field2=T1.FIELD2 GROUP BY field3)
```

### TOP N em uma subconsulta não correlacionada

O Visual FoxPro 9.0 suporta a cláusula TOP N em uma subconsulta não correlacionada. A cláusula ORDER BY deve estar presente se a cláusula TOP N for usada, e este é o único caso em que é permitida em subconsulta.

A seguir está a sintaxe geral para a cláusula TOP N em uma subconsulta não correlacionada.

SELECT … WHERE … (SELECT TOP nExpr [PERCENT] … FROM … ORDER BY …) …

#### Exemplos

O exemplo a seguir, que geraria um erro no Visual FoxPro 8.0, agora é suportado no Visual FoxPro 9.0.

```foxpro
CLOSE DATABASES ALL
CREATE CURSOR MyCursor1 (field1 I, field2 I, field3 I)
INSERT INTO MyCursor1 VALUES(1,2,3)
CREATE CURSOR MyCursor2 (field1 I, field2 I, field3 I)
INSERT INTO MyCursor2 VALUES(1,2,3)
SELECT * FROM MyCursor1 WHERE field1 ;
   IN (SELECT TOP 5 field2 FROM MyCursor2 order by field2)
```

### Subconsultas em uma lista SELECT

O Visual FoxPro 9.0 permite uma subconsulta como coluna ou parte de expressão em uma projeção. Uma subconsulta em uma projeção tem exatamente os mesmos requisitos que uma subconsulta usada em uma operação de comparação. Se uma subconsulta não retorna nenhum registro, o valor NULL é retornado.

No Visual FoxPro 8.0, uma tentativa de usar uma subconsulta como coluna ou parte de expressão em uma projeção geraria o erro 1810 (SQL: Invalid use of subquery).

A seguir está a sintaxe geral para uma subconsulta em uma lista SELECT.

SELECT … (SELECT …) … FROM …

#### Exemplo

O exemplo a seguir, que geraria um erro no Visual FoxPro 8.0, agora é suportado no Visual FoxPro 9.0.

```foxpro
SELECT T1.field1, (SELECT field2 FROM MyCursor2 T2;
   WHERE T2.field1=T1.field1) FROM MyCursor1 T1
```

### Funções de agregação em uma lista SELECT de uma subconsulta

No Visual FoxPro 9.0, funções de agregação agora são suportadas em uma lista SELECT de uma subconsulta comparada usando os operadores de comparação <, <=, >, >= seguidos de ALL, ANY ou SOME. Consulte Considerations for SQL SELECT Statements para obter mais informações sobre funções de agregação.

#### Exemplo

O exemplo a seguir demonstra o uso de uma função de agregação (a função COUNT( )) em uma lista SELECT de uma subconsulta.

```foxpro
CLOSE DATABASES ALL
CREATE CURSOR MyCursor (FIELD1 i)
INSERT INTO MyCursor VALUES (6)
INSERT INTO MyCursor VALUES (0)
INSERT INTO MyCursor VALUES (1)
INSERT INTO MyCursor VALUES (2)
INSERT INTO MyCursor VALUES (3)
INSERT INTO MyCursor VALUES (4)
INSERT INTO MyCursor VALUES (5)
INSERT INTO MyCursor VALUES (-1)
CREATE CURSOR MyCursor2 (FIELD2 i)
INSERT INTO MyCursor2  VALUES (1)
INSERT INTO MyCursor2  VALUES (2)
INSERT INTO MyCursor2  VALUES (2)
INSERT INTO MyCursor2  VALUES (3)
INSERT INTO MyCursor2  VALUES (3)
INSERT INTO MyCursor2  VALUES (3)
INSERT INTO MyCursor2  VALUES (4)
INSERT INTO MyCursor2  VALUES (4)
INSERT INTO MyCursor2  VALUES (4)
INSERT INTO MyCursor2  VALUES (4)
SELECT * FROM MYCURSOR WHERE field1;
   < ALL (SELECT count(*) FROM MyCursor2 GROUP BY field2) ;
   INTO CURSOR MyCursor3
BROWSE
```

### Subconsultas correlacionadas permitem que expressões complexas sejam comparadas com campo correlacionado

No Visual FoxPro 8.0, campos correlacionados só podem ser referenciados nas seguintes formas:

campo correlacionado <comparação> campo local

-ou-

campo local <comparação> campo correlacionado

No Visual FoxPro 9.0, campos correlacionados suportam comparação com expressões locais, conforme mostrado nas seguintes formas:

campo correlacionado <comparação> expressão local

-ou-

expressão local <comparação> campo correlacionado

Uma expressão local deve usar pelo menos um campo local e não pode referenciar nenhum campo externo (correlacionado).

#### Exemplo

No exemplo a seguir, uma expressão local (MyCursor2.field2 / 2) é comparada a um campo correlacionado (MyCursor.field1).

```foxpro
SELECT * FROM MyCursor ;
   WHERE EXISTS(SELECT * FROM MyCursor2  ;
   WHERE MyCursor2.field2 / 2 > MyCursor.field1)
```

### Alterações para expressões comparadas com subconsultas.

No Visual FoxPro 8.0, a parte esquerda de uma comparação usando os operadores de comparação [NOT] IN, <, <=, =, ==, <>, !=, >=, >, ALL, ANY ou SOME com uma subconsulta deve referenciar uma e somente uma tabela da cláusula FROM. No caso de uma comparação com subconsulta correlacionada, a tabela também deve ser a tabela correlacionada.

No Visual FoxPro 9.0, as comparações funcionam das seguintes formas:
 - A expressão no lado esquerdo de uma comparação IN deve referenciar pelo menos uma tabela da cláusula FROM.
- A parte esquerda para as condições =, ==, <>, != seguidas de ALL, SOME ou ANY deve referenciar pelo menos uma tabela da cláusula FROM.
- A parte esquerda para a condição >, >=, <, <= seguida de ALL, SOME ou ANY (SELECT TOP…) deve referenciar pelo menos uma tabela da cláusula FROM.
- A parte esquerda para a condição >, >=, <, <= seguida de ALL, SOME ou ANY (SELECT <aggregate function>…) deve referenciar pelo menos uma tabela da cláusula FROM.
- A parte esquerda para a condição >, >=, <, <= seguida de ALL, SOME ou ANY (subconsulta com GROUP BY e/ou HAVING) deve referenciar pelo menos uma tabela da cláusula FROM.

No Visual FoxPro 9.0, a parte esquerda de uma comparação que não vem da lista (por exemplo, ALL, SOME ou ANY não estão incluídos) não precisa referenciar nenhuma tabela da cláusula FROM.

Em todos os casos, a parte esquerda da comparação pode referenciar mais de uma tabela da cláusula FROM. Para uma subconsulta correlacionada, a parte esquerda da comparação não precisa referenciar a tabela correlacionada.

### Subconsulta em uma lista SET do comando UPDATE - SQL

No Visual FoxPro 9.0, o comando UPDATE - SQL agora suporta uma subconsulta na cláusula SET.

Uma subconsulta em uma cláusula SET tem exatamente os mesmos requisitos que uma subconsulta usada em uma operação de comparação. Se a subconsulta não retorna nenhum registro, o valor NULL é retornado.

Apenas uma subconsulta é permitida em uma cláusula SET. Se houver uma subconsulta na cláusula SET, subconsultas na cláusula WHERE não são permitidas.

A seguir está a sintaxe geral para uma subconsulta na cláusula SET.

UPDATE … SET … (SELECT …) …

#### Exemplo

O exemplo a seguir demonstra o uso de uma subconsulta na cláusula SET.

```foxpro
CLOSE DATA
CREATE CURSOR MyCursor1 (field1 I , field2 I NULL)
INSERT INTO MyCursor1 VALUES (1,1)
INSERT INTO MyCursor1 VALUES (2,2)
INSERT INTO MyCursor1 VALUES (5,5)
INSERT INTO MyCursor1 VALUES (6,6)
INSERT INTO MyCursor1 VALUES (7,7)
INSERT INTO MyCursor1 VALUES (8,8)
INSERT INTO MyCursor1 VALUES (9,9)
CREATE CURSOR MyCursor2 (field1 I , field2 I)
INSERT INTO MyCursor2 VALUES (1,10)
INSERT INTO MyCursor2 VALUES (2,20)
INSERT INTO MyCursor2 VALUES (3,30)
INSERT INTO MyCursor2 VALUES (4,40)
INSERT INTO MyCursor2 VALUES (5,50)
INSERT INTO MyCursor2 VALUES (6,60)
INSERT INTO MyCursor2 VALUES (7,70)
INSERT INTO MyCursor2 VALUES (8,80)
UPDATE MyCursor1 SET field2=100+(SELECT field2 FROM MyCursor2 ;
  WHERE MyCursor2.field1=MyCursor1.field1) WHERE field1>5
SELECT MyCursor1
LIST
```

# Sub-SELECT na cláusula FROM

Um sub-SELECT é frequentemente chamado de tabela derivada. Tabelas derivadas são instruções SELECT na cláusula FROM referenciadas por um alias ou um nome especificado pelo usuário. O conjunto de resultados do SELECT na cláusula FROM cria uma tabela usada pela instrução SELECT externa. O Visual FoxPro 9.0 permite o uso de uma subconsulta na cláusula FROM.

Um sub-SELECT deve estar entre parênteses e um alias é obrigatório. Correlação não é suportada. Um sub-SELECT tem as mesmas limitações de sintaxe do comando SELECT, mas não as limitações de sintaxe de subconsulta. Todos os sub-SELECTs são executados antes que o SELECT mais externo seja avaliado.

A seguir está a sintaxe geral para uma subconsulta na cláusula FROM.

SELECT … FROM (SELECT …) [AS] Alias…

#### Exemplo

O exemplo a seguir demonstra o uso de uma subconsulta na cláusula FROM.

```foxpro
SELECT * FROM (SELECT * FROM MyCursor T1;
   WHERE field1 = (SELECT T2.field2 FROM MyCursor1 T2;
   WHERE T2.field1=T1.field2);
   UNION SELECT * FROM MyCursor2;
   ORDER BY 2 desc) AS subquery
*** Note that the following code will generate an error ***
SELECT * FROM (SELECT TOP 5 field1 FROM MyCursor) ORDER BY field1
```

# ORDER BY com nomes de campos na cláusula UNION

Ao usar uma cláusula UNION no Visual FoxPro 8.0, você é obrigado a usar referências numéricas na cláusula ORDER BY. No Visual FoxPro 9.0, essa restrição foi removida e você pode usar nomes de campos.

Os campos referenciados devem estar presentes na lista SELECT (projeção) do último SELECT no UNION; essa projeção é usada para a operação ORDER BY.

#### Exemplo

O exemplo a seguir demonstra o uso de nomes de campos na cláusula ORDER BY.

```foxpro
CLOSE DATABASES all
CREATE CURSOR MyCursor(field1 I,field2 I)
INSERT INTO MyCursor values(1,6)
INSERT INTO MyCursor values(2,5)
INSERT INTO MyCursor values(3,4)
SELECT field1, field2, .T. AS FLAG,1 FROM MyCursor;
   WHERE field1=1;
   UNION ;
   SELECT field1, field2, .T. AS FLAG,1 FROM MyCursor;
   WHERE field1=3;
   ORDER BY field2 ;
   INTO CURSOR TEMP READWRITE
BROWSE NOWAIT
```

# Desempenho otimizado de TOP N

No Visual FoxPro 8.0 e versões anteriores, ao usar a cláusula TOP N [PERCENT] todos os registros são ordenados e depois o TOP N é extraído. No Visual FoxPro 9.0, o desempenho foi melhorado eliminando registros que não se qualificam para o TOP N do processo de ordenação o mais cedo possível.

A otimização TOP N é feita apenas se o comando SET ENGINEBEHAVIOR estiver definido como 90.

A otimização exige que TOP N retorne no máximo N registros (o que não é o caso no Visual FoxPro 8.0 e versões anteriores), o que é imposto se SET ENGINEBEHAVIOR estiver definido como 90.

TOP N PERCENT não pode ser otimizado a menos que todo o conjunto de resultados possa ser lido na memória de uma vez.

# Otimização aprimorada para condições OR em várias tabelas

O Visual FoxPro 9.0 proporciona otimização Rushmore aprimorada envolvendo condições OR em várias tabelas. O Visual FoxPro usa condições OR em várias tabelas para otimizar Rushmore condições de filtro para uma tabela, desde que ambos os lados da condição possam ser otimizados. O exemplo a seguir mostra isso:

```foxpro
CLEAR
CREATE CURSOR Test1 (f1 I)
FOR i=1 TO 20
  INSERT INTO Test1 VALUES (I)
NEXT
INDEX ON f1 TAG f1
CREATE CURSOR Test2 (f2 I)
FOR i=1 TO 20
  INSERT INTO Test2 VALUES (I)
NEXT
INDEX ON f2 TAG f2
SYS(3054,12)
SELECT * from Test1, Test2 WHERE (f1 IN (1,2,3) AND f2 IN (17,18,19)) OR ;
  (f2 IN (1,2,3) AND f1 IN (17,18,19)) INTO CURSOR Result
SYS(3054,0)
```

Neste cenário, a tabela Test1 pode ser otimizada Rushmore usando a seguinte condição:

`(f1 IN (1,2,3) OR f1 IN (17,18,19))`e a tabela Test2 com a seguinte:

`(f2 IN (17,18,19) OR f2 IN (1,2,3))`

# Suporte a dados em buffer local

Às vezes pode ser benéfico usar SELECT - SQL para selecionar registros de um cursor em buffer local em que a tabela não foi atualizada. Muitas vezes, ao criar controles como grades, caixas de listagem e caixas de combinação, é necessário considerar registros recém-adicionados que ainda não foram confirmados no disco. Atualmente, instruções SQL são baseadas em conteúdo que já foi confirmado no disco.

O Visual FoxPro 9.0 fornece aprimoramentos de linguagem que permitem especificar se os dados retornados por um comando SELECT - SQL são baseados em dados em buffer ou dados gravados diretamente no disco.

O comando SELECT - SQL agora suporta uma cláusula WITH … BUFFERING que permite especificar se os dados recuperados são baseados em dados em buffer ou dados gravados diretamente no disco. Para obter mais informações, consulte SELECT - SQL Command - WITH Clause.

Se você não incluir a cláusula BUFFERING, os dados recuperados são então determinados pela configuração do comando SET SQLBUFFERING. Para obter mais informações, consulte SET SQLBUFFERING Command.

# Aprimoramentos a outros comandos SQL

As seções a seguir descrevem aprimoramentos feitos aos comandos INSERT - SQL, UPDATE - SQL e DELETE - SQL no Visual FoxPro 9.0.

### Cláusula UNION no comando INSERT - SQL

No Visual FoxPro 9.0, uma cláusula UNION agora é suportada no comando INSERT - SQL.

A seguir está a sintaxe geral para a cláusula UNION.

INSERT INTO … SELECT … FROM … [UNION SELECT … [UNION …]]

#### Exemplo

O exemplo a seguir demonstra o uso de uma cláusula UNION em INSERT-SQL.

```foxpro
CLOSE DATABASES ALL
CREATE CURSOR MyCursor (field1 I,field2 I)
CREATE CURSOR MyCursor1 (field1 I,field2 I)
CREATE CURSOR MyCursor2 (field1 I,field2 I)
INSERT INTO MyCursor1 VALUES (1,1)
INSERT INTO MyCursor2 VALUES (2,2)
INSERT INTO MyCursor SELECT * FROM MyCursor1 UNION SELECT * FROM MyCursor2
SELECT MyCursor
LIST
```

### Comandos UPDATE - SQL correlacionados

O Visual FoxPro 9.0 agora suporta atualizações correlacionadas com o comando UPDATE - SQL.

Se uma cláusula FROM estiver incluída no comando UPDATE -SQL, então o nome após a palavra-chave UPDATE define o destino da operação de atualização. Este nome pode ser um nome de tabela, um alias ou um nome de arquivo. A seguinte lógica é usada para selecionar a tabela de destino:
 - Se o nome corresponde a um alias implícito ou explícito para uma tabela na cláusula FROM, então a tabela é usada como destino da operação de atualização.
- Se o nome corresponde ao alias do cursor na sessão de dados atual, então o cursor é usado como destino.
- Uma tabela ou arquivo com o mesmo nome é usado como destino.

A cláusula FROM do comando UPDATE -SQL tem a mesma sintaxe da cláusula FROM no comando SELECT - SQL com as seguintes limitações:
 - A tabela ou cursor de destino não pode estar envolvida em um OUTER JOIN como tabela secundária.
- O cursor de destino não pode ser um resultado de subconsulta.
- Todas as outras JOINs podem ser avaliadas antes de unir a tabela de destino.

A seguir está a sintaxe geral para um comando UPDATE correlacionado.

UPDATE … SET … FROM … WHERE …

#### Exemplo

O exemplo a seguir demonstra uma atualização correlacionada usando o comando UPDATE -SQL.

```foxpro
CLOSE DATABASES ALL
CREATE CURSOR MyCursor1 (field1 I , field2 I NULL,field3 I NULL)
INSERT INTO MyCursor1 VALUES (1,1,0)
INSERT INTO MyCursor1 VALUES (2,2,0)
INSERT INTO MyCursor1 VALUES (5,5,0)
INSERT INTO MyCursor1 VALUES (6,6,0)
INSERT INTO MyCursor1 VALUES (7,7,0)
INSERT INTO MyCursor1 VALUES (8,8,0)
INSERT INTO MyCursor1 VALUES (9,9,0)
CREATE CURSOR MyCursor2 (field1 I , field2 I)
INSERT INTO MyCursor2 VALUES (1,10)
INSERT INTO MyCursor2 VALUES (2,20)
INSERT INTO MyCursor2 VALUES (3,30)
INSERT INTO MyCursor2 VALUES (4,40)
INSERT INTO MyCursor2 VALUES (5,50)
INSERT INTO MyCursor2 VALUES (6,60)
INSERT INTO MyCursor2 VALUES (7,70)
INSERT INTO MyCursor2 VALUES (8,80)
CREATE CURSOR MyCursor3 (field1 I , field2 I)
INSERT INTO MyCursor3 VALUES (6,600)
INSERT INTO MyCursor3 VALUES (7,700)
UPDATE MyCursor1 SET MyCursor1.field2=MyCursor2.field2, field3=MyCursor2.field2*10 FROM MyCursor2 ;
  WHERE MyCursor1.field1>5 AND MyCursor2.field1=MyCursor1.field1
SELECT MyCursor1
LIST
UPDATE MyCursor1 SET MyCursor1.field2=MyCursor3.field2 FROM MyCursor2, MyCursor3  ;
  WHERE MyCursor1.field1>5 AND MyCursor2.field1=MyCursor1.field1 AND MyCursor2.field1=MyCursor3.field1
SELECT MyCursor1
LIST
```

### Comandos DELETE - SQL correlacionados

O Visual FoxPro 9.0 agora suporta exclusões correlacionadas com o comando DELETE - SQL.

Se uma cláusula FROM possui mais de uma tabela, o nome após a palavra-chave DELETE é obrigatório e define o destino da operação de exclusão. Este nome pode ser um nome de tabela, um alias ou um nome de arquivo. A seguinte lógica é usada para selecionar a tabela de destino:
 - Se o nome corresponde a um alias implícito ou explícito para uma tabela na cláusula FROM, então a tabela é usada como destino da operação de atualização.
- Se o nome corresponde ao alias do cursor na sessão de dados atual, então o cursor é usado como destino.
- Uma tabela ou arquivo com o mesmo nome é usado como destino.

The DELETE -SQL command FROM clause has the same syntax as the FROM clause in the SELECT - SQL command with the following limitations:
 - A tabela ou cursor de destino não pode estar envolvida em um OUTER JOIN como tabela secundária.
- O cursor de destino não pode ser um resultado de subconsulta.
- Deve ser possível avaliar todas as outras JOINs antes de unir a tabela de destino.

A seguir está a sintaxe geral para um comando DELETE correlacionado.

DELETE [alias] FROM alias1 [, alias2 … ] … WHERE …

#### Exemplo

O exemplo a seguir demonstra uma exclusão correlacionada usando o comando DELETE -SQL.

```foxpro
CLOSE DATABASES ALL
CREATE CURSOR MyCursor1 (field1 I , field2 I NULL,field3 I NULL)
INSERT INTO MyCursor1 VALUES (1,1,0)
INSERT INTO MyCursor1 VALUES (2,2,0)
INSERT INTO MyCursor1 VALUES (5,5,0)
INSERT INTO MyCursor1 VALUES (6,6,0)
INSERT INTO MyCursor1 VALUES (7,7,0)
INSERT INTO MyCursor1 VALUES (8,8,0)
INSERT INTO MyCursor1 VALUES (9,9,0)
CREATE CURSOR MyCursor2 (field1 I , field2 I)
INSERT INTO MyCursor2 VALUES (1,10)
INSERT INTO MyCursor2 VALUES (2,20)
INSERT INTO MyCursor2 VALUES (3,30)
INSERT INTO MyCursor2 VALUES (4,40)
INSERT INTO MyCursor2 VALUES (5,50)
INSERT INTO MyCursor2 VALUES (6,60)
INSERT INTO MyCursor2 VALUES (7,70)
INSERT INTO MyCursor2 VALUES (8,80)
CREATE CURSOR MyCursor3 (field1 I , field2 I)
INSERT INTO MyCursor3 VALUES (6,600)
INSERT INTO MyCursor3 VALUES (7,700)
DELETE MyCursor1 FROM MyCursor2  ;
  WHERE MyCursor1.field1>5 AND MyCursor2.field1=MyCursor1.field1
SELECT MyCursor1
LIST
RECALL ALL
DELETE MyCursor1 FROM MyCursor2, MyCursor3  ;
  WHERE MyCursor1.field1>5 AND MyCursor2.field1=MyCursor1.field1 AND MyCursor2.field1=MyCursor3.field1
SELECT MyCursor1
LIST
RECALL ALL
DELETE FROM MyCursor1 WHERE MyCursor1.field1>5
SELECT MyCursor1
list
RECALL ALL
DELETE MyCursor1 from MyCursor1 WHERE MyCursor1.field1>5
RECALL ALL IN MyCursor1
DELETE T1 ;
  FROM MyCursor1 T1 JOIN MyCursor2 ON T1.field1>5 AND MyCursor2.field1=T1.field1, MyCursor3  ;
  WHERE MyCursor2.field1=MyCursor3.field1
RECALL ALL IN MyCursor1
```

### Campos atualizáveis no comando UPDATE - SQL

O número de campos que podem ser atualizados com o comando UPDATE - SQL não é mais limitado a 128 como em versões anteriores do Visual FoxPro. Agora você está limitado a 255, que é o número de campos disponíveis em uma tabela.

### SET ENGINEBEHAVIOR

O comando SET ENGINEBEHAVIOR possui uma nova opção do Visual FoxPro 9.0, 90, que afeta o comportamento do comando SELECT - SQL para a cláusula TOP N e funções de agregação. Para informações adicionais, consulte SET ENGINEBEHAVIOR Command.

### Conversão de tipos de dados

A conversão entre tipos de dados (por exemplo, conversão entre campos memo e de caractere) foi aprimorada no Visual FoxPro 9.0. Essa melhoria de conversão se aplica ao comando ALTER TABLE - SQL com a opção COLUMN, bem como a alterações estruturais feitas com o Table Designer.
