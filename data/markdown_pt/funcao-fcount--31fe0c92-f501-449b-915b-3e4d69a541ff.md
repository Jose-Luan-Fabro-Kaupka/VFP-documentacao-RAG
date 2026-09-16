# Função FCOUNT( )

Retorna o número de campos em uma tabela.

```foxpro
FCOUNT([nWorkArea | cTableAlias])
```

#### Parâmetros
 **nWorkArea**
Especifica a área de trabalho da tabela para a qual FCOUNT( ) retorna o número de campos. FCOUNT( ) retorna 0 se uma tabela não estiver aberta na área de trabalho que você especificar.
**cTableAlias**
Especifica o alias da tabela para a qual FCOUNT( ) retorna o número de campos. O Visual FoxPro gera uma mensagem de erro se você especificar um alias de tabela que não exista.

# Valor de retorno

Numérico

# Observações

Se você omitir os argumentos opcionais, FCOUNT( ) retorna o número de campos na tabela aberta na área de trabalho atualmente selecionada.

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
SELECT 0
USE employee  && Opens employee table
CLEAR
? FCOUNT('CUSTOMER')     && Displays 13, # of fields in Customer
? FCOUNT('EMPLOYEE')  && Displays 22, # of fields in Employee
```
