# Propriedade RefreshCmdDataSource

Especifica a origem de dados usada para o método RecordRefresh. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.RefreshCmdDataSource[ = DataSource]
```

#### Parâmetros
 **DataSource**
Especifica uma referência a uma origem de dados existente de tipos de origem de dados permitidos. DataSource atua apenas como um ponteiro para a origem de dados real, que deve existir em tempo de execução. A tabela a seguir lista os valores para DataSource, que dependem do valor da propriedade RefreshCmdDataSourceType Property. DataSource Tipo DataSource "ADO" Referência a um objeto Command ActiveX Data Object (ADO) válido "ODBC" Inteiro positivo que representa ou variável de memória que contém um identificador de conexão Open Database Connectivity (ODBC) válido "Native", null (.NULL.) ou cadeia de caracteres vazia ("") Ignorado. O valor padrão é o valor nulo (.NULL.).

# Observações

Aplica-se a: Classe CursorAdapter

Você pode definir esta propriedade no evento BeforeRecordRefresh.
