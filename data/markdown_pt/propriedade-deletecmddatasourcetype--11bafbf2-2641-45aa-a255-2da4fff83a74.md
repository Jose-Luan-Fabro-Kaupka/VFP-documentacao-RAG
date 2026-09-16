# Propriedade DeleteCmdDataSourceType

Especifica o tipo da fonte de dados usada pela propriedade DeleteCmdDataSource. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.DeleteCmdDataSourceType [= cDataSourceType]
```

# Valor de retorno
 **cDataSourceType**
Tipo de dados caractere. O parâmetro cDataSourceType especifica o tipo da fonte de dados da propriedade DeleteCmdDataSource.

# Observações

Aplica-se a: classe CursorAdapter

Se DeleteCmdDataSourceType estiver vazia ("") ou for nula (.NULL.), o Visual FoxPro desconsiderará a propriedade CursorAdapter DeleteCmdDataSource e usará as propriedades CursorAdapter DataSource e DataSourceType.

Para gerar um XML UpdateGram, você deve definir o valor de DeleteCmdDataSourceType como "XML".
