# Função SQLCOMMIT( )

Confirma uma transação.

```foxpro
SQLCOMMIT(nStatementHandle)
```

#### Parâmetros
 **nStatementHandle**
Especifica o identificador de instrução da fonte de dados retornado por SQLCONNECT( ) .

# Valor de retorno

Numérico. SQLCOMMIT( ) retorna 1 se a transação for confirmada com sucesso; caso contrário, retorna -1. Se SQLCOMMIT( ) retornar -1, você pode usar AERROR( ) para determinar por que a transação não pôde ser confirmada.

# Observações

Se transações manuais estiverem em vigor (a propriedade Transactions de SQLSETPROP( ) estiver definida como Manual), você pode enviar várias atualizações para tabelas remotas e confirmar todas as atualizações com SQLCOMMIT( ).

As atualizações podem ser revertidas com SQLROLLBACK( ).

# Exemplo

O exemplo a seguir supõe que SQLCONNECT( ) seja emitido com sucesso e que seu valor de retorno seja armazenado em uma variável de memória chamada `gnHandle`. SQLSETPROP( ) é usado para definir a propriedade Transactions como 2 (Manual), permitindo que você use SQLCOMMIT( ) e SQLROLLBACK( ).

A tabela `authors` é modificada com SQLEXEC( ), e as alterações na tabela são confirmadas com SQLCOMMIT( ).

```foxpro
= SQLSETPROP(gnHandle, 'Transactions', 2)  && Manual transactions
= SQLEXEC(gnHandle, "INSERT INTO authors (au_id, au_lname);
   VALUES ('aupoe', 'Poe')")  && Modify the authors table
= SQLCOMMIT(gnHandle)  && Commit the changes
```
