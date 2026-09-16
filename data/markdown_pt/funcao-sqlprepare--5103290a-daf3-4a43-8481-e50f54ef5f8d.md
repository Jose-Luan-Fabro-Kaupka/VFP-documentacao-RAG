# Função SQLPREPARE( )

Prepara uma instrução SQL para execução remota por SQLEXEC( ).

```foxpro
SQLPREPARE(nStatementHandle, cSQLCommand, [cCursorName])
```

#### Parâmetros
 **nStatementHandle**
Especifica o handle de instrução para a fonte de dados retornado por SQLCONNECT( ).
**cSQLCommand**
Especifica a instrução SQL passada para a fonte de dados. A instrução SQL pode conter uma cláusula WHERE parametrizada, que cria uma view parametrizada. Todos os parâmetros na cláusula WHERE devem ser definidos antes de SQLPREPARE( ) ser emitido. Por exemplo, se os parâmetros são variáveis, as variáveis devem ser criadas e inicializadas antes de SQLPREPARE( ) ser emitido. Para obter mais informações sobre views parametrizadas, consulte How to: Create Parameterized Views .
**cCursorName**
Especifica o nome do cursor Visual FoxPro para o qual o conjunto de resultados é enviado. Se você não incluir um nome de cursor, o Visual FoxPro usa o nome padrão SQLRESULT. Para múltiplos conjuntos de resultados, novos nomes de cursor são derivados anexando um número incrementado ao nome do primeiro cursor.

# Valor de retorno

Numeric

# Observações

SQLPREPARE( ) envia a instrução SQL para a fonte de dados, onde ela é compilada para execução mais rápida. Depois que a instrução SQL é compilada, ela pode ser executada com SQLEXEC( ). Se SQLEXEC( ) é usado para executar uma instrução SQL preparada com SQLPREPARE( ), somente o handle de instrução é necessário em SQLEXEC( ).

# Exemplo

```foxpro
gcAuthor = 'Smith'
= SQLPREPARE(gnHandle, 'SELECT * FROM authors;   WHERE au_lname = ?gcAuthor')
= SQLEXEC(gnHandle)
...
gcAuthor = 'Jones'
= SQLEXEC(gnHandle)
```
