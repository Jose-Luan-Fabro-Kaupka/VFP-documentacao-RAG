# Função GETDIR( )

Exibe a caixa de diálogo Select Directory da qual você pode escolher um diretório.

```foxpro
GETDIR([cDirectory [, cText [, cCaption [, nFlags [, lRootOnly]]]]])
```

#### Parâmetros
 **cDirectory**
Especifica o diretório exibido inicialmente na caixa de diálogo. Quando cDirectory não é especificado, a caixa de diálogo abre com o diretório padrão do Visual FoxPro exibido.
**cText**
Especifica o texto para a lista de diretórios na caixa de diálogo.
**cCaption**
Especifica a legenda a ser exibida na barra de título da caixa de diálogo. O padrão do Windows é "Select Directory".
**nFlags**
Especifica as opções para a caixa de diálogo. nFlags pode incluir zero ou uma combinação aditiva dos valores. A tabela a seguir inclui algumas das flags mais comuns. Para obter mais informações, consulte SHBrowseForFolder no MSDN. nFlag Value Description 1 BIF_RETURNONLYFSDIRS Return only file system directories (physical locations). If a user selects folders that are not part of the file system, the OK button is grayed. 2 BIF_DONTGOBELOWDOMAIN Do not include network folders below the domain level in the tree view control (For example, My Computer and My Networks). 8 BIF_RETURNFSANCESTORS Return only file system ancestors. If a user selects anything other than a file system ancestor, the OK button is grayed. 16 BIF_EDITBOX The browse dialog includes an edit control in which the user can type the name of an item. Available on Windows 98 and above, or with Internet Explorer 4.0 or higher (assuming shell integration option selected). Requires version 4.71 of shell32.dll. 32 BIF_VALIDATE Validates the editbox contents. If the editbox is used, it is necessary to validate the user-specified content. If the user types an invalid name into the edit box, the Cancel button becomes the only selection available. This flag is ignored if BIF_EDITBOX is not specified. 64 BIF_NEWDIALOGSTYLE Use the new user-interface. Setting this flag provides the user with a larger, resizable dialog box. Additional functionality includes: drag and drop capability within the dialog box, reordering, context menus, new folders, delete, and other context menu commands. Support in Windows 2000 and above. Requires version 5.00 of shell32.dll. 16384 BIF_BROWSEINCLUDEFILES The browse dialog will display files as well as folders. Available on Windows 98 and above, or with Internet Explorer 4.0 or higher (assuming shell integration option selected). Requires version 4.71 of shell32.dll.
**lRootOnly**
Especifica que apenas cDirectory e suas subpastas são exibidos. Este parâmetro impede a navegação acima da pasta raiz. Se você não especificar cDirectory , o diretório padrão (valor SET DEFAULT) é usado.

# Valor de retorno

Character

# Observações

GETDIR( ) retorna como uma cadeia de caracteres o nome do diretório que você escolhe.

Se você não escolher um diretório (clicar em Cancel, pressionar ESC ou escolher Close no menu da janela), GETDIR( ) retorna a cadeia vazia.

A partir do Visual FoxPro 7, GETDIR( ) suporta duas caixas de diálogo diferentes. Se você fornecer menos de três parâmetros, GETDIR( ) retorna a caixa de diálogo das versões anteriores. Se você fornecer mais de dois parâmetros, o Visual FoxPro usa a rotina SHBrowseForFolder da API Win32 para fornecer a caixa de diálogo.
