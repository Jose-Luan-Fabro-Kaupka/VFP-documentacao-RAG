# Matrizes de objetos e membros

Você pode criar matrizes contendo objetos e como membros de classes.

# Matrizes de objetos

Você pode criar matrizes que contêm objetos. Ao criar matrizes que contêm objetos, tenha em mente as seguintes considerações:
 - Você não pode atribuir um objeto individual a todos os elementos em uma matriz usando um único comando. Você deve atribuir o objeto a cada elemento da matriz individualmente.
- Você não pode atribuir um valor à propriedade de uma matriz inteira. Por exemplo, o comando a seguir resulta em um erro: MyArray.Enabled = .F.
- Quando você redimensiona uma matriz de objetos para que seja maior que a matriz original, os novos elementos são inicializados como False (.F.), como é o caso com todas as matrizes no Visual FoxPro. Quando você redimensiona uma matriz de objetos para que seja menor que a matriz original, os objetos com um subscrito maior que o maior novo subscrito são liberados.

Por exemplo, o código a seguir cria uma matriz chamada `MyArray` que contém cinco botões de comando usando uma estrutura de loop:

```foxpro
DIMENSION MyArray[5]
FOR x = 1 TO 5
   MyArray[x] = CREATEOBJECT("CommandButton")
ENDFOR
```

# Matrizes de membros de classe

Você pode incluir matrizes como membros de classes e armazenar objetos nelas.

O exemplo a seguir cria um formulário que contém um objeto criado a partir da classe Container customizada, ButtonList. A classe ButtonList contém um membro que é uma matriz chamada `aChoices`, em que cada elemento contém um objeto de controle diferente.

Quando você executa o exemplo a partir de um arquivo de programa (.prg), um formulário aparece com dois botões de comando e uma caixa de seleção. Quando o usuário clica em um botão de comando ou seleciona a caixa de seleção no formulário, o Visual FoxPro passa o número de índice do elemento da matriz que contém o controle para o evento Click através do parâmetro `tnIndex`. Uma estrutura de comando DO CASE exibe uma janela com o número do elemento.

código diferente dependendo de qual botão foi clicado.

```foxpro
loForm = CREATEOBJECT("Form")
loForm.AddObject("cntButtons", "ButtonList")
loForm.cntButtons.SetAll("Visible", .T.)
loForm.cntButtons.Visible = .T.
loForm.Show(1)
DEFINE CLASS ButtonList AS Container
   Height = 100
   Width = 130
   BorderWidth = 0

   DIMENSION aChoices[3]

   ADD OBJECT aChoices[1] AS CommandButton WITH ;
      Top = 10, ;
      Height = 20, ;
      Left = 10, ;
      Caption = "Element One"
   ADD OBJECT aChoices[2] AS CommandButton WITH ;
      Top = 40, ;
      Left = 10, ;
      Height = 20, ;
      Caption = "Element Two"
   ADD OBJECT aChoices[3] AS CheckBox WITH ;
      Top = 70, ;
      Left = 10, ;
      Caption = "Element Three"

   PROCEDURE aChoices.Click
      LPARAMETER tnIndex
      DO CASE
         CASE tnIndex = 1
            WAIT WINDOW "1"
         CASE tnIndex = 2
            WAIT WINDOW "2"
         CASE tnIndex = 3
            WAIT WINDOW "3"
      ENDCASE
   ENDPROC
ENDDEFINE
```
