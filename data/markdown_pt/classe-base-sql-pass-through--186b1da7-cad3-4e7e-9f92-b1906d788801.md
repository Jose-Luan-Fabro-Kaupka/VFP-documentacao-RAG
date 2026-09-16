# Classe base SQL Pass Through

Esta classe é usada para SQL Pass Through e torna possível executar stored procedures em um banco de dados host como o Microsoft SQL Server.

| Categoria | Data Query |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Classe | _execsp |
| Classe base | Custom |
| Biblioteca de classes | _dataquery.vcx |
| Classe pai | _custom |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Galeria de Componentes, selecione Add to Project ou Add to Form. Quando você solta a classe em um formulário, o Visual FoxPro coloca o ícone da classe no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Você precisa adicionar código que especifique informações de parâmetro e conexão para que a classe possa retornar um conjunto de resultados em um cursor.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| LUseSQLSyntax | Especifica se deve usar sintaxe Server Exec. Padrão: .F. |
| Método DoSQL | Executa uma instrução SQL Pass Through. Sintaxe: DoSQL( ) Retorno: nenhum Argumentos: nenhum |
| Método GetSQL | Obtém resultados da instrução SQL Pass Through. Sintaxe: GetSQL( ) Retorno: nenhum Argumentos: nenhum |
| Propriedade aParams[1,0] | Interno à classe. |
| Propriedade cCursorName | Interno à classe. |
| Propriedade cSpname | Interno à classe. |
| Propriedade cSQL | Interno à classe. |
| Propriedade hConnectHandle | Interno à classe. |
| Método ProcessError | Interno à classe. |
| Método SetParams | Interno à classe. |
| Método SetSQL | Interno à classe. |
