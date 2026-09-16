# Propriedade RefreshCmdDataSourceType

Especifica o tipo de fonte de dados usado para o método RecordRefresh. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.RefreshCmdDataSourceType[ = cExpression]
```

# Valor de retorno
 **cExpression**
Especifica o tipo de fonte de dados usado para o método RecordRefresh. cExpression é uma expressão de caractere que avalia para um dos seguintes: cExpression Descrição Cadeia vazia "" O Visual FoxPro ignora a propriedade RefreshCmdDataSource do CursorAdapter e usa as propriedades DataSource e DataSourceType do CursorAdapter. ODBC A fonte de dados é ODBC (Open Database Connectivity). ADO A fonte de dados é ADO (ActiveX Data Objects). Native A fonte de dados são tabelas ou cursores nativos do Visual FoxPro.

# Observações

Aplica-se a: CursorAdapter Class

Você pode definir esta propriedade no BeforeRecordRefresh Event.
