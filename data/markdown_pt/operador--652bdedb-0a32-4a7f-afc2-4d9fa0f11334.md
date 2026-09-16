# Operador $

Retorna True (.T.) se uma expressão de caracteres estiver contida em outra expressão de caracteres; caso contrário, retorna False (.F.).

```foxpro
cSearchFor $ cSearchIn
```

#### Parâmetros
 **cSearchFor**
Especifica a expressão procurada dentro de cSearchIn .
**cSearchIn**
Especifica a expressão que é pesquisada para verificar se contém cSearchFor . Se cSearchFor for encontrado em cSearchIn , $ retorna True (.T.); caso contrário, retorna False (.F.). cSearchFor e cSearchIn podem ser variáveis de tipo caractere ou elementos de array, campos de tipo caractere, literais de cadeia de caracteres ou campos memo de qualquer comprimento. Campos memo podem ser manipulados como expressões de caracteres, campos em tabelas, variáveis ou elementos de array. Por exemplo, se MEMO_FLD for um campo memo, o seguinte é aceitável: LIST FOR 'FOX' $ UPPER(memo_fld)

# Valor de retorno

Logical

# Observações

Se a expressão de caracteres não for encontrada, False (.F.) é retornado. O operador $ diferencia maiúsculas de minúsculas e não é otimizável pelo Rushmore.

# Exemplo

O exemplo a seguir cria uma tabela chamada `memotest` contendo um campo memo. Três registros são adicionados à tabela. LIST é usado para exibir os três registros. O sinal de dólar ($) é usado para listar os registros que contêm a cadeia de caracteres "FOX". Os arquivos criados para o exemplo são então excluídos.

```foxpro
CLOSE DATABASES
CLEAR
CREATE TABLE memotest (Text C(3), Memo M)
INSERT INTO  memotest (Text, Memo) VALUES ('Fox', 'Fox')
INSERT INTO  memotest (Text, Memo) VALUES ('Cat', 'Cat')
INSERT INTO  memotest (Text, Memo) VALUES ('FOX', 'FOX')
LIST FIELDS  Memo, Text FOR 'FOX' $ UPPER(Memo)
USE
DELETE FILE memotest.dbf
DELETE FILE memotest.fpt
```
