# Classe foundation Data Edit Buttons

Este é um conjunto completo de botões de edição que inclui botões Top, Previous, Next, Bottom, Find, Print, Add Delete, Edit e Save. O Form Wizard usa esta classe.

| Category | Data Editing |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Buttons |
| Class | picbtns |
| Base Class | CommandGroup |
| Class Library | wizbtns.vcx |
| Parent Class | txtbtns |
| Sample | ...\Samples\Solution\Ffc\dataedit.scx |

# Observações

Você pode usar esta classe em formulários simples com uma única tabela ou em formulários de relacionamento 1-para-Muitos usando campos para uma tabela pai e uma grade para a tabela filha.

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho Component Gallery Item, selecione Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro posiciona os botões no formulário. Você pode especificar uma fonte de dados e fornecer objetos de entrada e saída. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse. A classe pai txtbtns contém propriedades adicionais que você pode definir.

| Properties, Events, Methods | Description |
| --- | --- |
| WizBMPpath property | Interno à classe. |
