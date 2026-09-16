# Propriedade InsertCmdDataSource

Especifica a fonte de dados a usar para a propriedade InsertCmd. Leitura/gravação em tempo de design e em tempo de execução.

> **Observação:** A propriedade InsertCmdDataSourceType do CursorAdapter determina como a propriedade InsertCmdDataSource é usada.

```foxpro
CursorAdapter.InsertCmdDataSource [= cDataSource]
```

# Valor de retorno
 **cDataSource**
Tipo de dados Character. O parâmetro cDataSource especifica a fonte de dados usada pela propriedade InsertCmd.

# Observações

Aplica-se a: Classe CursorAdapter

A tabela a seguir descreve comportamentos que se aplicam a InsertCmdDataSource dependendo do valor de InsertCmdDataSourceType.

| InsertCmdDataSourceType | Comportamento de InsertCmdDataSource |
| --- | --- |
| Vazio ("") | InsertCmdDataSource é ignorado. O Visual FoxPro usa a fonte de dados na propriedade DataSource do CursorAdapter. No entanto, se o cursor associado ao objeto CursorAdapter é baseado em um ADO RecordSet, o Visual FoxPro usa a funcionalidade do ADO RecordSet para inserir o registro. Para usar essa funcionalidade, certifique-se de que a propriedade DataSourceType do CursorAdapter está definida como "ADO". |
| "ADO" | InsertCmdDataSource deve ser definido como um objeto ADO Command válido. A propriedade ActiveConnection do objeto ADO Command deve ser definida como um objeto ADO Connection válido e aberto. O Visual FoxPro define a propriedade CommandText do objeto ADO Command como o valor da propriedade InsertCmd do CursorAdapter. O Visual FoxPro analisa o comando para parâmetros, cria valores de parâmetro se encontrados e os define no objeto Command. A operação de inserção ocorre como: CursorAdapter.InsertCmdDataSource.Execute() Para obter mais informações sobre uso de um ADO RecordSet, atualização automática e geração automática de comandos SQL, consulte Gerenciamento de acesso a dados usando CursorAdapters. |
| "XML" | O Visual FoxPro ignora a propriedade DataSource do CursorAdapter. |
