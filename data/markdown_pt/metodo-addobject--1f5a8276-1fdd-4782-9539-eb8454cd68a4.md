# Método AddObject

Adiciona um objeto a um objeto Container em tempo de execução.

```foxpro
Object.AddObject(cName, cClass [, cOLEClass] [, aInit1, aInit2 ...])
```

#### Parâmetros
**cName**
Especifica o nome usado para fazer referência ao novo objeto.
**cClass**
Especifica a classe do objeto a ser adicionado.
**cOLEClass**
Especifica a classe OLE do objeto a ser adicionado. Observação: se você pretende distribuir aplicativos em tempo de execução que adicionam controles ActiveX que exigem informações de chave de licença (por exemplo, os controles Microsoft Treeview e Listview), não use o método AddObject(.....cOLEClass). Em vez disso, crie e salve uma subclasse do controle ActiveX em uma biblioteca de classes VCX. Em tempo de execução, use AddObject (ou NewObject) para adicionar essa classe OleControl que contém o controle.
**aInit1 , aInit2**
Especificam parâmetros passados ao evento Init do novo objeto.

# Observações

Aplica-se a: Column Object | CommandGroup Control | Container Object | Custom Object | DataEnvironment Object | Form Object | FormSet Object | Grid Control | OptionGroup Control | Page Object | PageFrame Control | _SCREEN System Variable | ToolBar Object

Chamar o método AddObject dispara o evento Init do objeto adicionado. Quando um formulário é adicionado a um conjunto de formulários, o evento Load ocorre antes de Init.

> **Observação:** Quando AddObject é usado para adicionar um objeto a um contêiner, a propriedade Visible do objeto é definida como False (.F.), permitindo configurar suas propriedades sem efeitos visuais inconvenientes enquanto sua aparência é alterada.

Se você usar AddObject( ) para adicionar dinamicamente um controle ActiveX a um formulário, o aplicativo distribuído poderá falhar se esse controle exigir chaves de licença no Registro que não estejam disponíveis na máquina de destino. Muitos fornecedores exigem essas chaves para manipular os controles em tempo de design, como ocorre com AddObject( ). Evite essa exigência criando primeiro uma subclasse do controle ActiveX em uma biblioteca de classes (.vcx) e usando AddObject( ) para adicionar dinamicamente uma instância da subclasse em tempo de execução. Sempre consulte o fornecedor do controle ActiveX que pretende distribuir, pois talvez existam outros arquivos dependentes a incluir.

# Exemplo

O exemplo a seguir demonstra como usar AddObject para adicionar objetos ou controles a um formulário. AddObject adiciona um controle Line e três botões de comando.

A propriedade Visible é definida como True (.T.) para o controle Line e para os botões de comando. Por padrão, objetos e controles adicionados a um formulário não ficam visíveis.

```foxpro
frmMyForm = CREATEOBJECT('Form')  && Create a Form
frmMyForm.Closable = .F.  && Disable the Control menu box
frmMyForm.AddObject('shpLine','Line')  && Add a Line control to the form
frmMyForm.AddObject('cmdCmndBtn1','cmdMyCmndBtn1')  && Up Cmnd button
frmMyForm.AddObject('cmdCmndBtn2','cmdMyCmndBtn2')  && Down Cmnd button
frmMyForm.AddObject('cmdCmndBtn3','cmdMyCmndBtn3')  && Quit Cmnd button
frmMyForm.shpLine.Visible = .T.  && Make Line control visible
frmMyForm.shpLine.Top = 20  && Specify Line control row
frmMyForm.shpLine.Left = 125  && Specify Line control column
frmMyForm.cmdCmndBtn1.Visible =.T.  && Up Command button visible
frmMyForm.cmdCmndBtn2.Visible =.T.  && Down" Command button visible
frmMyForm.cmdCmndBtn3.Visible =.T.  && Quit Command button visible
frmMyForm.SHOW  && Display the form
READ EVENTS  && Start event processing
DEFINE CLASS cmdMyCmndBtn1 AS COMMANDBUTTON  && Create Command button
   Caption = 'Slant \<Up'  && Caption on the Command button
   Left = 50  && Command button column
   Top = 100  && Command button row
   Height = 25  && Command button height

   PROCEDURE Click
      ThisForm.shpLine.Visible = .F.  && Hide the Line control
      ThisForm.shpLine.LineSlant ='/'  && Slant up
      ThisForm.shpLine.Visible = .T.  && Show the Line control
ENDDEFINE
DEFINE CLASS cmdMyCmndBtn2 AS CommandButton  && Create Command button
   Caption = 'Slant \<Down'  && Caption on the Command button
   Left = 200  && Command button column
   Top = 100  && Command button row
   Height = 25  && Command button height
   PROCEDURE Click
      ThisForm.shpLine.Visible = .F.  && Hide the Line control
      ThisForm.shpLine.LineSlant ='\'  && Slant down
      ThisForm.shpLine.Visible = .T.  && Show the Line control
ENDDEFINE
DEFINE CLASS cmdMyCmndBtn3 AS CommandButton  && Create Command button
   Caption = '\<Quit'  && Caption on the Command button
   Cancel = .T.  && Default Cancel Command button (Esc)
   Left = 125  && Command button column
   Top = 150  && Command button row
   Height = 25  && Command button height
   PROCEDURE Click
      CLEAR EVENTS  && Stop event processing, close Form
ENDDEFINE
```
