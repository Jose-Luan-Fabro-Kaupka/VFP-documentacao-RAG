# Classe Foundation ActiveX Calendar

Esta classe usa o controle ActiveX de calendário que pode ser vinculado a um campo de data de um formulário ou outro contêiner.

| Category | Date/Time |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Data/Time |
| Class | _olecalendar |
| Base Class | OLEcontrol |
| Class Library | _datetime.vcx |
| Parent Class | _olecontrol |
| Sample | ...\Samples\Solution\Ffc\datacal.scx |

# Observações

Para usar, arraste a classe para um projeto ou formulário ou, no menu de atalho do item do Component Gallery, selecione Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro abre um builder para que você possa especificar o valor apropriado de Date_column. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

| Properties, Events, Methods | Description |
| --- | --- |
| Date_column property | Especifica um campo do tipo data ao qual vincular o calendário. Padrão: "" |
| RefreshDisplay method | Atualiza a exibição do calendário com o valor na coluna especificada na propriedade Date_column. Sintaxe: RefreshDisplay( ) Retorno: nenhum Argumentos: nenhum |
