# Como: definir propriedades em tempo de execução

O modelo de objetos no Visual FoxPro permite controlar propriedades de formulário em tempo de execução.

# Referenciando objetos na hierarquia de objetos

Para manipular um objeto em código, você precisa identificá-lo em relação à hierarquia de contêineres. No nível mais alto da hierarquia de contêineres, ou seja, o formulário ou conjunto de formulários, você precisa referenciar a variável de objeto. A menos que você use a cláusula NAME do DO FORM Command, a variável de objeto tem o mesmo nome do arquivo de formulário (.scx).

### Para manipular propriedades
- Em código, referencie a variável de objeto, o controle e então a propriedade com o operador ponto ( . ) como separador, usando o seguinte formato: ObjectVariable .[ Form .] Control . Property = Setting

A tabela a seguir lista propriedades ou palavras-chave que facilitam referenciar um objeto na hierarquia de objetos.

| Property or keyword | References |
| --- | --- |
| ActiveControl | O controle no formulário ativo no momento que tem o foco. |
| ActiveForm | O formulário ativo no momento. |
| ActivePage | A página ativa no formulário ativo no momento. |
| Parent | O contêiner imediato do objeto |
| THIS | O objeto ou um procedimento ou evento do objeto. |
| THISFORM | O formulário que contém o objeto. |
| THISFORMSET | O conjunto de formulários que contém o objeto. |

Por exemplo, para alterar a legenda de um botão de comando no formulário `frmCust` em um conjunto de formulários armazenado em Custview.scx, use o seguinte comando em um programa ou na janela Command:

```foxpro
CustView.frmCust.cmdButton1.Caption = "Edit"
```

Use as palavras-chave THIS, THISFORM e THISFORMSET para referenciar objetos a partir de um formulário. Por exemplo, para alterar a Caption de um botão de comando quando o botão de comando é clicado, inclua o seguinte comando no código do evento Click do botão de comando:

```foxpro
THIS.Caption = "Edit"
```

A tabela a seguir apresenta exemplos de uso de THISFORMSET, THISFORM, THIS e Parent para definir propriedades de objetos:

| Command | Where to include the command |
| --- | --- |
| THISFORMSET.frm1.cmd1.Caption = 'OK' | No código de evento ou método de qualquer controle em qualquer formulário do conjunto de formulários, exceto frm1 . |
| THISFORM.cmd1.Caption = 'OK' | No código de evento ou método de qualquer controle, exceto cmd1, no mesmo formulário em que cmd1 está. |
| THIS.Caption = 'OK' | No código de evento ou método do controle cuja legenda você deseja alterar. |
| THIS.Parent.BackColor = RGB(192,0,0) | No código de evento ou método de um controle em um formulário. O comando altera a cor de fundo do formulário para vermelho escuro. |

# Definindo propriedades em tempo de execução com expressões

Você também pode definir propriedades em tempo de execução usando expressões ou funções.

### Para definir propriedades como expressões em tempo de execução
- Atribua uma expressão à propriedade. -ou-
- Atribua o resultado de uma função definida pelo usuário à propriedade. Por exemplo, você poderia definir a legenda de um botão como Edit ou Save, dependendo do valor de uma variável. Declare a variável no programa que chama seu formulário: PUBLIC glEditing glEditing = .F. Então use uma expressão IIF na configuração Caption: frsSet1.frmForm1.cmdButton1.Caption = ; IIF(glEditing = .F., "Edit", "Save")

Você poderia determinar o tamanho de um botão e definir a legenda usando expressões com campos em uma tabela:

```foxpro
* set button width to length of 'Call ' + first and last names
frmForm1.cmdButton1.Width = 5 + ;
   LEN(ALLTRIM(employee.first_name    + " " + employee.last_name))
* set button caption to 'Call ' + first and last names
frmForm1.cmdButton1.Caption = "Call " + ;
   ALLTRIM(employee.first_name + " " + employee.last_name)
```

Você também poderia definir a legenda usando uma função definida pelo usuário:

```foxpro
frsSet1.frmForm1.cmdButton1.Caption = setcaption()
```

# Definindo várias propriedades

Você pode definir várias propriedades de uma vez.

### Para definir várias propriedades
- Use a estrutura de comando WITH ... ENDWITH. Por exemplo, para definir várias propriedades de uma coluna em uma grade em um formulário, você poderia incluir a seguinte instrução em qualquer código de evento ou método no formulário: WITH THISFORM.grdGrid1.grcColumn1 .Width = 5 .Resizable = .F. .ForeColor = RGB(0,0,0) .BackColor = RGB(255,255,255) .SelectOnEntry = .T. ENDWITH

# Chamando métodos em tempo de execução

Depois que um objeto é criado, você pode chamar os métodos desse objeto de qualquer lugar em seu aplicativo.

### Para chamar um método para um objeto
- Use a seguinte sintaxe: Parent . Object . Method

Por exemplo, o código a seguir chama métodos para exibir um formulário e definir o foco em um botão de comando:

```foxpro
* form set saved in MYF_SET.SCX
myf_set.frmForm1.Show
myf_set.frmForm1.cmdButton1.SetFocus
```

Para ocultar o formulário, emita este comando:

```foxpro
myf_set.frmForm1.Hide
```
