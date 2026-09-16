# Propriedade DataSourceType

Especifica o tipo de fonte de dados da fonte de dados na propriedade DataSource do DataEnvironment ou do CursorAdapter. A propriedade DataSourceType do DataEnvironment ou do CursorAdapter determina o valor da propriedade DataSource correspondente. Somente leitura em tempo de design e leitura/gravação em tempo de execução. Há duas versões da sintaxe.

```foxpro
DataEnvironment.DataSourceType [= cDataSourceType]
```

```foxpro
CursorAdapter.DataSourceType [= cDataSourceType]
```

# Valor de retorno
 **cDataSourceType**
Tipo de dados Character. O parâmetro cDataSourceType especifica uma cadeia de caracteres que descreve o tipo de fonte de dados da fonte de dados usada pelo ambiente de dados ou pelo cursor adapter. A tabela a seguir lista os valores de cDataSourceType. DataSourceType DataSource "ADO" Referência a um objeto RecordSet ou Command ActiveX Data Object (ADO) válido "ODBC" Um identificador de conexão Open Database Connectivity (ODBC) válido "Native", "XML", null (.NULL.) ou cadeia vazia ("") Desconsiderado

# Observações

Aplica-se a: Classe CursorAdapter | Objeto DataEnvironment

Você não pode usar views locais e remotas como fonte "Native" para objetos CursorAdapter, mas pode anexá-las usando o método CursorAttach.

O DataSourceType do DataEnvironment não é especificado em tempo de design quando o ambiente de dados não especifica uma fonte de dados.
