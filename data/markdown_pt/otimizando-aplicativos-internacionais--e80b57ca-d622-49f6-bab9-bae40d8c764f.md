# Otimizando aplicativos internacionais

Se você está desenvolvendo aplicativos internacionais, pode ser necessário gerenciar a sequência de colação dos seus dados para desempenho ideal. Esta seção discute:
 - Usar sequência de colação com eficiência.
- Usar SELECT - SQL com múltiplas sequências de colação.

# Usando sequência de colação com eficiência

Se seus dados não incluem marcas diacríticas, como acentos () ou trema (), você pode melhorar o desempenho usando a sequência de colação machine porque:
 - Chaves de índice não-machine são duas vezes maiores porque contêm as informações diacríticas.
- Colação não-machine usa muitas regras especiais para indexar caracteres e retornar resultados corretos.

Como a sequência de colação machine é mais rápida, geralmente é preferida para joins e pesquisas, enquanto outras sequências de colação são perfeitas para ordenar registros.

Quando você cria um índice, o Visual FoxPro usa a sequência de colação atual definida usando os comandos SET COLLATE Command, CREATE TABLE - SQL Command, ALTER TABLE - SQL Command ou INDEX Command. Por exemplo, se você quiser criar dois índices com duas sequências de colação, pode usar SET COLLATE e uma sequência de comandos como a seguir:

```foxpro
SET COLLATE TO "MACHINE"
INDEX ON lastname TAG _lastname     && Join or seek index.
SET COLLATE TO "GENERAL"
INDEX ON lastname TAG lastname  && Sort index.
```

Quando quiser fazer seek, select ou join no campo `lastname`, emita o comando `SET COLLATE TO "MACHINE"` antes de executar a operação. A Rushmore Query Optimization usa o índice criado na sequência de colação machine, e a operação de pesquisa executa muito rapidamente.

# Usando SQL SELECT com múltiplas sequências de colação

Quando você emite um comando SELECT - SQL Command, o Visual FoxPro usa a sequência de colação atual para pesquisa e para as cláusulas ORDER BY e GROUP BY. Se quiser pesquisar e ordenar usando sequências de colação diferentes, pode dividir seus comandos SQL em duas etapas da seguinte forma:

```foxpro
* Select records using one collating sequence.
SET COLLATE TO "MACHINE"
SELECT * FROM table INTO CURSOR temp1 ;
  WHERE lname = "Mller"
* Order records using a different collating sequence.
SET COLLATE TO "GENERAL"
SELECT * FROM temp1 INTO TABLE output ORDER BY lastname
```
