# Foundation Class Messagebox Handler

Esta classe fornece um wrapper simples em torno da função MessageBox para que você possa exibir facilmente uma caixa de mensagem de um tipo especificado com conteúdo alternativo.

| Categoria | Misc Forms |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Classe | _msgbox |
| Classe base | Custom |
| Biblioteca de classes | _dialogs.vcx |
| Classe pai | _custom |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, especifique os valores apropriados para a mensagem (cMessage), o tipo de caixa de mensagem (nType) e outras propriedades apropriadas. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de foundation classes.

| Properties, Events, Methods | Descrição |
| --- | --- |
| Propriedade cMessage | Especifica o texto da mensagem da caixa de mensagem. Padrão: "" |
| Propriedade nType | Especifica o tipo da caixa de mensagem. Para opções, consulte MessageBox( ). Padrão: 48 |
| Propriedade cTitle | Especifica o texto do título da caixa de mensagem. Padrão: _screen.caption |
| Propriedade lBeep | Especifica se ocorre um beep quando a caixa de mensagem é ativada. Padrão: .F. |
| Método Show | Exibe uma caixa de mensagem e retorna o resultado da caixa de diálogo. Sintaxe: Show(tcMessage, tnType, tcTitle, tlBeep) Retorno: this.Display( ) Argumentos: tcMessage especifica o texto que aparece na caixa de diálogo. tnType especifica as opções de botões e ícones, o botão padrão e o comportamento da caixa de diálogo. tcTitle especifica o texto que aparece na barra de título da caixa de diálogo. tlBeep especifica se um som de alerta acompanha a exibição da caixa de diálogo. |
| Método Set | Define as propriedades para a mensagem, tipo, título e som de alerta da caixa de diálogo. Interno à classe. Sintaxe: Set(tcMessage, tnType, tcTitle, tlBeep, tnParameters) Retorno: none Argumentos: tcMessage especifica o texto que aparece na caixa de diálogo. tnType especifica as opções de botões e ícones, o botão padrão e o comportamento da caixa de diálogo. tcTitle especifica o texto que aparece na barra de título da caixa de diálogo. tlBeep especifica se um som de alerta acompanha a exibição da caixa de diálogo. |
