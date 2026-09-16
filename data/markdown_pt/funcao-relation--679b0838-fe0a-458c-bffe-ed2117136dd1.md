# Função RELATION( )

Retorna uma expressão relacional especificada para uma tabela aberta em uma área de trabalho específica.

```foxpro
RELATION(nRelationNumber [, nWorkArea | cTableAlias])
```

#### Parâmetros
 **nRelationNumber**
Especifica qual relação é retornada. Por exemplo, se nRelationNumber for 3, RELATION( ) retorna a expressão relacional da terceira relação criada.
**nWorkArea**
Especifica a área de trabalho de uma tabela aberta em outra área de trabalho. Se uma tabela não estiver aberta na área de trabalho especificada, RELATION( ) retorna uma cadeia de caracteres vazia.
**cTableAlias**
Especifica o alias da tabela de uma tabela aberta em outra área de trabalho.

# Valor de retorno

Character

# Observações

Por padrão, RELATION( ) retorna expressões relacionais para uma tabela especificada. Se você não especificar uma área de trabalho ou alias, RELATION( ) retorna expressões relacionais para a tabela na área de trabalho selecionada atualmente. Se não existirem relações, retorna uma cadeia de caracteres vazia. Para informações adicionais sobre a criação de relações entre tabelas, consulte Comando SET RELATION.

DISPLAY STATUS e LIST STATUS exibem expressões relacionais. Execute MODIFY DATABASE para exibir o Database Designer. Isso permite visualizar e modificar relações entre tabelas no banco de dados aberto atualmente. Execute SET para exibir a janela Data Session. Isso permite visualizar e modificar relações entre tabelas livres.

# Exemplo

No exemplo a seguir, você abre as tabelas e define as ordens. Em seguida, usa RELATION( ) para exibir as relações.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer IN 0 ORDER cust_id  && Opens Customer table
USE employee IN 0 ORDER emp_id  && Opens Customer table
USE orders IN  0 ORDER order_id  && Opens Customer table
SELECT orders
SET RELATION TO emp_id INTO employee
SET RELATION TO cust_id INTO customer ADDITIVE
? RELATION(1)  && Displays CUST_ID
? RELATION(2)  && Displays EMP_ID
? RELATION(3)  && Displays empty string
```
