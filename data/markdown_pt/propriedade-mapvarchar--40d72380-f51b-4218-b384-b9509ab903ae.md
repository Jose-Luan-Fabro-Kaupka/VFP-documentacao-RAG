# Propriedade MapVarchar

A propriedade MapVarchar do CursorAdapter habilita o mapeamento padrão de tipos de dados ODBC e ADO para o tipo de dados Varchar do Visual FoxPro.

A propriedade MapVarchar do XMLAdapter habilita o mapeamento padrão de tipos de dados XML para o tipo de dados Varchar do Visual FoxPro.

Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Object.MapVarchar [= lValue]
```

# Valor de retorno
 **lValue**
Habilita o mapeamento padrão de tipos de dados ODBC, ADO e XML para o tipo de dados Varchar do Visual FoxPro. A tabela a seguir descreve os valores de lValue. lValue Descrição True (.T.) Para objetos CursorAdapter, o seguinte mapeamento de tipos de dados ocorre por padrão: os tipos de dados ODBC SQL_WVARCHAR e SQL_VARCHAR são mapeados para o tipo Varchar quando a precisão da coluna correspondente na fonte de dados é igual ou inferior a 254 bytes. Caso contrário, se a precisão for superior a 254 bytes, esses tipos são mapeados para o tipo Memo. Os tipos de dados ADO adVarChar e adVarWChar são mapeados para o tipo Varchar quando possível. Para objetos XMLAdapter, o Visual FoxPro mapeia dados que anteriormente eram mapeados para o tipo Character para o tipo Varchar. False (.F.) (Padrão) Para objetos CursorAdapter, impede o mapeamento padrão de tipos remotos para o tipo de dados Varchar do Visual FoxPro. Para obter mais informações, consulte Data Type Conversion Control. Para objetos XMLAdapter, impede o mapeamento padrão de tipos XML para o tipo de dados Varchar do Visual FoxPro. Para obter mais informações, consulte Visual FoxPro and XML Schema Data Type Mapping.

# Observações

Aplica-se a: CursorAdapter Class | XMLAdapter Class
