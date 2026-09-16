# Suporte a dados do provedor OLE DB do Visual FoxPro

A tabela a seguir descreve os tipos e outras características de arquivo e código de dados suportados pelo provedor OLE DB do Visual FoxPro.

| Tipo de dados | Indicador | Tamanho | Intervalo | Tipo OLE DB |
| --- | --- | --- | --- | --- |
| Character | C | 1 byte por caractere até 254 | Qualquer caractere | DBTYPE_STR |
| Character (binary) | C NOCPTRANS | 1 byte por caractere até 254 | Qualquer caractere | DBTYPE_BYTES |
| Date | D | 8 bytes | 0001-01-01 a 9999-12-31 | DBTYPE_DATE |
| DateTime | T | 8 bytes | 0001-01-01 a 9999-12-31; 00:00:00 a.m. a 11:59:59 p.m. | DBTYPE_DBTIMESTAMP |
| Numeric | N | 1 a 20 bytes | - .9999999999E+19 a .9999999999E+20 | DBTYPE_DECIMAL |
| Float | F | 1 a 20 bytes | - .9999999999E+19 a .9999999999E+20 | DBTYPE_DECIMAL |
| Integer | I | 4 bytes | 2147483647 a 2147483647 | DBTYPE_I4 |
| Double | B | 8 bytes | +/-4.94065645841247E-324 a +/-8.9884656743115E307 | DBTYPE_R8 |
| Currency | Y | 8 bytes | - 922337203685477.5807 a 922337203685477.5807 | DBTYPE_CY |
| Logical | L | .T./.F. | DBTYPE_BOOL | |
| Memo | M | 4 bytes na tabela | Memória disponível | DBTYPE_BYTES |
| Memo (binary) | M NOCPTRANS | 4 bytes na tabela | Memória disponível | DBTYPE_BYTES |
| General (blob) | G | 4 bytes na tabela | Memória disponível | DBTYPE_BYTES |

A tabela a seguir descreve o mapeamento dos tipos OLE DB do Visual FoxPro para tipos do Visual Studio:

| Indicador | Tipo OLE DB | Tipo Visual Studio |
| --- | --- | --- |
| C | DBTYPE_STR | System.String |
| C NOCPTRANS | DBTYPE_BYTES | System.String |
| D | DBTYPE_DATE | System.DateTime |
| T | DBTYPE_DBTIMESTAMP | System.DateTime |
| N | DBTYPE_NUMERIC | System.Decimal |
| F | DBTYPE_NUMERIC | System.Decimal |
| I | DBTYPE_I4 | System.Int32 |
| B | DBTYPE_R8 | System.Double |
| Y | DBTYPE_CY | System.Decimal |
| M | DBTYPE_STR | System.String |
| M NOCPTRANS | DBTYPE_BYTES | System.Byte |
| G | DBTYPE_BYTES | System.Byte |
