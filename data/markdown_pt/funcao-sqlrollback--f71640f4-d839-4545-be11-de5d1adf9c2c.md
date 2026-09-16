# Função SQLROLLBACK( )

Cancela quaisquer alterações feitas durante a transação atual.

```foxpro
SQLROLLBACK(nStatementHandle)
```

#### Parâmetros
 **nStatementHandle**
Especifica o identificador de instrução para a fonte de dados retornado por SQLCONNECT( ).

# Valor de retorno

Numérico. SQLROLLBACK( ) retorna 1 se a transação for revertida com sucesso; caso contrário, retorna -1. Se SQLROLLBACK( ) retornar -1, você pode usar AERROR( ) para determinar por que a transação não pôde ser revertida.

# Observações

Se transações manuais estiverem em vigor (a propriedade de transação SQLSETPROP( ) estiver definida como manual), você pode enviar várias atualizações para tabelas remotas. As atualizações podem ser revertidas com SQLROLLBACK( ).

As atualizações podem ser confirmadas com SQLCOMMIT( ).

# Exemplo

O exemplo a seguir pressupõe que SQLCONNECT( ) seja emitido com sucesso e seu valor de retorno seja armazenado em uma variável de memória chamada `gnHandle`. SQLSETPROP( ) é usado para definir a propriedade Transactions como 2 (manual), permitindo usar SQLCOMMIT( ) e SQLROLLBACK( ).

A tabela `authors` é modificada com SQLEXEC( ) e as alterações na tabela são canceladas com SQLROLLBACK( ).

```foxpro
= SQLSETPROP(gnHandle, 'Transactions', 2)  && manual
= SQLEXEC(gnHandle, "INSERT INTO authors (au_id, au_lname);
   VALUES ('aupoe', 'Poe')")
= SQLROLLBACK(gnHandle)
```
