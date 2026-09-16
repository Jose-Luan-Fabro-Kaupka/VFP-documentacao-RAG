# Função DBF( )

Retorna o nome de uma tabela aberta em uma área de trabalho especificada ou um nome de tabela a partir de um alias de tabela.

```foxpro
DBF([cTableAlias | nWorkArea])
```

#### Parâmetros
 **cTableAlias**
Especifica o alias da tabela.
**nWorkArea**
Especifica o número da área de trabalho. Se você omitir cTableAlias e nWorkArea , DBF( ) retorna o nome da tabela aberta na área de trabalho atual . DBF( ) retorna uma cadeia de caracteres vazia se uma tabela não estiver aberta na área de trabalho que você especificar. Se uma tabela não tiver o alias que você especificar com cTableAlias , o Visual FoxPro gera uma mensagem de erro. Para obter informações sobre como criar um alias para uma tabela, consulte USE .

# Valor de retorno

Character

# Observações

Quando SET FULLPATH está ON, DBF( ) retorna o caminho para a tabela com o nome da tabela. Quando SET FULLPATH está OFF, DBF( ) retorna a unidade em que a tabela reside com o nome da tabela.

# Exemplo

O exemplo a seguir retorna o nome de uma tabela a partir de sua área de trabalho e de seu alias e retorna a cadeia de caracteres vazia depois que todas as tabelas foram fechadas.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer IN 2 ALIAS mycust
CLEAR
? DBF(2)  && Displays customer.dbf with its path
? DBF('mycust')  && Displays customer.dbf with its path
CLOSE DATABASES
? DBF()      && Displays the empty string
```
