# Função FILTER( )

Retorna a expressão de filtro de tabela especificada em SET FILTER.

```foxpro
FILTER([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica a área de trabalho da tabela. FILTER( ) retorna a cadeia vazia se não houver tabela aberta nessa área.
**cTableAlias**
Especifica o alias da tabela. O Visual FoxPro gera um erro se o alias não existir.

# Valor de retorno

Character

# Observações

Se os argumentos opcionais forem omitidos, FILTER( ) retornará a expressão da tabela aberta na área atualmente selecionada. Para criar um filtro, consulte Comando SET FILTER.

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
SET TALK ON
SET FILTER TO SUBSTR(cust_id,1) = 'B'
CLEAR
? FILTER()  && Display filter expression
STORE FILTER('customer') TO gcOldFilter    && Save filter expression
SET FILTER TO country = 'USA'
? FILTER()  && Display filter expression
SET FILTER TO &gcOldFilter    && Restore filter expression
? FILTER()  && Display filter expression
LIST FIELDS cust_id, contact  && Demonstrate filter condition
```
