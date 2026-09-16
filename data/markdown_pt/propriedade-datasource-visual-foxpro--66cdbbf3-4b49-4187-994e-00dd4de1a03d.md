# Propriedade DataSource (Visual FoxPro)

Especifica a origem de dados que os objetos DataEnvironment e CursorAdapter devem usar. A propriedade DataSourceType do DataEnvironment ou CursorAdapter determina o valor da propriedade DataSource correspondente. Leitura/gravação em tempo de design e em tempo de execução. Há duas versões da sintaxe.

```foxpro
DataEnvironment.DataSource [= DataSource]
```

```foxpro
CursorAdapter.DataSource [= DataSource]
```

# Valor de retorno
 **DataSource**
Especifica uma referência a uma origem de dados existente de tipos permitidos. DataSource atua apenas como um ponteiro para a origem de dados real, que deve existir em tempo de execução. A tabela a seguir lista os valores para DataSource, que dependem do valor da propriedade DataSourceType. DataSource DataSourceType Referência a um objeto RecordSet ActiveX Data Object (ADO) válido "ADO" Inteiro positivo que representa ou variável de memória que contém um identificador de conexão Open Database Connectivity (ODBC) válido "ODBC" Ignorado. "Native", "XML", null (.NULL.) ou cadeia de caracteres vazia ("")

# Observações

Aplica-se a: Classe CursorAdapter | Objeto DataEnvironment

Quando o CursorAdapter DataSourceType é "Native", não é necessário especificar CursorAdapter DataSource porque o cursor retornado pela propriedade SelectCmd Property do CursorAdapter é a origem de dados padrão. O nome do cursor retornado é determinado pela propriedade Alias do CursorAdapter, que é definida pelo método CursorFill do CursorAdapter.

Se as propriedades InsertCmdDataSourceType Property, UpdateCmdDataSourceType Property e DeleteCmdDataSourceType Property do CursorAdapter estiverem vazias, a propriedade DataSource do CursorAdapter substitui as propriedades InsertCmdDataSource Property, UpdateCmdDataSource Property e DeleteCmdDataSource Property do CursorAdapter.

Se a propriedade UseDeDataSource do CursorAdapter for True (.T.), as propriedades DataSource e DataSourceType do DataEnvironment substituem as mesmas propriedades do CursorAdapter.
