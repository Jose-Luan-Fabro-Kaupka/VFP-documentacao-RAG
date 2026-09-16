# Foundation Class About Dialog Box

Esta classe é um modelo simples de caixa de diálogo About para aplicações personalizadas. A caixa de diálogo inclui um botão que acessa informações do sistema usando a classe Registry.

| Categoria | Misc Forms |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Dialogs |
| Classe | _aboutbox |
| Classe base | Form |
| Biblioteca de classes | _dialogs.vcx |
| Classe pai | _form |
| Amostra | ...\Samples\Solution\Ffc\dialogs.scx |

# Observações

Para usar, solte a classe em um projeto ou, no menu de atalho Component Gallery Item, selecione Add to Project. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe, criar uma subclasse ou criar um formulário. Se você escolher Create a new form, o Visual FoxPro exibe a caixa de diálogo Open para que você possa especificar o nome do formulário, depois cria e abre o formulário no Form Designer. Especifique valores para os labels e, em seguida, salve e chame o formulário da sua aplicação.

| Propriedades, eventos, métodos | Descrição |
| --- | --- |
| Propriedade cMSINFODir | Especifica o caminho de Msinfo.exe. Padrão: "" |
| Método GetRegisteredCompany | Uma rotina stub para retornar a empresa registrada. Para usar, substitua o valor de lblUserCorp.Caption. |
| Método GetRegisteredOwner | Uma rotina stub para retornar o proprietário registrado. Para usar, substitua o valor de lblUserName.Caption. |
