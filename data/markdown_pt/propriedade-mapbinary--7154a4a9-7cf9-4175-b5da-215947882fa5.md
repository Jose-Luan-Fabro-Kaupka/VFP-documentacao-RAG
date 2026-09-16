# Propriedade MapBinary

A propriedade MapBinary do CursorAdapter habilita o mapeamento padrão de tipos de dados de ODBC e ADO para os tipos Varbinary Blob do Visual FoxPro.

A propriedade MapBinary do XMLAdapter habilita o mapeamento padrão de tipos de dados XML para os tipos Varbinary Blob do Visual FoxPro.

Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Object.MapBinary [= lValue]
```

# Valor de retorno
 **lValue**
Habilita o mapeamento padrão de tipos de dados para tipos de fonte de dados ODBC, ADO e XML. A tabela a seguir descreve os valores de lValue. lValue Descrição True (.T.) Para objetos CursorAdapter, o seguinte mapeamento de tipos de dados ocorre por padrão: o tipo ODBC SQL_LONGVARBINARY é mapeado para o tipo Blob. Os tipos ODBC SQL_BINARY e SQL_VARBINARY são mapeados para o tipo Varbinary quando a precisão da coluna correspondente na fonte de dados é igual ou menor que 254 bytes. Caso contrário, se a precisão for maior que 254 bytes, esses tipos são mapeados para o tipo Blob. Para tipos ADO, adVarBinary e adBinary são mapeados para o tipo Varbinary quando a precisão da coluna correspondente na fonte de dados é igual ou menor que 254 bytes. Caso contrário, se a precisão for maior que 254 bytes, esses tipos são mapeados para o tipo Blob. Para objetos XMLAdapter, o método LoadXML mapeia todos os tipos binários para o tipo Varbinary se seu tamanho for menor ou igual a 254 bytes. Caso contrário, se o tamanho for maior que 254 bytes, os tipos binários são mapeados para o tipo Blob. Quando a propriedade DataType do XMLField é definida como Varbinary ou Blob, a propriedade IsBinary do XMLField é definida como True (.T.) e a propriedade DisableEncode é definida como False (.F.) automaticamente. Observação Você não pode alterar as propriedades IsBinary e DisableEncode enquanto a propriedade DataType do XMLField estiver definida como Varbinary. False (.F.) (Padrão) Para objetos CursorAdapter, impede o mapeamento padrão de tipos remotos para os tipos Varbinary e Blob do Visual FoxPro. Para obter mais informações, consulte Data Type Conversion Control. Para objetos XMLAdapter, impede o mapeamento padrão de tipos XML para os tipos de dados Varbinary e Blob do Visual FoxPro. Para obter mais informações, consulte Visual FoxPro and XML Schema Data Type Mapping.

# Observações

Aplica-se a: CursorAdapter Class | XMLAdapter Class
