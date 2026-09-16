# Função CURVAL( )

Retorna valores de campo diretamente do disco para uma tabela ou uma fonte de dados remota.

```foxpro
CURVAL(cExpression [, cTableAlias | nWorkArea])
```

#### Parâmetros
 **cExpression**
Especifica uma expressão cujo valor CURVAL( ) retorna de uma tabela ou fonte de dados remota. cExpression é tipicamente um campo ou uma expressão consistindo em um conjunto de campos da tabela ou fonte de dados remota.
**cTableAlias**
Especifica o alias da tabela da qual os valores de campo são retornados do disco para uma tabela ou fonte de dados remota.
**nWorkArea**
Especifica a área de trabalho da tabela da qual os valores de campo são retornados do disco para uma tabela ou fonte de dados remota.

# Valor de retorno

Character, Currency, Date, DateTime, Double, Float, Logical, Numeric ou Memo

# Observações

Os valores de campo retornados por CURVAL( ) e OLDVAL( ) podem ser comparados para determinar se outro usuário em uma rede alterou os valores de campo enquanto os campos estavam sendo editados. CURVAL( ) e OLDVAL( ) só podem retornar valores diferentes quando o buffer de linha ou tabela otimista está habilitado. O buffer de linha ou tabela otimista é habilitado com CURSORSETPROP( ).

> **Observação:** Se você estiver trabalhando com uma view em um ambiente multiusuário, os valores retornados por CURVAL() podem não estar atualizados, a menos que você chame a função REFRESH() primeiro. Os dados retornados por uma view são armazenados em buffer, e a função CURVAL() lê valores do buffer. No entanto, se outros usuários alteraram dados nas tabelas subjacentes da view, os dados em buffer não são atualizados até que a função REFRESH() seja chamada.

CURVAL( ) retorna valores de campo para o registro atual, e o tipo de dados do valor de retorno é determinado pela expressão que você especifica com cExpression.

O valor é retornado para a tabela ou cursor aberto na área de trabalho selecionada atualmente se CURVAL( ) for emitido sem os argumentos opcionais cTableAlias ou nWorkArea.

# Exemplo

Este exemplo cria uma tabela livre chamada `mytable`, e um valor de "One" é inserido no campo `cDigit`. O buffer de tabela otimista é habilitado com SET MULTILOCKS ON e CURSORSETPROP( ).

Um valor de "Two" é então inserido no campo `cDigit`, e CURVAL( ) e OLDVAL( ) são usados para exibir os valores originais de `cDigit`. TABLEUPDATE( ) é usado para confirmar as alterações na tabela, e CURVAL( ) e OLDVAL( ) são usados para exibir os novos valores de `cDigit`. Observe que, como este é um exemplo de usuário único, CURVAL( ) e OLDVAL( ) retornam valores idênticos.

```foxpro
CLOSE DATABASES
CLEAR
CREATE TABLE mytable FREE (cDigit C(10))
* Store original value
INSERT INTO mytable (cDigit) VALUES ("One")
SET MULTILOCKS ON        && Allow optimistic table buffering
= CURSORSETPROP("Buffering",5)   && Optimistic table buffering on
REPLACE cDigit WITH "Two"    && New value
? "Current value: " + CURVAL("cDigit", "mytable")
? "Old value: " + OLDVAL("cDigit", "mytable")
= TABLEUPDATE(.T.)       && Commit changes made to table
? "Table changes committed"
? "New current value: " + CURVAL("cDigit", "mytable")
? "New old value: " + OLDVAL("cDigit", "mytable")
```
