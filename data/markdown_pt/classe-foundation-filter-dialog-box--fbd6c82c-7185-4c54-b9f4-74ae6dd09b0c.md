# Classe Foundation Filter Dialog Box

Esta classe é uma caixa de diálogo que usa um objeto de filtro existente para permitir filtrar dados em um campo específico.

| Categoria | Data Query |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Classe | _filterdialog |
| Classe base | Form |
| Biblioteca de classes | _table.vcx |
| Classe pai | _form |
| Exemplo | ...\Samples\Solution\Ffc\datasort.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho do item da Component Gallery, selecione Create Form ou Add to Project. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Quando você solta a classe em um projeto ou escolhe Create a new form from the selected class no menu de atalho, o Visual FoxPro exibe uma caixa de diálogo Open para que você possa especificar o nome do formulário. Então o Visual FoxPro cria e abre o formulário no Form Designer.

_FilterDialog permite usar expressões do Visual FoxPro para construir um filtro complexo usando booleanos, condições aninhadas e assim por diante, limitado aos campos disponíveis nas tabelas abertas no momento. Ele fornece automaticamente delimitadores para vários tipos de campo. Ele sugere quais expressões podem ser otimizáveis verificando tags disponíveis na tabela atual. A lista de campos coloca "*" na frente dos nomes de campo que possuem tags de índice utilizáveis.

Como _FilterExpr, _FilterDialog precisa de pelo menos uma tabela aberta na qual pode definir um filtro. Diferentemente de _FilterExpr, _FilterDialog não é necessariamente modal; no entanto, é modal quando _FilterExpr a chama. FilterDialog determina a tabela atual no evento Init. FilterDialog nunca altera sessões de dados.

Quando chamado por _FilterExpr, _FilterDialog determina qual filtro o usuário já especificou na caixa de edição _FilterExpr e exibe essa expressão como seu conjunto inicial de condições. Quando _FilterDialog é chamado diretamente, ele verifica o alias atual para um filtro, usando SET("FILTER"), e mostra qualquer filtro atual como suas condições iniciais.

O método _FilterDialog SetUpFilter( ) usa as condições listadas na caixa de diálogo e cria uma expressão de filtro, depois aplica a função NORMALIZE( ) à expressão. O resultado é armazenado na propriedade cFilter. Quando você clica em OK, SetupFilter( ) é executado. _FilterDialog chama o método _FilterExpr.SetFilter se for chamado por uma instância de _FilterExpr; caso contrário, usa _table para determinar se a navegação é permitida, define o filtro diretamente e atualiza a exibição se o filtro for definido.

_FilterDialog é um objeto autônomo e não requer a existência de _FilterExpr para construir um filtro. No entanto, quando chamado por _FilterExpr, as duas caixas de diálogo trabalham juntas para construir um filtro, especificando uma expressão em _FilterExpr e fazendo escolhas em _FilterDialog. Para obter mais informações sobre a classe Filter Expression, consulte Classe Foundation Filter Expression Dialog Box.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes foundation.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cFilter | Contém a expressão de filtro processada no método SetupFilter. Padrão: "" |
| Método SetupFilter | Este método pega as condições listadas na caixa de diálogo e as transforma em uma expressão de filtro, depois aplica a função NORMALIZE( ) à expressão. Sintaxe: SetupFilter(tcValue) Retorno: cFilter Argumentos: tcValue especifica uma expressão para usar como filtro. cFilter é o valor contido na propriedade cFilter. |
| Propriedade cOldexact | Interna à classe. |
| Propriedade iBact | Interna à classe. |
| Propriedade iQptr | Interna à classe. |
| Propriedade iQuerymax | Interna à classe. |
| Propriedade iSelect | Interna à classe. |
| Propriedade oCaller | Interna à classe. |
| Propriedade aDBFs[1,0] | Interna à classe. |
| Propriedade aTags[1,0] | Interna à classe. |
| Propriedade aQuery[1,0] | Interna à classe. |
| Propriedade aFLDs[1,0] | Interna à classe. |
| Método SetAction | Interno à classe. |
| Método QReset | Interno à classe. |
| Método QSet | Interno à classe. |
| Método FSet | Interno à classe. |
| Método NoBrack | Interno à classe. |
| Método Brackets | Interno à classe. |
| Método SetTags | Interno à classe. |
| Método OnTag | Interno à classe. |
| Método NoTag | Interno à classe. |
| Método EditQuery | Interno à classe. |
| Método SetRowsources | Interno à classe. |
| Método SetInitialQueryParts | Interno à classe. |
