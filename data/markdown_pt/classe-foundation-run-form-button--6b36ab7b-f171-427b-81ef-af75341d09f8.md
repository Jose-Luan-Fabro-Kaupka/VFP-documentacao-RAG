# Classe Foundation Run Form Button

Esta classe fornece um botão genérico para executar um formulário.

| Categoria | Misc Buttons |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Buttons |
| Classe | _cmdRunForm |
| Classe base | CommandButton |
| Biblioteca de classes | _miscbtns.vcx |
| Classe pai | _commandbutton |
| Exemplo | ...\Samples\Solution\Ffc\buttons.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um builder para que você possa especificar cFileName, o nome do formulário que deseja executar. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cFilename | Especifica o nome do formulário a ser executado. Padrão: "" |
| Propriedade lSetCaption | Especifica se o caption é definido automaticamente com base no valor de cFilename. Padrão: .T. |
