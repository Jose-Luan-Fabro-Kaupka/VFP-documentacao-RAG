# Classe Foundation Common System Folders

Esta classe fornece a localização de janelas comuns do sistema, como a pasta Meus Documentos e a pasta Application Data. Elas são comumente necessárias em aplicativos que oferecem conformidade com o Windows 2000 Logo. Consulte SHGetFolderPath na MSDN para obter mais detalhes.

| Category | System Utilities |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Utilities |
| Class | _commonfolder |
| Base Class | Custom |
| Class Library | _system.vcx |
| Parent Class | _custom |
| Sample | ...\Samples\Solution\Ffc\Logo.scx |

# Observações

Para usar, arraste a classe para um projeto ou formulário ou, no menu de atalho do item do Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca o ícone da classe no formulário. Você pode especificar os valores de propriedade apropriados e fornecer quaisquer objetos de entrada e saída necessários. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Properties, Events, Methods | Description |
| --- | --- |
| GetFolder method | Retorna o caminho para a pasta do sistema especificada. Sintaxe: GetFolder(nFolderID, lCreateNew) Retorno: nome da pasta Argumentos: nFolderID referência de ID da pasta. Consulte o método da classe para IDs comuns conforme especificado em SHGetFolderPath na MSDN. lCreateNew especifica se deve criar a pasta quando ela não existir |
