# Função TXNLEVEL( )

Retorna um valor numérico que indica o nível de transação atual.

```foxpro
TXNLEVEL()
```

# Valor de retorno

Numérico

# Observações

Use BEGIN TRANSACTION para criar uma transação. As transações são aninhadas emitindo BEGIN TRANSACTION quando outra transação está em andamento. As transações podem ser aninhadas dessa forma até cinco níveis. Use TXNLEVEL( ) para determinar o nível de transação atual.

TXNLEVEL( ) retorna um valor de 0 a 5. TXNLEVEL( ) retorna 0 se não houver transação em andamento.

# Exemplo

No exemplo a seguir, a tabela `customer` no banco de dados `testdata` é aberta. BEGIN TRANSACTION é emitido para iniciar uma transação, e TXNLEVEL( ) é usado para exibir o nível de transação (1). BEGIN TRANSACTION é emitido novamente para iniciar uma transação aninhada, e TXNLEVEL( ) exibe 2 para o nível de transação atual.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE Customer     && Open customer table
CLEAR
BEGIN TRANSACTION
   tLevel = ALLTRIM(STR(TXNLEVEL()))
   =MESSAGEBOX("Current Transaction: " + tLevel, 0, "Transaction Level")
   BEGIN TRANSACTION
      tLevel = ALLTRIM(STR(TXNLEVEL()))
      =MESSAGEBOX("Current Transaction: " + tLevel, 0, ;
         "Transaction Level")
   END TRANSACTION
END TRANSACTION
```
