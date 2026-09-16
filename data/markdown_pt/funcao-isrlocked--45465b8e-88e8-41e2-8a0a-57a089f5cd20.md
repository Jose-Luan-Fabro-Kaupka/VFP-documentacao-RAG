# Função ISRLOCKED( )

Retorna o status de bloqueio do registro.

```foxpro
ISRLOCKED([nRecordNumber, [nWorkArea | cTableAlias]])
```

#### Parâmetros
 **nRecordNumber**
Especifica o número do registro para o qual o status de bloqueio é retornado. Se nRecordNumber for omitido, o status de bloqueio do registro é retornado para o registro atual.
**nWorkArea**
Especifica o número da área de trabalho da tabela para a qual o status de bloqueio do registro é retornado. Se você omitir cTableAlias e nWorkArea , o status de bloqueio do registro é retornado para a tabela aberta na área de trabalho atual.
**cTableAlias**
Especifica o alias da tabela para a qual o status de bloqueio do registro é retornado.

# Valor de retorno

Lógico

# Observações

ISRLOCKED( ) retorna um valor lógico true (.T.) se o registro estiver bloqueado pela aplicação atual; caso contrário, retorna um valor lógico false (.F.).

> **Observação:** ISRLOCKED( ) retorna .T. somente na sessão de dados que aplicou o bloqueio do registro.
