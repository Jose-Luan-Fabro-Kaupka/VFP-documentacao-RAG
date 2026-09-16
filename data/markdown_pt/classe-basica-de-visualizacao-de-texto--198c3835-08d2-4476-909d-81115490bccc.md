# Classe básica de visualização de texto

Quando usada em um projeto ou formulário, esta classe fornece um editor de texto simples em uma caixa de diálogo que também contém botões para formatar ou salvar texto e fechar o editor.

| Categoria | Relatórios |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output |
| Classe | _showtext |
| Classe base | Form |
| Biblioteca de classes | _reports.vcx |
| Classe pai | _form |
| Exemplo | ...\Samples\Solution\Ffc\output.scx |

# Observações

O principal objetivo desta classe é fornecer uma janela de visualização controlável para outras classes em _reports.vcx. Portanto, essa caixa de diálogo não possui um botão para carregar um novo arquivo (embora você possa adicionar um em uma subclasse), e sua caixa de edição é somente leitura por padrão.

Para usá-la, solte a classe em um projeto ou, no menu de atalho do item da Galeria de Componentes, selecione Adicionar ao projeto. Ao soltar a classe em um projeto, você pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Quando você escolhe Criar um novo formulário com base na classe selecionada, o Visual FoxPro abre um construtor para que você especifique o nome do formulário; em seguida, cria e abre o formulário no Designer de Formulários.

Consulte Diretrizes para usar as classes básicas do Visual FoxPro para obter mais informações sobre o uso de classes básicas.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cFixedFontName | O nome da fonte para o conteúdo da caixa de edição. Padrão: Courier New |
| Propriedade nFixedFontSze | O tamanho da fonte para o conteúdo da caixa de edição. Padrão: 9 |
| Propriedade cSourceFile | O nome do arquivo de origem a ser exibido ou editado. Padrão: "" |
| Propriedade cTargetFile | O nome do arquivo no qual o conteúdo da caixa de edição será salvo. Padrão: "" |
| Propriedade lFixedFontBold | Especifica uma fonte em negrito para o conteúdo da caixa de edição. Padrão: .F. |
| Propriedade lFixedFontiItalic | Especifica uma fonte em itálico para o conteúdo da caixa de edição. Padrão: .F. |
| Propriedade lSuppressCaptionChange | Impede que a legenda da caixa de diálogo seja alterada quando o arquivo de origem muda. Isso é útil para exibir o conteúdo de um arquivo temporário. Padrão: .F. |
| Método SetFonts | Aplica à caixa de edição que exibe o arquivo as características atuais das propriedades de fonte. Sintaxe: SetFonts( ) Retorno: nenhum Argumentos: nenhum |
| Método GetFixedFont | Usa uma caixa de diálogo comum para exibir fontes. Restrito a itens de fonte de largura fixa. Sintaxe: GetFixedFont( ) Retorno: nenhum Argumentos: nenhum |
| Método cTargetfile_access | Interno à classe. |
| Método cSourcefile_assign | Interno à classe. |
