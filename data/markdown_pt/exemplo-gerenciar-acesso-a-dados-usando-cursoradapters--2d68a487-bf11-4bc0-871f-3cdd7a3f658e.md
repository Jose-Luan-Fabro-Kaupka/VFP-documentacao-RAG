# Exemplo Gerenciar acesso a dados usando CursorAdapters

Arquivo: ...\Samples\Solution\Toledo\CASample.scx

Este exemplo demonstra como objetos CursorAdapter recuperam dados de três tipos diferentes de fonte de dados:
 - Native Este exemplo demonstra um cursor Native conectado ao banco de dados Northwind do Visual FoxPro.
- Open Database Connectivity (ODBC) Este exemplo demonstra um cursor ODBC conectado ao banco de dados Northwind do SQL Server, se instalado.
- ActiveX® Data Objects (ADO) Este exemplo demonstra um cursor ADO conectado ao banco de dados Northwind do SQL Server, se instalado.

Os cursors são com buffer de linha e usam atualizações automáticas, portanto, quando você sai da linha, quaisquer alterações na linha são enviadas ao banco de dados.

Para visualizar as configurações de propriedade dos objetos CursorAdapter, clique no botão View CursorAdapter Properties. Essas configurações de propriedade foram definidas usando o CursorAdapter Builder.
