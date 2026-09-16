# Exemplo de leitura de valores ODBC do Registro

Arquivo: ...\Samples\Solution\WINAPI\Regodbc.scx

Este exemplo mostra como acessar o Registro do Windows usando o comando nativo DECLARE-DLL do Visual FoxPro. A API do Windows fornece diversas funções para acessar, ler e gravar no Registro. A biblioteca de classes Registry.prg em ...\Samples\Classes contém uma definição de classe que expõe essas funções como métodos que podem ser chamados em seus aplicativos.

O Registro contém uma lista de todos os drivers e fontes de dados ODBC instalados. Se o aplicativo depende de ODBC, convém verificar o Registro para determinar se um driver ou uma fonte de dados específica está instalada. Este exemplo mostra como consultar informações ODBC.

```foxpro
LOCAL oReg,regfile,nErrNum,lDrivers
PUBLIC aODBCData
regfile = HOME(2)+"classes\registry.prg"
SET PROCEDURE TO (m.regfile) ADDITIVE
oReg = CreateObject("ODBCReg")
DIMENSION aODBCData[1]
m.nErrNum = oReg.GetODBCDrvrs(@aODBCData)
```
