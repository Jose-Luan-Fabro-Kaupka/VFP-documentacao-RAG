# Classe base Foundation Keywords Dialog Box

Esta classe cria uma caixa de diálogo que exibe uma lista especificada de palavras-chave, como a caixa de diálogo de palavras-chave do Component Gallery.

| Categoria | Misc Forms |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Dialogs |
| Classe | _keywords |
| Classe base | Form |
| Biblioteca de classes | dialogs . vcx |
| Classe pai | _dialog |
| Amostra | ...\Samples\Solution\Ffc\dialogs.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho do item do Component Gallery, selecione Create Form. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Quando você solta a classe em um projeto ou escolhe Criar um novo formulário da classe selecionada no menu de atalho, o Visual FoxPro abre um builder para que você possa especificar o nome do formulário, depois cria e abre o formulário no Form Designer.

Por padrão, a caixa de diálogo usa o arquivo Keywords.dbf do Component Gallery. Você pode especificar seu próprio arquivo de palavras-chave na propriedade cTablename. Você também pode fornecer um conjunto de palavras-chave em uma lista delimitada por vírgulas na propriedade cKeywords.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| propriedade cKeywords | Especifica um grupo de palavras-chave delimitadas por espaço a buscar na tabela especificada em cTablename . Padrão: "" |
| propriedade cTablename | Especifica o nome de uma tabela que contém palavras-chave. Padrão: (IIF(VERSION(2)=0,"",HOME( )+"gallery\")+"keywords.dbf")) |
| objeto oKeywords | O objeto que recupera a lista de palavras-chave definida na propriedade cKeywords. Padrão: .F. |
| método Apply | Exibe as palavras-chave especificadas pela propriedade cKeywords da tabela especificada em cTablename . Sintaxe: Apply( ) Retorno: nenhum Argumentos: nenhum |
| propriedade lAddMode | Interno à classe. |
| propriedade lUpdated | Interno à classe. |
| propriedade cLastValue | Interno à classe. |
