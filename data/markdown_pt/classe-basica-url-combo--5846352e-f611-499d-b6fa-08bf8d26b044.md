# Classe básica URL Combo

Esta classe, quando colocada em um formulário, cria uma caixa de combinação para inserir uma URL da Web. Ela inicia o Internet Explorer e navega até o site.

| Categoria | Internet |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Internet |
| Classe | _urlcombobox |
| Classe base | Combobox |
| Biblioteca de classes | _internet.vcx |
| Classe pai | _combobox |
| Exemplo | ...\Samples\Solution\Ffc\hyperlnk.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Component Gallery, selecione Add to Project ou Add to Form. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse. Quando você solta a classe em um formulário, o Visual FoxPro abre um builder para que você possa especificar os valores apropriados de cURL, cURLHistoryTable e iURLHistory no formulário no Form Designer. Você pode usar a tabela de histórico para fornecer um ou mais locais iniciais para navegação na Web.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes básicas.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| propriedade cURL | A URL atual. Padrão: "" |
| propriedade cURLHistoryTable | Especifica o nome da tabela de histórico de URL que retém URLs acessadas anteriormente. Padrão: (IIF(VERSION(2)=0,"",HOME( ))+"URLHst ry.dbf")) |
| propriedade lInitialized | Sinalizador de controle inicializado. Padrão: .F. |
| propriedade lURLHistory | Salva o histórico de URL. Padrão: .T. |
| método Navigate | Solicita o documento com base no endereço URL. Sintaxe: Navigate( ) Retorno: nenhum Argumentos: nenhum |
| propriedade cHyperlinkClass | Interno à classe. |
| propriedade cHyperlinkclasslibrary | Interno à classe. |
| propriedade cTempFilePrefix | Interno à classe. |
| propriedade lDropDown | Interno à classe. |
| propriedade lFormNavigate | Interno à classe. |
| propriedade lGotFocus | Interno à classe. |
| propriedade lMoveFocus | Interno à classe. |
| propriedade lRequestOnEnter | Interno à classe. |
| propriedade oHyperlink | Interno à classe. |
| método Initialize | Interno à classe. |
| método oHyperlink_access | Interno à classe. |
| método OpenURLHistory | Interno à classe. |
| método ValidURL | Interno à classe. |
