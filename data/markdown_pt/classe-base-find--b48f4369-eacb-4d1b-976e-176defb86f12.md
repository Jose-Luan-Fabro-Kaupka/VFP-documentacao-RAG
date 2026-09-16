# Classe base Find

Esta classe cria um objeto genérico que localiza um registro com base em critérios especificados. A classe também fornece um método Find Next opcional.

| Category | Data Query |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Class | _tablefind |
| Base Class | Custom |
| Class Library | _table.vcx |
| Parent Class | _table |
| Sample | ...\Samples\Solution\Ffc\dataqry.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um builder para que você possa especificar os valores apropriados de cFindString, lMatchCase, lSkipMemo, lWrapAround. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Properties, Events, Methods | Description |
| --- | --- |
| cFields property | Especifica a lista de campos a pesquisar. Padrão: "" |
| cFindString property | Especifica a cadeia de caracteres a pesquisar. Padrão: "" |
| lFindAgain | Especifica se o arquivo é percorrido para encontrar instâncias sucessivas de cFindString . Padrão: .F. |
| lMatchCase property | Especifica se a pesquisa usa sensibilidade a maiúsculas e minúsculas. Padrão: .F. |
| lSkipMemos property | Especifica se os campos Memo são ignorados na pesquisa. Padrão: .F. |
| lWrapAround property | Especifica se a pesquisa continua desde o início se o final do arquivo (EOF) for atingido. Padrão: .F. |
| SkipField method | Remove tcSkipField da pesquisa. Sintaxe: SkipField( ) Retorno: nenhum Argumentos: tcSkipField especifica o campo a ignorar durante a pesquisa. |
| aMemos [1] property | Interno à classe. |
| iMemos property | Interno à classe. |
| cControlCharacter property | Interno à classe. |
