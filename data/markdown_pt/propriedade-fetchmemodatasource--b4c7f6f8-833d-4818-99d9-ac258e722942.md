# Propriedade FetchMemoDataSource

Especifica a fonte de dados usada para o método DelayedMemoFetch. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.FetchMemoDataSource[ = DataSource]
```

#### Parâmetros
 **DataSource**
Especifica uma referência a uma fonte de dados existente de tipos de fonte de dados permitidos. DataSource atua apenas como um ponteiro para a fonte de dados real, que deve existir em tempo de execução. A tabela a seguir lista os valores para DataSource , que dependem do valor da propriedade FetchMemoDataSourceType . DataSource DataSource Type "ADO" Referência a um objeto Command ActiveX Data Object (ADO) válido. "ODBC" Inteiro positivo que representa ou variável de memória que contém um identificador de conexão Open Database Connectivity (ODBC) válido. "Native", null (.NULL.) ou cadeia de caracteres vazia ("") Desconsiderado. O valor padrão é o valor nulo (.NULL.).

# Observações

Aplica-se a: CursorAdapter Class
