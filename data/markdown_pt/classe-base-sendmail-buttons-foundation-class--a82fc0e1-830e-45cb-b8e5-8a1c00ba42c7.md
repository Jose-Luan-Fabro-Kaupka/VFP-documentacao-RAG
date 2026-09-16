# Classe base SendMail Buttons Foundation Class

Esta classe, que usa o controle ActiveX MAPI, trata do envio de uma mensagem de correio a partir de um formulário. Quando solta em um formulário, pode ser usada para enviar o registro atual diretamente para seu aplicativo de correio.

| Categoria | Misc Buttons |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Buttons |
| Classe | _mailbtn |
| Classe base | Container |
| Biblioteca de classes | _miscbtns.vcx |
| Classe pai | _container |
| Amostra | ...\Samples\Solution\OLE\sendmail.scx |

# Observações

Para usar, solte a classe em um projeto ou formulário ou, no menu de atalho do Component Gallery Item, selecione Add to Project ou Add to Form. Quando você solta a classe em um formulário em um data environment, o Visual FoxPro coloca um botão no seu formulário onde ele acessará o registro atual do formulário ativo. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Properties, Events, Methods | Descrição |
| --- | --- |
| propriedade logSession | Especifica se o logon no correio foi bem-sucedido. Padrão: .F. |
| método SignOn | Tenta fazer logon no correio. Sintaxe: SignOn( ) Retorno: none Argumentos: none |
| método AddTabs | Interno à classe. |
