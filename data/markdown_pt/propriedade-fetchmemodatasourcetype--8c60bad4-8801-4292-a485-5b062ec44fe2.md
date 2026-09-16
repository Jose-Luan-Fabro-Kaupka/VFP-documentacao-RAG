# Propriedade FetchMemoDataSourceType

Especifica o tipo de fonte de dados usado para o método DelayedMemoFetch. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.FetchMemoDataSourceType[ = cExpression]
```

# Valor de retorno
 **cExpression**
Especifica o tipo de fonte de dados usado para o método DelayedMemoFetch. cExpression é uma expressão de caractere que avalia para um dos seguintes: cExpression Descrição Cadeia de caracteres vazia "" O Visual FoxPro ignora a propriedade CursorAdapter FetchMemoDataSource e usa as propriedades CursorAdapter DataSource e DataSourceType. ODBC A fonte de dados é ODBC (Open Database Connectivity). ADO A fonte de dados é ADO (ActiveX Data Objects).

# Observações

Aplica-se a: CursorAdapter Class
