# Função FIELD( )

Retorna o nome de um campo, referenciado por número, em uma tabela.

```foxpro
FIELD(nFieldNumber | cFieldName [, nWorkArea | cTableAlias [, nFlags]])
```

#### Parâmetros
 **nFieldNumber**
Especifica o número do campo. Se nFieldNumber for 1, o nome do primeiro campo na tabela é retornado; se nFieldNumber for 2, o nome do segundo campo é retornado, e assim por diante. A cadeia de caracteres vazia é retornada se nFieldNumber for maior que o número de campos. Os nomes de campo são retornados em maiúsculas.
**cFieldName**
Especifica o nome de um campo. Isso é usado principalmente para recuperar a legenda real do campo conforme armazenada em um contêiner de banco de dados (DBC) quando usado com o parâmetro nFlags. Se a legenda do campo for uma expressão (=), a expressão é avaliada. Caso contrário, a cadeia literal real é retornada. Se a expressão não puder ser avaliada em tempo de execução, um erro é gerado e o nome real do campo é retornado.
**nWorkArea**
Especifica a área de trabalho da tabela para a qual FIELD( ) retorna nomes de campo. FIELD( ) retorna a cadeia de caracteres vazia se uma tabela não estiver aberta na área de trabalho especificada.
**cTableAlias**
Especifica o alias da tabela para a qual FIELD( ) retorna nomes de campo. O Visual FoxPro gera uma mensagem de erro se você especificar um alias de tabela que não existe.
**nFlags**
Especifica se o nome real do campo ou a legenda do campo é retornado. nFlags Value description 0 Return actual field name. FIELD( ) preserves the case of the returned field name, as long as the table is stored in a DBC. 1 Return field caption. If the field caption is an expression, return its evaluated value.

# Valor de retorno

Tipo de dados Character. Se você omitir os argumentos opcionais, FIELD( ) retorna os nomes dos campos na tabela aberta na área de trabalho selecionada no momento.

# Observações

Você pode usar a função SELECT( ) para determinar a área de trabalho atual para nWorkArea. Você pode usar a função ALIAS( ) para determinar o alias da tabela na área de trabalho atual para cTableAlias. Para obter mais informações, consulte a função SELECT( ) e a função ALIAS( ).

# Exemplo

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
CLEAR
FOR gnCount = 1 TO FCOUNT()  && Loop for number of fields
   ? FIELD(gnCount)  && Display each field
NEXT
?
? 'Number of fields: ' + ALLTRIM(STR(gnCount -1))
```
