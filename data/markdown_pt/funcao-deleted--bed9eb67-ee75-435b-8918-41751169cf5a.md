# Função DELETED( )

Retorna um valor lógico que indica se o registro atual está marcado para exclusão.

```foxpro
DELETED([cTableAlias | nWorkArea])
```

#### Parâmetros
 **cTableAlias | nWorkArea**
Você pode verificar o status do registro atual em uma tabela aberta em outra área de trabalho especificando o número da área de trabalho com nWorkArea ou o alias da tabela com cTableAlias. Se uma tabela não estiver aberta na área de trabalho que você especificar, DELETED( ) retorna false. Se você omitir cTableAlias e nWorkArea, o status de exclusão é retornado para o registro atual na área de trabalho atual.

# Valor de retorno

Lógico

# Observações

Se o registro estiver marcado para exclusão, DELETED( ) retorna true (.T.); caso contrário, DELETED( ) retorna false (.F.).

Registros podem ser marcados para exclusão com DELETE e DELETE – SQL, e podem ser desmarcados com RECALL.

A otimização de consulta Rushmore otimiza consultas que testam o status de exclusão de registros se a tabela estiver indexada em DELETED( ).

Para obter informações sobre o uso do Rushmore para otimizar consultas, consulte SET OPTIMIZE Command e Using Rushmore Query Optimization to Speed Data Access.

# Exemplo

O exemplo a seguir abre a tabela `customer` no banco de dados `testdata`. DELETE – SQL é usado para marcar todos os registros para exclusão em que o campo `country` contém USA. DELETED( ) é usado para exibir todos os registros marcados para exclusão. RECALL ALL é usado para desmarcar todos os registros marcados para exclusão.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
DELETE FROM customer WHERE country = 'USA'  && Mark for deletion
CLEAR
LIST FIELDS company, country FOR DELETED() && List marked records
RECALL ALL  && Unmark all records marked for deletion
```
