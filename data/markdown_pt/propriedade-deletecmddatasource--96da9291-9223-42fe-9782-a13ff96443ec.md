# Propriedade DeleteCmdDataSource

Especifica a fonte de dados usada pela propriedade DeleteCmd Property. Leitura/gravação em tempo de design e em tempo de execução.

> **Observação:** A propriedade CursorAdapter DeleteCmdDataSourceType determina como a propriedade DeleteCmdDataSource é usada.

```foxpro
CursorAdapter.DeleteCmdDataSource [ = cDataSource]
```

# Valor de retorno
 **cDataSource**
Tipo de dados caractere. O parâmetro cDataSource especifica a fonte de dados usada pela propriedade DeleteCmd.

# Observações

Aplica-se a: CursorAdapter Class

A tabela a seguir descreve comportamentos adicionais que se aplicam a DeleteCmdDataSource dependendo do valor de DeleteCmdDataSourceType.

| DeleteCmdDataSourceType | Comportamento de DeleteCmdDataSource |
| --- | --- |
| Empty ("") | DeleteCmdDataSource é ignorado. O Visual FoxPro usa a fonte de dados na propriedade CursorAdapter DataSource. Se o cursor associado ao objeto CursorAdapter for baseado em um ActiveX Data Object (ADO) RecordSet, o Visual FoxPro usa a funcionalidade do ADO RecordSet para excluir o registro. Para usar esta funcionalidade, certifique-se de que a propriedade CursorAdapter DataSourceType esteja definida como "ADO". |
| "ADO" | DeleteCmdDataSource deve ser definido como um objeto ADO Command válido. A propriedade ActiveConnection do objeto ADO Command deve ser definida como um objeto ADO Connection válido e aberto. O Visual FoxPro define a propriedade CommandText do objeto ADO Command como o valor da propriedade CursorAdapter DeleteCmd. O Visual FoxPro analisa o comando em busca de parâmetros, cria valores de parâmetro se encontrados e os define no objeto Command. A operação de exclusão ocorre como: CursorAdapter.DeleteCmdDataSource.Execute() Para obter mais informações sobre o uso de um ADO RecordSet, atualização automática e geração automática de comandos SQL, consulte Data Access Management Using CursorAdapters . |
