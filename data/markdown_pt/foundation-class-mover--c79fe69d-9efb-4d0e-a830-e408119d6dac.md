# Foundation Class Mover

Quando colocada em um projeto ou formulário, esta classe fornece uma classe simples de caixa de listagem mover com botões Move e Remove.

| Categoria | Movers |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\User Controls |
| Classe | _mover |
| Classe base | Container |
| Biblioteca de classes | _mover.vcx |
| Classe pai | _container |
| Exemplo | ...\Samples\Solution\Ffc\movers.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Galeria de Componentes, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca os controles de caixa de listagem da classe e os botões de movimentação no formulário. Em seguida, você pode especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de foundation classes.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| propriedade aChoices[1,0] | O array de opções disponíveis na caixa de listagem esquerda. Padrão: .F. |
| propriedade aSelections[1,0] | O array de itens selecionados na caixa de listagem direita. Padrão: .F. |
| propriedade UseArrays | Especifica se deve usar arrays para as caixas de listagem. Padrão: .T. |
| método InitChoices | Inicializa o array de opções. Sintaxe: InitChoices(@aChoices) Retorno: nenhum Argumentos: aChoices especifica um array de opções iniciais. |
| método InitSelections | Inicializa o array de seleções. Sintaxe: InitSelections(@aSelections) Retorno: nenhum Argumentos: aSelections especifica o array de seleções iniciais. |
| método GetSelections | Recupera os itens selecionados. Sintaxe: GetSelections(@aSelections) Retorno: nenhum Argumentos: aSelections especifica o nome do array contendo as seleções de destino. |
| método PopList | A rotina para preencher as caixas de listagem. Sintaxe: PopList(@aListArray, oLstRef) Retorno: nenhum Argumentos: aListArray especifica os itens com os quais preencher a lista. oLstRef é uma referência ao objeto de controle. |
| propriedade OldlSelectedItem | Interno à classe. |
| propriedade OldrSelectedItem | Interno à classe. |
| propriedade SortLeft | Interno à classe. |
| propriedade Updated | Interno à classe. |
| método SizeToContainer | Interno à classe. |
| método ValidItem | Interno à classe. |
