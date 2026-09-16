# Classe base SetAllX Extension Foundation Class

A classe SetAllX é uma extensão do método SetAll( ) do Visual FoxPro disponível em muitas classes Visual FoxPro. Diferentemente do método SetAll( ) do Visual FoxPro, você pode especificar uma baseclass cujos objetos são afetados.

| Category | Object Extension |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Class | _setallx |
| Base Class | Custom |
| Class Library | _setallx.vcx |
| Parent Class | _custom |
| Sample | ...\Samples\Solution\Ffc\Setallx.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca o ícone da classe no formulário. Você pode especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de classes base.

| Properties, Events, Methods | Description |
| --- | --- |
| Setallx method | Versão estendida do método SetAll( ). Sintaxe: SetAllX(toParent, tcProperty, tcExpr, tcBaseClassList, tlNoContainerMode, tlErrorWait) Retorno: logical Argumentos: toParent fornece uma referência ao objeto pai . tcProperty especifica a propriedade a ser definida. tcExpr especifica o valor da propriedade sendo definida. tcBaseClassList especifica a baseclass que aplica as alterações. tlNoContainerMode impede a iteração pelo contêiner. tlErrorWait especifica se aguardar erro. |
