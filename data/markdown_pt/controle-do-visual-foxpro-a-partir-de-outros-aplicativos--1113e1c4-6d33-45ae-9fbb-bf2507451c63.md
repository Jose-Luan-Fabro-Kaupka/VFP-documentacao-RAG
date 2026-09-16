# Controle do Visual FoxPro a partir de outros aplicativos

Como o Visual FoxPro atua tanto como servidor (com conformidade de nível 2) quanto como cliente, aplicativos compatíveis com Automação podem criar instâncias do Visual FoxPro, executar comandos do Visual FoxPro e acessar objetos do Visual FoxPro.

Você controla o Visual FoxPro a partir de outros aplicativos usando o objeto Application do Visual FoxPro. Um objeto Application é criado automaticamente sempre que o Visual FoxPro é iniciado, diretamente, por DDE ou por Automação.

Por exemplo, as linhas de código a seguir em Visual Basic® ou em um módulo do Microsoft Excel criam uma referência a um objeto Application do Visual FoxPro:

```foxpro
Dim oFox as Object
Set oFox = CreateObject("VisualFoxPro.Application")
```

Depois de obter uma referência ao objeto Application do Visual FoxPro, você pode chamar métodos associados a ele e acessar outros objetos por meio das propriedades de coleção do objeto Application.
 Métodos do objeto Application
| DataToClip | Help |
| --- | --- |
| DoCmd | Quit |
| Eval | RequestData |

O exemplo a seguir usa código do Visual Basic for Applications em um módulo do Excel para criar um objeto Application do Visual FoxPro, abrir uma tabela do Visual FoxPro e adicionar os resultados de uma consulta à planilha ativa:

```foxpro
Sub FoxTest()
Dim oFox as Object
Set oFox = CreateObject("VisualFoxPro.Application")
oFox.DoCmd "USE customer"
oFox.DoCmd "SELECT contact, phone FROM customer
   WHERE country = " + Chr$(39) + USA+ Chr$(39) + " INTO CURSOR cust"
oFox.DataToClip "cust",,3
Range("A1:B1").Select
ActiveSheet.Paste
End Sub
```

# O modelo de objetos Application do Visual FoxPro

Um objeto Application é criado automaticamente sempre que o Visual FoxPro é iniciado, diretamente, por Automação ou DDE. Esse objeto fornece acesso a todos os demais objetos criados em uma sessão do Visual FoxPro por meio de propriedades Collection.
 Modelo de objetos Application do Visual FoxPro

# Acesso a objetos por meio de propriedades de coleção

O objeto Application do Visual FoxPro e todos os objetos contêineres do Visual FoxPro têm uma propriedade de contagem e uma propriedade de coleção associadas. A propriedade de coleção é uma matriz que referencia cada objeto contido. A propriedade de contagem é numérica e indica o número de objetos contidos.

A tabela a seguir lista os objetos e suas propriedades correspondentes de coleção e contagem.

| Objeto | Propriedade de coleção | Propriedade de contagem |
| --- | --- | --- |
| Application | Objects Forms | Count FormCount |
| FormSet | Forms | FormCount |
| Form | Objects Controls | Count ControlCount |
| PageFrame | Pages | PageCount |
| Page | Controls | ControlCount |
| Grid | Columns | ColumnCount |
| CommandGroup | Buttons | ButtonCount |
| OptionGroup | Buttons | ButtonCount |
| Column | Controls | ControlCount |
| ToolBar | Controls | ControlCount |
| Container | Controls | ControlCount |
| Control | Controls | ControlCount |

Essas propriedades permitem usar um loop de programa para gerenciar todos os objetos contidos ou alguns deles. Por exemplo, as linhas de código a seguir definem a propriedade Visible de todos os formulários como True (.T.):

```foxpro
FOR EACH Form IN Application.Forms
   Form.Visible = .T.
ENDFOR
```
