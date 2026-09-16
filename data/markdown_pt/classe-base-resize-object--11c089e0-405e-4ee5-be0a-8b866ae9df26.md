# Classe base Resize Object

Esta classe faz com que objetos soltos em um formulário sejam redimensionados e movidos com o evento Resize do formulário.

| Categoria | Interface do usuário |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\User Controls |
| Classe | _resizable |
| Classe base | Custom |
| Biblioteca de classes | _controls.vcx |
| Classe pai | _custom |
| Exemplo | ...\Samples\Solution\Forms\cresize.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item do Component Gallery, selecione Add to Project ou Add to Form. Ao adicionar a classe a um formulário, especifique o método AdjustControls no evento Resize dos controles do formulário. Ao soltar a classe em um projeto, você pode escolher entre adicionar a classe ou criar uma subclasse.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade InitialResize | Especifica se os controles já foram ajustados. Padrão: .T. |
| Método AdjustControls | Ajusta o posicionamento e o tamanho dos objetos contidos após um evento Resize. Sintaxe: AdjustControls( ) Retorno: nenhum Argumentos: nenhum |
| Método Reset | Redefine o controle Timer para que ele comece a contar a partir de 0. Sintaxe: Reset( ) Retorno: nenhum Argumentos: nenhum |
| Propriedade InitialFormHeight | Interna à classe. |
| Propriedade InitialFormWidth | Interna à classe. |
| Propriedade aControlStats[1,5] | Interna à classe. |
| Método AddToArray | Interno à classe. |
| Método SetSize | Interno à classe. |
| Método LoopThroughControls | Interno à classe. |
