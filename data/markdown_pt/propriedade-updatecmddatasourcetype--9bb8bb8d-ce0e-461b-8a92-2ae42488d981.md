# Propriedade UpdateCmdDataSourceType

Especifica o tipo de fonte de dados para a fonte de dados usada pela propriedade UpdateCmdDataSource Property. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.UpdateCmdDataSourceType [= cDataSourceType]
```

# Valor de retorno
 **cDataSourceType**
Tipo de dados Character. O parâmetro cDataSourceType especifica o tipo de fonte de dados da fonte de dados na propriedade UpdateCmdDataSource.

# Observações

Aplica-se a: CursorAdapter Class

Se UpdateCmdDataSourceType estiver vazio ("") ou nulo (.NULL.), o Visual FoxPro usa a fonte de dados na propriedade DataSource Property (Visual FoxPro) do CursorAdapter.

Para gerar um UpdateGram XML, você deve definir explicitamente o valor de UpdateCmdDataSourceType como "XML".
