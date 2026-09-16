# Classe Foundation Find Button

Esta classe fornece um botão Find genérico, usa o objeto Find e localiza um registro com base em critérios específicos.

| Categoria | Data Query |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Classe | _findbutton |
| Classe base | Container |
| Biblioteca de classes | _table.vcx |
| Classe pai | _container |
| Exemplo | ...\Samples\Solution\Ffc\dataqry.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um builder para que você possa especificar os valores apropriados de cFindString, lMatchCase, lSkipMemo e lWraparound. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de foundation classes.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cAlias | Especifica a fonte de dados na qual pesquisar. Padrão: "" |
| Propriedade cFindString | Especifica a cadeia de caracteres a ser pesquisada. Padrão: "" |
| LFindAgain | Especifica se o arquivo é percorrido para encontrar instâncias sucessivas de cFindString . Padrão: .F. |
| Propriedade lMatchCase | Especifica a sensibilidade a maiúsculas e minúsculas da pesquisa. Padrão: .F. |
| Propriedade lSkipMemos | Especifica se os campos Memo devem ser ignorados na pesquisa. Padrão: .F. |
| Propriedade lWrapAround | Especifica se a pesquisa deve continuar desde o início se o final do arquivo (EOF) for atingido. Padrão: .F. |
| Método DoFind | Executa uma pesquisa. Sintaxe: DoFind( ) Retorno: nenhum Argumentos: nenhum |
| Método SkipField | Remove o campo, tcSkipField, da pesquisa. Sintaxe: SkipField( ) Retorno: nenhum Argumentos: tcSkipField especifica o campo a ser ignorado durante a pesquisa. |
