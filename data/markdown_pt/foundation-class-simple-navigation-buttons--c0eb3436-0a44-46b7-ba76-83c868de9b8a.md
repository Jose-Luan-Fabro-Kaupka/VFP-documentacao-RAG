# Foundation Class Simple Navigation Buttons

Quando colocada em um projeto ou formulário, esta classe fornece um par simples de botões de navegação Next e Previous.

| Categoria | Data Navigation |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Data Navigation |
| Classe | _nav2Buttons |
| Classe base | Container |
| Biblioteca de classes | _table.vcx |
| Classe pai | _container |
| Amostra | ...\Samples\Solution\Forms\single.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário em um data environment ou, no menu de atalho do item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca os botões de comando no formulário. Você pode então especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade lCycle | Especifica se o movimento do ponteiro continua quando o final ou o início do arquivo é encontrado. Padrão: .F. |
| Método TableNav | Trata a navegação de registros. Sintaxe: TableNav(tcAction) Retorno: nenhum Argumentos: tcAction especifica uma ação de navegação como Next ou Previous. |
| Método lCycle_access | Interno à classe. |
