# Operador de resolução de escopo ::

Executa um método da classe pai a partir de um método da subclasse.

```foxpro
cClassName::cMethod
```

# Observações

O operador :: é usado para executar um método da classe pai a partir de um método da subclasse. Quando você cria uma subclasse, os métodos da subclasse são herdados automaticamente da classe pai. O operador :: permite executar o método da classe pai no método da subclasse e, em seguida, realizar processamento adicional para o método da subclasse. As definições de subclasse no exemplo demonstram como o operador :: é usado para executar o método da classe pai em um método da subclasse.

Para obter informações adicionais sobre o operador de resolução de escopo ::, consulte Programação orientada a objetos.

# Exemplo

O exemplo a seguir cria um formulário e adiciona dois botões de comando ao formulário. Ao clicar em qualquer um dos botões, você pode sair do formulário — o segundo botão, `cmdAnotherButton`, chama o procedimento Click de `cmdQuit`. Essa ação é possível devido à criação de subclasses. O operador de resolução de escopo chama o código da classe pai para o objeto de subclasse.

```foxpro
frmMyForm = CREATEOBJECT("Form")
frmMyForm.Width  = 450
frmMyForm.Height   = 100
frmMyForm.Caption  = "Scope Resolution Example"
frmMyForm.AutoCenter =.T.
frmMyForm.AddObject("cmdQuit","cmdQuitButton")
frmMyForm.AddObject("cmdAnother","cmdAnotherButton")
frmMyForm.SHOW       && Display the form
READ EVENTS        && Start event processing
```

O exemplo a seguir define dois botões de comando. O primeiro botão será usado para criar uma subclasse para o segundo botão. A criação da subclasse pode ser observada pelas propriedades FontBold e ForeColor, que são definidas para `cmdQuit`, mas nunca explicitamente configuradas para `cmdAnotherButton`. Estamos definindo `cmdAnotherButton` como uma subclasse de `cmdQuitButton`. Como resultado, esse botão receberá todos os atributos definidos acima para `cmdQuitButton`.

```foxpro
DEFINE CLASS cmdQuitButton AS CommandButton
  Caption  = "\<Quit"   && Caption on command button
  Left   = 175    && Left edge of button
  Top    = 60     && Position for top of button
  Height   = 25     && Button height
  Visible  = .T.    && Show button on form
  FontItalic = .T.    && Turn on italic text
  ForeColor  = RGB(0,0,255) && Change button text color
  PROCEDURE Click
  WAIT WINDOW "Executing the CLICK procedure for cmdQuit." TIMEOUT 1
  CLEAR EVENTS     && Stop event processing
ENDDEFINE
DEFINE CLASS cmdAnotherButton AS cmdQuitButton
  Caption = "Click to quit"
  Left  = 175
  Top   = 30
  Height  = 25

  PROCEDURE Click
  WAIT WINDOW "Click event for button: cmdAnotherButton" TIMEOUT 1
  cmdQuitButton::Click
ENDDEFINE
```
