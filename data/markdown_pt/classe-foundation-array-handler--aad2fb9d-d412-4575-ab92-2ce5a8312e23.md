# Classe foundation Array Handler

Esta classe fornece métodos para manipular certas operações de array que não são realizadas pelas funções de array do Visual FoxPro, incluindo inserir e excluir elementos de array específicos e examinar um array por coluna.

| Categoria | Data Utilities |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Classe | _arraylib |
| Classe base | Custom |
| Biblioteca de classes | _utility.vcx |
| Classe pai | _custom |
| Amostra | ...\Samples\Solution\Ffc\arrays.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca o ícone da classe no formulário. Você pode especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de foundation classes.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Método AColScan | Examina a coluna nColumn do array aSearch pelo valor especificado em sExpr . Sintaxe: AcolScan(@aSearch, sExpr, nColumn, lRetRow) Retorno: nenhum Argumentos: aSearch especifica o array a analisar. sExpr especifica a expressão a buscar. nColumn especifica a coluna do array na qual buscar sExpr. lRetRow especifica se o método retorna o número da linha em que sExpr foi encontrado. |
| Método DelAitem | Exclui um elemento de array. Sintaxe: DelAitem(@aArray, wziRow) Retorno: nenhum Argumentos: aArray especifica o nome do array sendo processado. wziRow especifica o item a ser excluído. |
| Método InsAitem | Insere um elemento de array. Sintaxe: InsAitem(@aArray, sContents, iRow) Retorno: nenhum Argumentos: aArray especifica o nome do array sendo processado. sContents especifica um valor de cadeia de caracteres a ser adicionado a aArray . iRow especifica a linha na qual inserir o valor em sContents . |
