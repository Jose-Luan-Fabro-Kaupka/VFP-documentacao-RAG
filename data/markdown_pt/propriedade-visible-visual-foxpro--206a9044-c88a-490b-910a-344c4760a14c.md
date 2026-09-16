# Propriedade Visible (Visual FoxPro)

Especifica se um objeto está visível ou oculto. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Object.Visible [= lExpr]
```

# Valor de retorno
 **lExpr**
Especifica um valor que determina se o objeto fica visível ou oculto. True (.T.): o objeto fica visível (padrão no Designer de Formulários). False (.F.): o objeto fica oculto (padrão no código de programa). Observação: mesmo oculto, o objeto continua acessível no código. Dica: para ocultar um objeto na inicialização, defina Visible como False (.F.) em tempo de design. Ao definir Visible no código, você pode ocultar e exibir o objeto em tempo de execução em resposta a um evento.

# Observações

Aplica-se a: CheckBox Control | Column Object | ComboBox Control | CommandButton Control | CommandGroup Control | Container Object | Control Object (Visual FoxPro) | EditBox Control | Form Object | FormSet Object | Grid Control | Image Control (Visual FoxPro) | Label Control (Visual FoxPro) | Line Control | ListBox Control | OLE Bound Control | OLE Container Control | OptionButton Control | OptionGroup Control | PageFrame Control | Project Object (Visual FoxPro) | _SCREEN System Variable | Separator Object | Shape Control | Spinner Control | TextBox Control (Visual FoxPro) | ToolBar Object

Para objetos Form, quando Visible é definido como False (.F.), o formulário é ocultado e o conjunto de formulários, formulário ou outro objeto ativo mais recente torna-se ativo. Quando Visible é True (.T.), o formulário fica visível, mas não se torna ativo. Para torná-lo visível e ativo na mesma etapa, use o método Show. Consulte Método Show (Visual FoxPro).

> **Observação:** Um formulário de um objeto FormSet não é exibido quando sua propriedade Visible é False (.F.), mesmo que Visible do conjunto seja True (.T.). Contudo, todos os formulários do conjunto são ocultados se Visible do conjunto for False (.F.).

Definir Visible de um formulário como True (.T.) não afeta a configuração da propriedade Order.

Para objetos Separator, Visible determina se um espaço aparece como separador quando Style é 0 (Normal — não exibir linha). Quando Visible é True (.T.) e Style é 0, aparece um espaço em vez do separador. Quando Visible é False (.F.), não aparece espaço, independentemente de Style.

Em versões anteriores ao Visual FoxPro 5.0, definir Visible para a variável de sistema _SCREEN não produz efeito.

# Exemplo

O exemplo exibe um formulário com um controle Line e três botões de comando baseados em classes CommandButton personalizadas. Os botões "Slope Up" e "Slope Down" alteram a inclinação da linha, e Quit encerra o programa. Visible oculta e exibe os controles nos momentos apropriados.

As linhas a seguir criam um formulário e desabilitam o botão Fechar para que o botão Quit personalizado encerre o programa.

```foxpro
frmMyForm = CREATEOBJECT('Form')
frmMyForm.Closable = .F.
```

As linhas a seguir usam AddObject para adicionar um controle Line e três botões de comando personalizados ao formulário.

```foxpro
frmMyForm.AddObject('shpLine','Line')
frmMyForm.AddObject('cmdCmndBtn1','cmdMyCmndBtn1')
frmMyForm.AddObject('cmdCmndBtn2','cmdMyCmndBtn2')
frmMyForm.AddObject('cmdCmndBtn3','cmdMyCmndBtn3')
```

Visible é definida como True (.T.) para exibir o controle de linha e os botões. Top e Left especificam a distância entre o controle e o formulário.

```foxpro
frmMyForm.shpLine.Visible = .T.
frmMyForm.cmdCmndBtn1.Visible =.T.
frmMyForm.cmdCmndBtn2.Visible =.T.
frmMyForm.cmdCmndBtn3.Visible =.T.
frmMyForm.shpLine.Top = 20
frmMyForm.shpLine.Left = 125
```

O método Show exibe o formulário, e READ EVENTS inicia o processamento de eventos.

```foxpro
frmMyForm.SHOW
READ EVENTS
```

DEFINE CLASS define três classes CommandButton personalizadas e contém configurações para as propriedades apropriadas. No evento Click, Visible oculta o controle de linha para permitir alterar sua inclinação e volta a exibi-lo depois. CLEAR EVENTS no evento Click do terceiro botão interrompe o processamento de eventos e fecha o formulário.

```foxpro
DEFINE CLASS cmdMyCmndBtn1 AS COMMANDBUTTON
   Caption = 'Slope \<Up'
   Left = 50
   Top = 100
   Height = 25
   PROCEDURE Click
      ThisForm.shpLine.Visible = .F.
      ThisForm.shpLine.LineSlant ='/'
      ThisForm.shpLine.Visible = .T.
ENDDEFINE
DEFINE CLASS cmdMyCmndBtn2 AS CommandButton
   Caption = 'Slope \<Down'
   Left = 200
   Top = 100
   Height = 25
   PROCEDURE Click
      ThisForm.shpLine.Visible = .F.
      ThisForm.shpLine.LineSlant ='\'
      ThisForm.shpLine.Visible = .T.
ENDDEFINE
DEFINE CLASS cmdMyCmndBtn3 AS CommandButton
   Caption = '\<Quit'
   Cancel = .T.
   Left = 125
   Top = 150
   Height = 25
   PROCEDURE Click
      CLEAR EVENTS
ENDDEFINE
```
