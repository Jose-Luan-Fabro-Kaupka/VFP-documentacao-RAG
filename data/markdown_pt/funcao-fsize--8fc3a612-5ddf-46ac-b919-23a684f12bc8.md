# Função FSIZE( )

Retorna o tamanho em bytes de um campo ou arquivo especificado.

```foxpro
FSIZE(cFieldName [, nWorkArea | cTableAlias] | cFileName)
```

#### Parâmetros
 **cFieldName**
Especifica o nome do campo.
**nWorkArea**
Especifica a área de trabalho da tabela para a qual FSIZE( ) retorna o tamanho do campo. FSIZE( ) retorna 0 se não houver uma tabela aberta na área de trabalho especificada.
**cTableAlias**
Especifica o alias da tabela para a qual FSIZE( ) retorna o tamanho do campo. O Visual FoxPro gera uma mensagem de erro se você especificar um alias de tabela que não existe.
**cFileName**
Especifica um arquivo para o qual FSIZE( ) retorna o tamanho em bytes.

# Valor de retorno

Numérico

# Observações

A configuração atual de SET COMPATIBLE determina se FSIZE( ) retorna o tamanho de um campo ou de um arquivo. Se SET COMPATIBLE estiver definido como OFF ou FOXPLUS (o padrão), FSIZE( ) retorna o tamanho de um campo. Se SET COMPATIBLE estiver definido como ON ou DB4, FSIZE( ) retorna o tamanho de um arquivo.

A tabela a seguir mostra o tamanho padrão (em bytes) para cada tipo de campo de comprimento fixo.

| Tipo de campo | Tamanho padrão do campo (em bytes) |
| --- | --- |
| Currency | 8 |
| Date | 8 |
| DateTime | 8 |
| Double | 8 |
| Integer | 4 |
| Logical | 1 |
| Memo | 4 |
| General | 4 |

O tamanho de um campo pode ser exibido com DISPLAY STRUCTURE e LIST STRUCTURE.

Se você omitir os argumentos opcionais nWorkArea e cTableAlias, FSIZE( ) retorna o tamanho do campo na tabela e na área de trabalho atuais.

# Exemplo

O exemplo a seguir usa FSIZE( ) para retornar o tamanho de dois campos na tabela `customer`.

```foxpro
SET COMPATIBLE OFF
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Open Customer table
CLEAR
? FSIZE('contact')  && Displays 30
? FSIZE('cust_id')  && Displays 6
```
