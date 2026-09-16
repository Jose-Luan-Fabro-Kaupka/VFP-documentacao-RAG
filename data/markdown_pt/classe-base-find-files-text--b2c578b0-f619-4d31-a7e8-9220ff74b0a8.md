# Classe base Find Files/Text

Esta classe wrapper usa o objeto COM FILER.DLL para pesquisar arquivos. É uma versão simplificada do formulário filer.

| Categoria | File Utilities |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Classe | _filer |
| Classe base | Custom |
| Biblioteca de classes | _utility.vcx |
| Classe pai | _custom |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um builder para que você possa especificar os valores apropriados de cFileExpression, cSearchPath, cSearchText, lIgnoreCase, lSubFolder e lWholeWords. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes base.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cFileExpression | Especifica um esqueleto de arquivo para a pesquisa. Esta expressão pode incluir curingas como ? e *. Padrão: "" |
| Propriedade cSearchPath | Especifica o diretório no qual iniciar a pesquisa de arquivos. Padrão: "" |
| Propriedade cSearchText | Especifica a cadeia de caracteres de texto a pesquisar dentro dos arquivos. Padrão: "" |
| Propriedade lIgnoreCase | Especifica se deve ignorar maiúsculas e minúsculas durante a pesquisa. Padrão: .T. |
| Propriedade lPromptDir | Especifica se deve solicitar ao usuário um caminho de pesquisa se nenhum for inserido. Padrão: .T. |
| Propriedade lSubFolder | Especifica se deve pesquisar em subpastas por arquivos. Padrão: .T. |
| Propriedade lWholeWords | Especifica se deve pesquisar correspondências de palavras inteiras. Padrão: .F. |
| Propriedade oFiles | Especifica uma coleção de arquivos retornados pela pesquisa Find. Padrão: .F. |
| Método Find | Pesquisa arquivos que atendem aos critérios especificados pelas propriedades. Sintaxe: Find( ) Retorno: nenhum Argumentos: nenhum |
