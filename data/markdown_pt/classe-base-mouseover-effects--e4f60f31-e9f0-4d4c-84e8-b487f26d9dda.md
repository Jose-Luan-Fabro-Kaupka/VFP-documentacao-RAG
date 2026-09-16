# Classe base MouseOver Effects

Esta classe destaca um controle enquanto o mouse é arrastado sobre ele.

| Categoria | Interface do usuário |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\User Controls |
| Classe | _mouseoverfx |
| Classe base | Custom |
| Biblioteca de classes | _ui.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Ffc\mousefx.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, especifique os valores apropriados para o destaque (iHighlightColor e nHighlightWidth) e outras propriedades apropriadas, depois coloque uma referência ao método HighlightMe no evento MouseMove do controle que deseja afetar. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes base.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade nMargin | Especifica a borda entre o controle e o destaque. Padrão: 2 |
| Propriedade iShadowColor | Especifica o código de cor da sombra. Padrão: 0 |
| Propriedade lMouseoverHost | Especifica se o mouse está sobre o host mousefx. Padrão: .T. |
| Propriedade nHighlightWidth | Especifica a largura do destaque. Padrão: 2 |
| Propriedade iHighlightColor | Especifica o código de cor do destaque. Padrão: 0 |
| Método CancelHighlight | Usa o valor de lMouseoverHost para determinar se há um objeto destacado que requer alteração. Define oCurrentCoolControl como .NULL. e retorna verdadeiro (.T.) quando lMouseOver indica que o controle atual acabou de mudar. Suas subclasses podem verificar este valor de retorno ou o estado de lMouseOverHost e oCurrentCoolControl para "subtrair" seus próprios efeitos especiais de controles cool nos momentos apropriados. Sintaxe: CancelHighlight (toObject) Retorno: lChange Argumentos: toObject especifica o objeto afetado no evento MouseOver. lChange especifica se o controle atual já mudou. |
| Método HighlightMe | Define oCurrentCoolControl, o controle atual, como a referência de objeto especificada por toObject. Retorna verdadeiro (.T.) quando precisa agir porque o controle atual acabou de mudar. Retorna .F. se não precisa agir porque não há mudança no controle atual. Suas subclasses podem usar a propriedade oCurrentCoolControl e o valor de retorno deste método para decidir quando precisam agir, fornecendo outros efeitos especiais, talvez específicos para algumas classes especiais de "controles atuais". Sintaxe: HighlightMe(toObject) Retorno: lChange Argumentos: toObject especifica o objeto afetado no evento MouseOver. lChange especifica se o controle atual já mudou. |
| Propriedade oCurrentCoolControl | Interna à classe. |
