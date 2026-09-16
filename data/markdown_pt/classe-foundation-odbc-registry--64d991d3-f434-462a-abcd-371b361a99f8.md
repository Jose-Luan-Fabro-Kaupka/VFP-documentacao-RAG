# Classe Foundation ODBC Registry

Esta classe fornece um conjunto de funções de registro que retornam informações específicas de ODBC, como drivers e fontes de dados.

| Categoria | System Utilities |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Classe | _odbcreg |
| Classe base | Custom |
| Biblioteca de classes | registry.vcx |
| Classe pai | registry |
| Exemplo | ...\Samples\Solution\WinAPI\regodbc.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Item da Galeria de Componentes, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca a classe no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer os objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes foundation.

| Propriedades, Eventos, Métodos | Descrição |
| --- | --- |
| Método LoadODBCFuncs | Carrega as funções de registro ODBC. Sintaxe: LoadODBCFuncs( ) Retorno: nenhum Argumentos: nenhum |
| Método GetODBCDrvrs | Recupera drivers ODBC. Sintaxe: GetODBCDrvrs(@aDrvrs, lDataSources) Retorno: nRetVal Argumentos: aDrvrs especifica, em um array, os drivers a recuperar. lDataSources especifica se deve acessar fontes de dados. |
| Método EnumODBCDrvrs | Enumera os drivers ODBC. Sintaxe: EnumODBCDrvrs(@aDrvrOpts, cODBCDriver) Retorno: aDrvrOpts, m.cSourceKey, HKEY_LOCAL_MACHINE, .F. Argumentos: aDrvrOpts especifica as opções de driver disponíveis. cODBCDriver especifica o nome do driver. |
| Método EnumODBCData | Enumera as fontes de dados ODBC. Sintaxe: EnumODBCData(@aDrvrOpts, cDataSource) Retorno: aDrvrOpts, m.cSourceKey, HKEY_CURRENT_USER, .F. Argumentos: aDrvrOpts especifica as opções de driver disponíveis. cDataSource especifica o nome da fonte de dados. |
