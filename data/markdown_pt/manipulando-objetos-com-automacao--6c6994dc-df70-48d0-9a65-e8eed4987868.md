# Manipulando objetos com automação

Objetos OLE em seus formulários ou programas, ou controles ActiveX dentro de controles OLE Container, podem ser manipulados por meio de código da mesma forma que você programa objetos nativos do Visual FoxPro.

# Manipulando propriedades de objetos extrínsecos

No código, você pode manipular um objeto usando suas propriedades. A forma de referenciar uma propriedade depende se o objeto está isolado ou faz parte de um contêiner, como o controle OLE Container ou o controle OLE Bound.

> **Observação:** Controles ActiveX sempre fazem parte de um controle OLE Container.

Um objeto em um contêiner tem duas partes: o objeto em si e um contêiner ao redor do objeto. Tanto o objeto quanto o contêiner possuem propriedades e, às vezes, elas têm os mesmos nomes. Para garantir que você referencie as propriedades do objeto, sempre acrescente a propriedade Object do contêiner ao nome do objeto. Por exemplo, o código a seguir refere-se à propriedade Left do objeto:

```foxpro
frm1.olecontrol1.Object.Left = 25  && Object's Left
```

Se você omitir a propriedade Object, você referencia a propriedade Left do contêiner:

```foxpro
frm1.olecontrol1.Left= 25  && Container's Left property
```

Por exemplo, suponha que você tenha uma aplicação que envia e-mail quando o usuário clica em um botão de comando de composição. Se você adicionou um controle de mensagem Microsoft MAPI a um formulário como `olecontrol1`, o código associado ao evento Click do botão de comando pode ser:

```foxpro
THISFORM.olecontrol1.Object.Compose
THISFORM.olecontrol1.Object.Send(.T.)
```

Além de usar a propriedade Object para referenciar propriedades do objeto contido, você pode usar outras propriedades do controle contêiner. Por exemplo, você pode referenciar a propriedade somente leitura OLEClass para identificar o tipo de objeto no contêiner e a propriedade Sizable para impedir que os usuários alterem o tamanho de um objeto. Para detalhes sobre propriedades de controle contêiner, consulte OLE Container Control.

No Form and Class Designers, as propriedades de controles ActiveX são exibidas na janela Properties do Visual FoxPro, mas a maioria dos controles ActiveX também possui sua própria interface para definir propriedades comuns. Você pode ver essa interface de propriedades selecionando a opção Properties específica do objeto no menu de atalho do controle ActiveX. Por exemplo, para abrir a caixa de diálogo Properties de um controle rich text, escolha Microsoft RichText Control Properties no menu de atalho.

# Usando métodos de objetos extrínsecos

Além de definir e recuperar propriedades de objetos, você pode manipular um objeto usando os métodos que ele suporta. Por exemplo, você pode usar o método Add de um objeto de coleção Microsoft Excel para criar um novo workbook do Microsoft Excel.

O exemplo de automação a seguir usa o método Add para criar um workbook do Excel, o método Save para salvar o workbook e o método Quit para encerrar o Excel:

| Código | Comentários |
| --- | --- |
| oleApp = CREATEOBJECT("Excel.Application") | Inicia o Excel. |
| OleApp.Visible=.T. | Exibe o Excel. |
| OleApp.Workbooks.Add | Cria um workbook. |
| OleApp.Cells(1,1).Value=7 | Define o valor de uma célula. |
| OleApp.ActiveWorkbook.SaveAs("C:\TEMP.XLS") | Salva o workbook. |
| OleApp.Quit | Encerra o Excel. |

Se você criar um objeto usando o controle OLE Container ou OLE Bound, pode usar o método DoVerb do controle para executar um verbo no objeto. Por exemplo, use DoVerb(0) para executar o verbo padrão, DoVerb(– 1) para ativar o objeto para edição visual e DoVerb(– 2) para abrir o objeto em uma janela separada.

> **Observação:** Consulte a documentação de uma aplicação para determinar quais comandos de automação ela suporta. Por exemplo, componentes de suplemento do Microsoft Excel não estão disponíveis para automação.

# Definindo tempos limite

Quando você envia uma solicitação a um objeto OLE, o servidor de automação a processa. Você não tem muito controle sobre o processamento do servidor, mas pode especificar por quanto tempo aguardará que um processo termine definindo as propriedades OLERequestPendingTimeout e OLEServerBusyTimeout. Você pode determinar o que acontece quando esse tempo expira definindo a propriedade OLEServerBusyRaiseError.

# Acessando coleções de objetos

Um tipo de objeto pode representar um único objeto ou uma coleção de objetos relacionados. Por exemplo, um objeto Microsoft Excel Workbook representa um único workbook, enquanto o objeto Workbooks representa todos os workbooks carregados no momento. Como o objeto Workbooks representa uma coleção de objetos, ele é chamado de objeto de coleção.

No código, uma coleção é uma lista não ordenada na qual a posição de um objeto pode mudar sempre que objetos são adicionados ou removidos da coleção. Você acessa um objeto em uma coleção iterando pela coleção, usando a propriedade Count da coleção. A propriedade Count retorna o número de itens na coleção. Você também pode usar o método Item para retornar um item em uma coleção.

Por exemplo, para exibir os nomes das planilhas em um workbook do Microsoft Excel, use o código a seguir:

```foxpro
oleApp = CREATEOBJECT("Excel.Application")
oleApp.Workbooks.Add
FOR EACH x IN oleApp.Workbooks
 ? x.Name
ENDFOR
```

Você também pode acessar uma coleção dentro de uma coleção. Por exemplo, você pode acessar uma coleção de células dentro de um intervalo usando o código a seguir:

```foxpro
oleApp = CREATEOBJECT("Excel.sheet")
oleApp.Workbooks.Add
oleApp.Range(oleApp.Cells(1,1),oleApp.Cells(10,10)).Value=100
oleApp.Visible=.T.
```

# Usando matrizes de objetos

Você pode passar matrizes para métodos e receber matrizes de volta. No entanto, você deve passar matrizes por referência prefixando o nome da matriz com o sinal @.

Por exemplo, para enviar uma matriz do Visual FoxPro ao Microsoft Excel, considere o código a seguir. Ele cria uma matriz no Visual FoxPro, atribui alguns valores à matriz, inicia o Microsoft Excel, cria um workbook, define um valor na primeira célula de uma planilha e depois copia esse valor para as outras planilhas na matriz:

```foxpro
DIMENSION aV(3)
aV(1) = "Sheet1"
aV(2) = "Sheet2"
aV(3) = "Sheet3"
oleApp=CREATEOBJECT("Excel.Application")
oleApp.Workbooks.Add
oleI=oleApp.Workbooks.Item(1)
oleI.Sheets.Item(1).Cells(1,1).Value = 83
oleI.Sheets(@aV).;
 FillAcrossSheets(oleI.Worksheets("Sheet1").Cells(1,1))
oleApp.Visible = .T.
```

Alternativamente, o exemplo a seguir retorna uma matriz ao Visual FoxPro e depois exibe o conteúdo da matriz:

```foxpro
oleApp = CREATEOBJECT("Excel.Application")
aOleArray = oleApp.GetCustomListContents(3)
FOR nIndex = 1 to ALEN(aOleArray)
   ? aOleArray(nIndex)
ENDFOR
```

> **Observação:** Com o Visual FoxPro, você não pode passar matrizes maiores que duas dimensões para objetos OLE. Para obter mais informações sobre o trabalho com matrizes no Visual FoxPro, consulte Arrays and Object and Member Arrays .

# Liberando objetos extrínsecos

Um servidor de automação é liberado automaticamente se não estiver visível e nenhuma variável em escopo referenciar o objeto. Você pode usar o comando RELEASE para liberar a variável associada a um objeto. Se o servidor estiver visível, use o método Quit para liberá-lo.
