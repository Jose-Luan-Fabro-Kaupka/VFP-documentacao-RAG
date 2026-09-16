# Como: criar uma consulta parametrizada

Assim como você pode criar exibições parametrizadas usando os Designers de Consulta e Exibição ou a linguagem, você pode criar uma consulta SQL pass-through parametrizada.

### Para criar uma consulta parametrizada com SQL pass-through
- Preceda um parâmetro do Visual FoxPro com um ponto de interrogação (?), e então inclua o parâmetro em uma cadeia SQL que você envia com a função SQLEXEC( ) .

O parâmetro que você fornece é avaliado como uma expressão do Visual FoxPro, e o valor é enviado como parte da instrução SQL da exibição. Se a avaliação falhar, o Visual FoxPro solicita o valor do parâmetro.

Por exemplo, se você tem a tabela `customer` do banco de dados `Testdata` em um servidor remoto, o código a seguir cria uma consulta parametrizada que limita a exibição aos clientes cujo país corresponde ao valor fornecido para o parâmetro `cCountry`:

```foxpro
? SQLEXEC(1,'SELECT * FROM customer WHERE customer.country = cCountry')
```

Se você deseja solicitar ao usuário um valor de parâmetro, preceda a expressão do parâmetro com um ponto de interrogação (?). Para obter mais informações, consulte Como: criar exibições parametrizadas.

Sua fonte de dados ODBC não aceita parâmetros nos seguintes locais:
 - Em uma lista de campos ou tabelas SELECT.
- Como ambas as expressões em um predicado de comparação.
- Como ambos os operandos de um operador binário.

Uma fonte de dados ODBC não aceitará parâmetros nos seguintes locais na cláusula WHERE ou HAVING de uma instrução SELECT:
 - Como o primeiro e o segundo operandos de um predicado BETWEEN.
- Como o primeiro e o terceiro operandos de um predicado BETWEEN.
- Como a expressão e o primeiro valor de um predicado IN.
- Como o operando de um operador unário + ou -.
- Como o argumento de uma função SET.

Para obter mais informações, consulte Usando parâmetros de entrada/saída do SQL Server.
