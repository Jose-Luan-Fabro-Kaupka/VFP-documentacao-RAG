# Propriedade UpdateCmdDataSource

Especifica a fonte de dados usada pela propriedade UpdateCmd. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.UpdateCmdDataSource [= cDataSource]
```

# Valor de retorno
 **cDataSource**
Tipo de dados Character. O parâmetro cDataSource especifica a fonte de dados usada pela propriedade UpdateCmd.

# Observações

Aplica-se a: CursorAdapter Class

A tabela a seguir descreve comportamentos que se aplicam a UpdateCmdDataSource dependendo do valor de UpdateCmdDataSourceType.

| UpdateCmdDataSourceType | Comportamento de UpdateCmdDataSource |
| --- | --- |
| Vazio ("") | UpdateCmdDataSource é ignorado. O Visual FoxPro usa a fonte de dados na propriedade DataSource do CursorAdapter. No entanto, se o cursor associado ao objeto CursorAdapter é baseado em um ActiveX Data Object (ADO) RecordSet, o Visual FoxPro usa a funcionalidade do ADO RecordSet para atualizar um registro. Para usar essa funcionalidade, certifique-se de que a propriedade DataSourceType do CursorAdapter está definida como "ADO". |
| "ADO" | UpdateCmdDataSource deve ser definido como um objeto ADO Command válido. A propriedade ActiveConnection do objeto ADO Command deve ser definida como um objeto ADO Connection válido e aberto. O Visual FoxPro define a propriedade CommandText do objeto ADO Command como o valor da propriedade UpdateCmd do CursorAdapter. O Visual FoxPro analisa o comando para parâmetros, cria valores de parâmetro se encontrados e os define no objeto Command. A operação de atualização ocorre como: CursorAdapter.UpdateCmdDataSource.Execute() Para obter mais informações sobre como usar um ADO RecordSet, atualização automática e geração automática de comandos SQL, consulte Data Access Management Using CursorAdapters. |
