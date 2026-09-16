# Como: tornar controles mais fáceis de usar

Você pode tornar a interface do usuário do aplicativo mais fácil de entender e usar criando teclas de acesso, definindo a ordem de tabulação, exibindo texto de ToolTip e desativando controles selecionados.

# Criando teclas de acesso

Você pode criar teclas de acesso para que os usuários possam escolher um controle de qualquer lugar do formulário pressionando ALT e a tecla.

### Para especificar uma tecla de acesso para um controle
- Na propriedade Caption do controle, preceda a letra desejada com uma barra invertida (\) seguida imediatamente por um sinal de menor que (<).

Para obter mais informações, consulte Caption Property (Visual FoxPro).

Por exemplo, a seguinte configuração para a propriedade Caption de um command button cria uma tecla de acesso usando a letra "O":

```foxpro
Caption = "\<Open"
```

O usuário pode escolher o command button em qualquer lugar do formulário pressionando ALT+O.

### Para especificar uma tecla de acesso para um text box ou edit box
- Crie um label contendo uma barra invertida (\) e um sinal de menor que (<) precedendo a letra desejada, por exemplo, C\<ustomer .
- Certifique-se de que o label é o controle na ordem de tabulação imediatamente anterior ao text box ou edit box que deve receber o foco.

# Definindo a ordem de tabulação para controles

A ordem de tabulação padrão dos controles no formulário é definida na ordem em que você adicionou os controles ao formulário. Você pode redefinir a ordem de tabulação para que o usuário percorra os controles em uma ordem mais lógica.

### Para alterar a ordem de tabulação dos controles
- Abra o formulário no Form Designer .
- No menu View, aponte para Tab Order e clique em Assign Interactively . Dica Você também pode clicar em Set Tab Order na barra de ferramentas do Form Designer. Para definir a ordem de tabulação usando uma lista, clique em Assign by List .
- Clique duas vezes na caixa numerada ao lado do controle que deve ter o foco inicial quando o formulário abrir.
- Clique na caixa numerada ao lado dos outros controles na ordem em que deseja que sejam acessados por tabulação.
- Quando terminar, clique em qualquer lugar fora das caixas numeradas..

Você também pode definir o método padrão para atribuir a ordem de tabulação usando uma lista definindo a opção Tab ordering na guia Forms da Options Dialog Box (Visual FoxPro).

Você pode definir a ordem de seleção para os option buttons e command buttons dentro de um control group. Para mover para um control group com o teclado, um usuário tabula até o primeiro botão no control group e depois usa as teclas de seta para selecionar outros botões no grupo.

### Para alterar a ordem de seleção dos botões dentro de um control group
- Na Properties Window (Visual FoxPro) , selecione o grupo na lista Object. Uma borda grossa indica que o grupo está em modo de edição.
- Selecione a janela Form Designer.
- No menu View, escolha Tab Order .
- Defina a ordem de seleção como faria com a ordem de tabulação dos controles.

# Definindo texto de ToolTip

Cada controle tem uma propriedade ToolTipText que permite especificar o texto exibido quando o usuário pausa o ponteiro do mouse sobre o controle. Dicas são especialmente úteis para botões com ícones em vez de texto.

### Para especificar texto de ToolTip
- Na Properties Window (Visual FoxPro) , selecione a propriedade ToolTipText e digite o texto desejado.

A propriedade ShowTips do formulário determina se o texto de ToolTip é exibido.

# Alterando a exibição do ponteiro do mouse

Você pode fornecer indicações visuais sobre os diferentes estados em que seu aplicativo pode estar alterando a exibição do ponteiro do mouse.

### Para alterar a exibição do ponteiro do mouse
- Crie um método que altere o ponteiro do mouse para um estado diferente.

Por exemplo, na classe tsBaseForm do aplicativo de exemplo Tasmanian Traders, um método WaitMode altera o ponteiro do mouse para o cursor de estado de espera padrão. Antes de executar qualquer código que possa levar algum tempo para processar, o aplicativo Tasmanian Traders passa um valor true (.T.) para o método WaitMode para alterar o ponteiro e informar ao usuário que o processamento está em andamento. Após a conclusão do processamento, uma chamada a WaitMode com false (.F.) restaura o ponteiro do mouse padrão.

```foxpro
* WaitMode Method of tsBaseForm class
LPARAMETERS tlWaitMode
lnMousePointer = IIF(tlWaitMode, MOUSE_HOURGLASS, MOUSE_DEFAULT)
THISFORM.MousePointer = lnMousePointer
THISFORM.SetAll('MousePointer', lnMousePointer)
```

 - Se deseja alterar o ponteiro do mouse para algo diferente de um dos ponteiros padrão, defina a propriedade MousePointer como 99 - Custom e defina a propriedade MouseIcon para seu próprio arquivo cursor (.cur) ou ícone (.ico). Para obter mais informações, consulte MousePointer Property e MouseIcon Property .

# Ativando e desativando controles

Você pode ativar ou desativar controles se eles não estiverem disponíveis sob certas condições.

### Para ativar ou desativar um controle
- Defina a propriedade Enabled do controle como False (.F.).

Para obter mais informações, consulte Enabled Property (Visual FoxPro).

Você pode ativar ou desativar option buttons ou command buttons individuais em um grupo definindo a propriedade Enabled de cada botão como True (.T.) ou False (.F.). Você também pode desativar ou habilitar todos os botões em um grupo definindo a propriedade Enabled do grupo, como na seguinte linha de código:

```foxpro
frmForm1.cmgCommandGroup1.Enabled = .T.
```

Quando você define a propriedade Enabled de um option button group ou command button group como false (.F.), todos os botões no grupo são desativados, mas não serão exibidos com ForeColor e BackColor desativados. Definir a propriedade Enabled do grupo não altera a propriedade Enabled dos botões individuais no grupo. Isso permite desativar um grupo de botões com alguns dos botões já desativados. Quando você habilita o grupo, os botões que estavam originalmente desativados permanecem desativados.

Se deseja desativar todos os botões em um grupo para que apareçam desativados e não deseja preservar informações sobre quais botões estavam originalmente desativados ou habilitados, pode usar o método SetAll do grupo, assim:

```foxpro
frmForm1.opgOptionGroup1.SetAll("Enabled", .F.)
```
