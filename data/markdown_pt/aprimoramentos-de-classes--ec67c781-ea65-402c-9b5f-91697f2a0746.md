# Aprimoramentos de classes

O Visual FoxPro contém os seguintes aprimoramentos a classes, formulários, controles e sintaxe relacionada a orientação a objetos.

# Ancorando controles visuais

Você pode ancorar um controle visual a uma ou mais bordas de seu contêiner pai usando a propriedade Anchor do controle. Quando você ancora um controle visual ao contêiner pai, as bordas do controle permanecem na mesma posição em relação às bordas do contêiner quando você redimensiona o contêiner. Para obter mais informações, consulte Propriedade Anchor.

# Acoplando formulários

O Visual FoxPro estende o suporte de acoplamento a formulários definidos pelo usuário. Acoplar formulários funciona de forma semelhante ao acoplamento de barras de ferramentas, exceto que você pode acoplar formulários a janelas do Ambiente de Desenvolvimento Interativo (IDE) do Visual FoxPro e a outros formulários, e os controles no formulário ainda podem obter foco quando o formulário está acoplado.

O Visual FoxPro inclui as seguintes propriedades, métodos e eventos novos e atualizados para suportar acoplamento de formulários.
 - Dockable Property
- GetDockState Method
- ADOCKSTATE( ) Function
- AfterDock Event
- BeforeDock Event
- Dock Method
- Docked Property
- DockPosition Property
- UnDock Event
- DOCK Command

Para obter mais informações, consulte Como: acoplar formulários.

# Controles CheckBox e OptionButton suportam quebra de palavras

A propriedade WordWrap agora é suportada para controles CheckBox e OptionButton. As porções de texto desses controles agora usam quebra de palavras. Para obter mais informações, consulte Propriedade WordWrap.

# Controles CommandButton podem alinhar texto com imagens

A propriedade Alignment agora se aplica a controles CommandButton ao especificar uma imagem para a propriedade Picture e definir a propriedade PicturePosition para um valor diferente do padrão. A propriedade Alignment também contém configurações novas e revisadas para controles CommandButton, CheckBox e OptionButton. Para obter mais informações, consulte Propriedade Alignment.

# Controles CommandButton, OptionButton e CheckBox podem ocultar Captions

A propriedade PicturePostion contém uma nova configuração de 14 (No text) para controles CommandButton, OptionButton e CheckBox. Você pode usar esta configuração para ocultar as porções de texto desses controles sem precisar definir a propriedade Caption como uma cadeia de caracteres vazia. Esta configuração é particularmente útil quando você deseja incluir uma tecla de atalho para um botão com um gráfico sem exibir o texto do Caption. Você deve definir a propriedade Style como 1 (Graphical) para que esta nova configuração se aplique.

Além disso, a propriedade PicturePosition agora se aplica a controles CheckBox e OptionButton quando Style está definido como 1 (Graphical).

Para obter mais informações, consulte Propriedade PicturePosition.

# Propriedades PictureMargin e PictureSpacing controlam espaçamento e margens em controles CommandButton, OptionButton e CheckBox

Você pode controlar melhor o posicionamento de imagens em controles CommandButton, OptionButton e CheckBox com as novas propriedades PictureMargin e PictureSpacing. A propriedade PictureMargin especifica o espaçamento de margem em pixels entre uma imagem e a borda do controle conforme determinado pela propriedade PicturePosition. A propriedade PictureSpacing especifica o espaçamento de margem em pixels entre uma imagem e o texto no controle.

Para obter mais informações, consulte Propriedade PictureMargin e Propriedade PictureSpacing.

# Suporte a objetos Collection em controles ComboBox e ListBox

Agora você pode especificar objetos Collection como fonte de linha e tipo de fonte de linha para as propriedades RowSource e RowSourceType de controles ComboBox e ListBox. Para obter mais informações, consulte Propriedade RowSource e Propriedade RowSourceType.

# Definindo índices ascendentes ou descendentes em cursors no DataEnvironment

Você pode especificar ordem ascendente ou descendente para um índice de cursor usando a nova propriedade OrderDirection para objetos Cursor.

> **Observação:** OrderDirection é desconsiderado quando a propriedade Order do cursor está vazia.

Para obter mais informações, consulte Propriedade OrderDirection.

# Grade suporta otimização Rushmore

O controle Grid pode ser definido para suportar otimização Rushmore se a fonte de dados subjacente contiver índices que suportem isso.

Para obter mais informações, consulte Propriedade Optimize (Visual FoxPro).

# Controle do ponteiro do mouse para colunas de grade e cabeçalhos de coluna

As propriedades MousePointer e MouseIcon agora se aplicam a objetos Column em uma grade e objetos Header em uma coluna. Para a propriedade MousePointer, você pode especificar a nova configuração de 16 (Down Arrow) para redefinir o ponteiro do mouse para um cabeçalho de coluna para a seta para baixo padrão.

Para obter mais informações, consulte Propriedade MousePointer e Propriedade MouseIcon.

# Rotacionando controles Label, Line e Shape

Você pode usar a nova propriedade Rotation para rotacionar controles Label. A propriedade Rotation se aplica a controles Line e Shape quando usada com a nova propriedade PolyPoints. Para obter mais informações, consulte Propriedade Rotation (Visual FoxPro), Propriedade PolyPoints e Criando formas mais complexas usando a propriedade PolyPoints.

# Controles Label podem exibir fundo com tema

Para controles Label, você pode definir a propriedade Style como Themed Background Only para mostrar apenas cores de fundo com tema quando os temas do Windows estão ativados. A cor de fundo do label é a mesma do contêiner pai do label. Para obter mais informações, consulte Propriedade Style.

# Controles ListBox podem ocultar barras de rolagem

Você pode usar a nova propriedade AutoHideScrollBar para controles ListBox para ocultar barras de rolagem quando a lista contém menos itens do que o número que pode ser visível na list box. Para obter mais informações, consulte Propriedade AutoHideScrollBar.

# Controles de barra de ferramentas podem exibir objetos Separator horizontais

Para objetos Separator, defina a propriedade Style como 1 para exibir uma linha horizontal ou vertical, dependendo de como a barra de ferramentas aparece. Se a barra de ferramentas aparece horizontalmente, a linha é exibida verticalmente. Se a barra de ferramentas aparece verticalmente, a linha é exibida horizontalmente. Em versões anteriores a esta versão, definir Style como 1 exibia apenas uma linha vertical.

> **Observação:** Em versões anteriores a esta versão, barras de ferramentas verticais do sistema e definidas pelo usuário desacopladas não exibiam separadores horizontais. Na versão atual, separadores horizontais agora são exibidos para barras de ferramentas verticais desacopladas.

For more information, see Style Property.

# Controles de barra de ferramentas podem ocultar objetos Separator

A propriedade Visible agora se aplica a objetos Separator para que você possa controlar se um objeto Separator é exibido em controles Toolbar. Quando usada em combinação com a propriedade Style, a propriedade Visible do separador determina se um espaço ou linha é exibido como separador quando sua propriedade Style está definida como 0 (Normal - do not display a line) ou 1 (display a horizontal or vertical line), respectivamente.

Para obter mais informações, consulte Propriedade Visible (Visual FoxPro).

# Criando formas mais complexas

Você pode usar a nova propriedade PolyPoints para controles Line e Shape para criar linhas e formas de polígono. PolyPoints especifica um array de qualquer dimensão contendo coordenadas no formato X1, Y1, X2, Y2, ..., organizadas na ordem em que a linha ou forma de polígono é desenhada.

Para controles Line, quando você cria uma linha de polígono usando a propriedade PolyPoints, pode especificar a nova configuração "S" ou "s" para a propriedade LineSlant para criar uma curva Bezier.

Para obter mais informações, consulte Propriedade PolyPoints e Propriedade LineSlant.

# Controles ComboBox podem ocultar listas suspensas

Agora você pode usar o comando NODEFAULT no evento DropDown para um controle ComboBox. Isso impedirá que a porção de lista suspensa de um controle ComboBox apareça. Para obter mais informações, consulte Comando NODEFAULT.

# NEWOBJECT( ) cria objetos sem acionar código de inicialização

Para imitar o comportamento de uma classe aberta no Class Designer ou Form Designer, passe 0 ao parâmetro cInApplication. Este recurso permite criar ferramentas de tempo de design que visualizam a estrutura de uma classe.

Ao passar 0 ao parâmetro cInApplication para a função NEWOBJECT( ), o Visual FoxPro permite criar uma instância de uma classe sem acionar código de inicialização (como código nos eventos Init, Load, Activate e BeforeOpenTables). Além disso, quando o objeto é liberado, ele não aciona seu código de destrutor (como código nos eventos Destroy e Unload). Apenas o código de inicialização e destrutor é suprimido; o código em outros eventos e métodos ainda é chamado.

Se você usar o parâmetro cInApplication para suprimir código de inicialização e destrutor em um objeto, também o suprime nos objetos filhos do objeto.

Este comportamento não é suportado para o Método NewObject.

Para obter mais informações, consulte Função NEWOBJECT( ).

# Especificar onde o foco é atribuído no evento Valid

Para direcionar onde o foco é atribuído, você pode usar o parâmetro opcional ObjectName no comando RETURN do evento Valid. O objeto especificado deve ser um objeto Visual FoxPro válido. Se o objeto especificado estiver desabilitado ou não puder receber foco, o foco é atribuído ao próximo objeto na ordem de tabulação. Se um objeto inválido for especificado, o Visual FoxPro mantém o foco no objeto atual.

Agora você pode definir foco em objetos nos seguintes cenários:
 - Definir foco em um objeto em outro formulário visível.
- Set focus to an object on a non-visible Page or Pageframe control.

Para obter mais informações, consulte Evento Valid.

# Controles TextBox têm funcionalidade de preenchimento automático

Você pode adicionar funcionalidade de preenchimento automático aos seus controles text box para tornar a entrada de dados mais eficiente. Preenchimento automático é a exibição automática de uma lista suspensa de entradas que correspondem à cadeia de caracteres conforme ela é digitada na caixa de texto. As entradas vêm de uma tabela especial que rastreia valores exclusivos inseridos na caixa de texto, o nome do controle que é a fonte do valor e informações de uso.

As seguintes propriedades suportam preenchimento automático:
 - AutoComplete Property
- AutoCompSource Property
- AutoCompTable Property

Ao definir a propriedade AutoComplete, você determina a ordem de classificação das entradas. Se desejar mais controle sobre a lista e onde ela é armazenada, pode usar a propriedade AutoCompSource para especificar a tabela usada para preencher a lista automática. Por padrão, a tabela é AUTOCOMP.DBF. Você pode usar uma tabela para cada controle text box ou uma única tabela pode preencher listas automáticas para várias caixas de texto.

Se você usar uma única tabela, que é o padrão, a tabela usa valores no campo Source para cada entrada para identificar o controle text box associado à entrada. Por padrão, o valor do campo Source é o nome do controle text box. Você pode especificar o valor do campo Source usando a propriedade AutoCompSource da caixa de texto. Por exemplo, você pode querer disponibilizar o mesmo conjunto de entradas para vários controles Text box no aplicativo, como informações de endereço. Você pode definir explicitamente as propriedades AutoCompTable e AutoCompSource para cada um dos controles para a mesma tabela e valor de campo de origem. A mesma lista automática aparece para cada um deles.

O controle text box trata da atualização da tabela de preenchimento automático para você com base nos valores realmente inseridos na caixa de texto. Se desejar remover um valor da lista, insira uma cadeia de caracteres em uma caixa de texto que corresponda à cadeia que deseja excluir para filtrar a lista. Selecione a entrada na lista e pressione a tecla DELETE. A cadeia de caracteres permanece na tabela, mas não aparece mais na lista automática.

> **Observação:** Você pode controlar o número de itens que aparecem na lista suspensa usando SYS(2910) - Contagem de exibição da lista .

Para obter mais informações, consulte Propriedade AutoComplete, Propriedade AutoCompSource e Propriedade AutoCompTable.

# Novas configurações de propriedades InputMask e Format

As seguintes novas configurações de InputMask e Format estão disponíveis:

Propriedade InputMask

| cMask | Descrição |
| --- | --- |
| U | Permite apenas caracteres alfabéticos e os converte para maiúsculas (A - Z). |
| W | Permite apenas caracteres alfabéticos e os converte para minúsculas (a - z). |

Propriedade Format

| cFunction | Descrição |
| --- | --- |
| Z | Exibe o valor como em branco se for 0, exceto quando o controle tem foco. Datas e DateTimes também são suportados nesses controles. Os delimitadores de data e datetime não são exibidos, a menos que o controle tenha foco. |

For more information, see Propriedade InputMask and Propriedade Format.

# Usar propriedade PictureVal para passar imagens como cadeias de caracteres

A nova propriedade PictureVal do controle Image pode ser usada em vez da Propriedade Picture (Visual FoxPro) para especificar uma expressão de cadeia de caracteres ou objeto de uma imagem. Para um objeto, o formato deve ser de um formato de interface IPicture compatível com a Função LOADPICTURE( ).

Para obter mais informações, consulte Propriedade PictureVal.

# CLEAR CLASSLIB atualizado

O comando CLEAR CLASSLIB agora executa automaticamente um comando CLEAR CLASS em cada classe na biblioteca de classes especificada. Quaisquer erros que possam ocorrer durante a liberação de classes individuais (por exemplo, classe em uso) são ignorados.

> **Observação:** Classes em outras bibliotecas de classes que são usadas ou referenciadas por uma classe na biblioteca de classes especificada não são limpas.

Para obter mais informações, consulte Comandos CLEAR.

# Limite de resolução de tela aumentado

Em versões anteriores do Visual FoxPro, a área máxima definível para um formulário é limitada a duas vezes a Screen Resolution para as dimensões X e Y. Por exemplo, se a resolução do seu monitor é 1280x1024, as dimensões máximas seriam:

```foxpro
Form.Width = 2552
Form.Height = 2014
```

Além disso, se você tentou definir as propriedades Width e Height para esses limites em tempo de design e então executou o formulário, veria que os valores reverteram para os limites de resolução de tela (já que foram salvos dessa forma):

```foxpro
Form.Width = 1280
Form.Height = 998
```

No Visual FoxPro 9.0, esta limitação foi aumentada para aproximadamente 32.000 pixels para cada dimensão e agora permite mais flexibilidade com certos formulários, como os roláveis:

```foxpro
Form.Width = 32759
Form.Height = 32733
```

Para obter mais informações, consulte Propriedade Width e Propriedade Height.

# Eventos de controle de código-fonte ProjectHook

Novos eventos foram adicionados à classe ProjectHook, que permitem executar operações de controle de código-fonte, como check-in e check-out de vários arquivos de uma vez.

Para obter mais informações, consulte Evento SCCInit e Evento SCCDestroy.

# Método AddProperty suporta configurações de tempo de design

Você pode especificar a visibilidade (Protected, Hidden ou Public) e a descrição de uma propriedade usando o método AddProperty com novos parâmetros disponíveis. Essas configurações também podem ser controladas na Caixa de diálogo New Property e na Caixa de diálogo Edit Property/Method. Para obter mais informações, consulte Método AddProperty.

# Método WriteMethod suporta configurações de tempo de design

Você pode especificar a visibilidade (Protected, Hidden ou Public) e a descrição de um método usando o método WriteMethod com novos parâmetros disponíveis. Essas configurações também podem ser controladas na Caixa de diálogo New Property e na Caixa de diálogo Edit Property/Method. Para obter mais informações, consulte Método WriteMethod.
