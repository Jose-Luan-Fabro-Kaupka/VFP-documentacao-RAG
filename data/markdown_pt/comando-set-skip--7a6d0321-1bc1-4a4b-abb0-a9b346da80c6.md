# Comando SET SKIP

Cria uma relação um-para-muitos entre tabelas.

```foxpro
SET SKIP TO [TableAlias1 [, TableAlias2] ...]
```

#### Parâmetros
 **TO TableAlias1 [, TableAlias2 ] ...**
Especifica os aliases de múltiplas tabelas filhas. Eles são usados para criar uma relação um-para-muitos com uma tabela pai. Use vírgulas para separar os aliases. Em comandos que suportam um escopo (DISPLAY, LIST e assim por diante), registros na tabela pai são repetidos para cada registro correspondente na tabela filha. Use SET SKIP TO sem argumentos adicionais para remover a relação um-para-muitos da tabela pai aberta na work area selecionada atualmente. Quaisquer relações um-para-um permanecem em vigor. Relações um-para-um podem ser removidas com SET RELATION TO.

# Observações

Usando SET RELATION, você pode estabelecer relações entre tabelas abertas em work areas diferentes. Quando o ponteiro de registro é movido na tabela pai, o ponteiro de registro na tabela filha move-se para o primeiro registro correspondente. A expressão relacional em SET RELATION determina onde o ponteiro de registro se move na tabela filha. Uma relação um-para-um é criada — para cada registro na tabela pai, o ponteiro de registro move-se para o primeiro registro correspondente na tabela filha. Se um registro correspondente não puder ser encontrado na tabela filha, o ponteiro de registro na tabela filha move-se para o final da tabela.

Frequentemente, uma tabela filha contém múltiplos registros que correspondem a um registro na tabela pai. SET SKIP permite estabelecer uma relação um-para-muitos entre um registro na tabela pai e múltiplos registros na tabela filha. Quando você percorre a tabela pai, o ponteiro de registro permanece no mesmo registro pai até que o ponteiro de registro percorra todos os registros relacionados na tabela filha.

Para estabelecer uma relação um-para-muitos, primeiro crie a relação entre a tabela pai e filha com SET RELATION. Depois, emita SET SKIP para criar uma relação um-para-muitos.

# Exemplo

O exemplo abaixo encontra todas as ocorrências em três tabelas onde cada item no primeiro campo é o mesmo. Ele faz isso usando SCAN na primeira tabela, que tem uma relação para uma segunda, que tem uma relação para uma terceira. A primeira tabela então faz um SET SKIP para as outras duas tabelas. Um SET SKIP na segunda tabela não tem efeito. Afeta somente a tabela sendo escaneada (substituída, etc.). No exemplo, oito correspondências são encontradas.

```foxpro
CLOSE DATABASES
* Creates parent table with values a and b in Name field
CREATE TABLE Parent FREE (Name C(1), Val C(10))
INSERT INTO Parent VALUES ('a', 'Parent.a1')
INSERT INTO Parent VALUES ('b', 'Parent.b1')
SELECT 0     && Child1 will have two a's and two b's
CREATE TABLE Child1 FREE (Name1 C(1), Val C(10))
INSERT INTO Child1 VALUES ('a', 'Child1.a1')
INSERT INTO Child1 VALUES ('b', 'Child1.b1')
INSERT INTO Child1 VALUES ('b', 'Child1.b2')
INSERT INTO Child1 VALUES ('a', 'Child1.a2')
INDEX ON Name1 TAG tagName   && The tag name is irrelevant
SELECT 0  && Child2 will have two a's and two b's
CREATE TABLE Child2 FREE (Name2 C(1), Val C(10))
INSERT INTO Child2 VALUES ('b', 'Child1.b1')
INSERT INTO Child2 VALUES ('b', 'Child1.b2')
INSERT INTO Child2 VALUES ('a', 'Child1.a1')
INSERT INTO Child2 VALUES ('a', 'Child1.a2')
INDEX ON Name2 TAG tagName     && The tag name is irrelevant
SELECT Child1
SET RELATION TO Name1 INTO Child2
SELECT Parent
SET RELATION TO Name INTO Child1
SET SKIP TO Child1, Child2 && Parent gets both skips.
           && Otherwise, only four record triplets
           && would be listed.
SCAN ALL  && There will be eight triplets: four a's and four b's
   ? Parent.Val, Child1.Val, Child2.Val
ENDSCAN
```
