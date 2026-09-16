# Classe base Regular Expressions

Expressões regulares são uma notação concisa e flexível para encontrar e substituir padrões de texto. A classe Regular Expressions dá acesso a rotinas para usar expressões regulares em seus aplicativos.

| Category | System Utilities |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Class | _regexp |
| Base Class | Custom |
| Class Library | _regexp.vcx |
| Parent Class | _custom |
| Sample | ...\Samples\Solution\Ffc\Regexp.scx |

# Observações

Para informações sobre a amostra, consulte Search Text Using Regular Expressions Sample. Para detalhes gerais sobre expressões regulares, consulte o MSDN.

Para usar a classe base Regular Expressions, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca o ícone da classe no formulário. Você pode especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Properties, Events, Methods | Description |
| --- | --- |
| Matches array | Especifica a matriz que contém os resultados do teste de cadeia de caracteres. Padrão: .F. |
| Pattern property | Contém o padrão (expressão regular). Padrão: * |
| Clear method | Limpa todos os valores. Sintaxe: Clear( ) Retorno: nenhum Argumentos: |
| Execute method | Testa o padrão contra a cadeia de caracteres. Sintaxe: Execute(tcStr, tlCaseMatters) Retorno: número de correspondências Argumentos: tcStr especifica a cadeia de caracteres a pesquisar. tlCaseMatters especifica se a diferença entre maiúsculas e minúsculas deve ser ignorada. |
