# Definindo um controle Grid

Um grid contém colunas, que por sua vez podem conter cabeçalhos e qualquer outro controle. O controle padrão contido em uma coluna é uma caixa de texto, de modo que a funcionalidade padrão do grid se aproxima de uma janela Browse. No entanto, a arquitetura subjacente do grid permite extensibilidade ilimitada.

O exemplo a seguir cria um formulário que contém um objeto Grid com duas colunas. A segunda coluna contém uma caixa de seleção para exibir os valores em um campo lógico em uma tabela.
 Controle Grid com uma caixa de seleção em uma coluna
 Definição de uma classe Grid com uma caixa de seleção em uma coluna do grid
| Código | Comentários |
| --- | --- |
| DEFINE CLASS grdProducts AS Grid Left = 24 Top = 10 Width = 295 Height = 210 Visible = .T. RowHeight = 28 ColumnCount = 2 | Inicia a definição da classe e define propriedades que determinam a aparência do grid. Quando você define a propriedade ColumnCount como 2, adiciona duas colunas ao grid. Cada coluna contém um cabeçalho com o nome Header1. Além disso, cada coluna tem um grupo independente de propriedades que determina sua aparência e comportamento. |
| Column1.ControlSource ="prod_name" Column2.ControlSource ="discontinu" | Quando você define o ControlSource de uma coluna, a coluna exibe os valores desse campo para todos os registros da tabela. Discontinu é um campo lógico. |
| Column2.Sparse = .F. | Column2 conterá a caixa de seleção. Defina a propriedade Sparse da coluna como .F. para que a caixa de seleção seja visível em todas as linhas, não apenas na célula selecionada. |
| Procedure Init THIS.Column1.Width = 175 THIS.Column2.Width = 68 THIS.Column1.Header1.Caption = ; "Product Name" THIS.Column2.Header1.Caption = ; "Discontinued" THIS.Column2.AddObject("chk1", ; "checkbox") THIS.Column2.CurrentControl = ; "chk1" THIS.Column2.chk1.Visible = .T. THIS.Column2.chk1.Caption = "" ENDPROC | Define larguras de coluna e legendas de cabeçalho. O método AddObject permite adicionar um objeto a um contêiner — neste caso, uma caixa de seleção chamada chk1 . Defina o CurrentControl da coluna para a caixa de seleção para que ela seja exibida. Certifique-se de que a caixa de seleção esteja visível. Defina a legenda como uma cadeia de caracteres vazia para que a legenda padrão "chk1" não seja exibida. |
| ENDDEFINE | Fim da definição da classe. |

A definição de classe a seguir é o formulário que contém o grid. Ambas as definições de classe podem ser incluídas no mesmo arquivo de programa.
 Definição de uma classe Form que contém a classe Grid
| Código | Comentários |
| --- | --- |
| DEFINE CLASS GridForm AS FORM Width = 330 Height = 250 Caption = "Grid Example" ADD OBJECT grid1 AS grdProducts | Cria uma classe de formulário e adiciona a ela um objeto baseado na classe grid. |
| PROCEDURE Destroy CLEAR EVENTS ENDPROC ENDDEFINE | O programa que cria um objeto baseado nesta classe usará READ EVENTS . Incluir CLEAR EVENTS no evento Destroy do formulário permite que o programa termine a execução quando o usuário fecha o formulário. Fim da definição da classe. |

O programa a seguir abre a tabela com os campos a serem exibidos nas colunas do grid, cria um objeto baseado na classe GridForm e emite o comando READ EVENTS:

```foxpro
CLOSE DATABASE
OPEN DATABASE (HOME(2) + "data\testdata.dbc")
USE products
frmTest= CREATEOBJECT("GridForm")
frmTest.Show
READ EVENTS
```

Este programa pode ser incluído no mesmo arquivo com as definições de classe se vier no início do arquivo. Você também pode usar o comando SET PROCEDURE TO para especificar o programa com as definições de classe e incluir este código em um programa separado.
