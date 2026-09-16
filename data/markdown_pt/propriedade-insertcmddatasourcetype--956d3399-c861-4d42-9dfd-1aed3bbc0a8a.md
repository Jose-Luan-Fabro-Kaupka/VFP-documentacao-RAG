# Propriedade InsertCmdDataSourceType

Especifica o tipo de fonte de dados da fonte de dados na propriedade InsertCmdDataSource. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.InsertCmdDataSourceType [= cDataSourceType]
```

# Valor de retorno
 **cDataSourceType**
Tipo de dados caractere. O parâmetro cDataSourceType especifica o tipo de fonte de dados da fonte de dados na propriedade InsertCmdDataSource.

# Observações

Aplica-se a: CursorAdapter Class

Se InsertCmdDataSourceType estiver vazio ("") ou for null (.NULL.), o Visual FoxPro ignora a propriedade CursorAdapter InsertCmdDataSource Property e usa as propriedades CursorAdapter DataSource Property (Visual FoxPro) e DataSourceType Property.

Para gerar um XML UpdateGram, você deve definir o valor de InsertCmdDataSourceType como "XML".
