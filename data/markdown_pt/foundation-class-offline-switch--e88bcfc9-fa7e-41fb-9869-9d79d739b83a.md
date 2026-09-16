# Foundation Class Offline Switch

O switch Offline funciona em um banco de dados que contém views remotas. Esta classe fornece um conjunto de botões que alternam entre o uso de dados online e offline.

| Category | Data Editing |
| --- | --- |
| Default Catalog | Visual FoxPro Catalog\Foundation Classes\Data Query |
| Class | _offline |
| Base Class | Container |
| Class Library | _dataquery.vcx |
| Parent Class | container |

# Observações

Para usar, solte a classe em um projeto ou formulário em um data environment ou, no menu de atalho do item da Component Gallery, selecione Add to Project ou Add to Form. Quando você adiciona a classe a um formulário, o Visual FoxPro coloca os botões da classe no formulário e abre um builder para que você possa especificar os valores lUseCurrentDBC, lAllViews, lUpdateViews e lRevertOnFail. Quando você solta a classe em um projeto, pode escolher entre adicionar a classe ou criar uma subclasse.

Consulte Guidelines for Using Visual FoxPro Foundation Classes para obter mais informações sobre o uso de foundation classes.

| Properties, Events, Methods | Description |
| --- | --- |
| cDatabase property | Specifies the name of the database containing views to take offline. Default: .F. |
| cViews[1,0] property | Specifies the array of views to process. Default: .F. |
| lAllViews property | Specifies whether to automatically use all views in the database. Default: .F. |
| lRevertOnFail property | Specifies whether to revert all views if one fails when going offline. Default: .T. |
| lUpdateViews property | Specifies whether to update all views when going online. Default: .T. |
| lUseCurrentDBC property | Specifies whether to use the currently opened database at the start. Default: .T. |
| GoOffLine method | Takes the views specified in the cViews array offline. Syntax: GoOffline( ) Return: none Arguments: none |
| GoOnLine method | Takes the views specified in the cViews array online. Syntax: GoOnline( ) Return: none Arguments: none |
| CheckOffLine method | Checks to see if views are currently online/offline. Syntax: CheckOffline( ) Return: none Arguments: none |
| Alert method | Displays a message box containing cMessage . Syntax: Alert(cMessage) Return: m.cMessage Arguments: cMessage specifies the text of the alert message. |
