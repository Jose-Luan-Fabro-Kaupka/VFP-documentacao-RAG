# Foundation Class User Privileges

Esta classe retorna os User Access Rights do usuário atualmente conectado. No Windows 2000, isso seria Guest, Power User ou Administrator. Essas informações são comumente necessárias em aplicações que fornecem conformidade com o Windows 2000 Logo.

| Category | System Utilities |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Class | _userpriv |
| Base Class | Custom |
| Class Library | _system.vcx |
| Parent Class | _custom |
| Sample | ...\Samples\Solution\Ffc\Logo.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do item da Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca o ícone da classe no formulário. Você pode especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de foundation classes.

| Properties, Events, Methods | Description |
| --- | --- |
| GetUserPriv method | Returns path to specified system folder. Syntax: GetUserPriv(cUser) Return: access of user Arguments: cUser specifies name of user to check. |
