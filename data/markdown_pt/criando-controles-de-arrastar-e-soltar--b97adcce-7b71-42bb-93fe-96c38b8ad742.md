# Criando controles de arrastar e soltar

Ao projetar aplicações Visual FoxPro, você pode arrastar texto, arquivos e objetos da Component Gallery, da janela Project Manager, do Database Designer (Visual FoxPro) e do Data Environment Designer para os locais desejados em formulários e relatórios. Os recursos de arrastar e soltar no Visual FoxPro permitem que você estenda essa capacidade ao usuário em tempo de execução.

Essa capacidade de arrastar e soltar se estende a operações com vários formulários. O usuário pode arrastar texto, arquivos e controles para qualquer lugar da tela, inclusive outros formulários.

Dois tipos de funcionalidade de arrastar e soltar são suportados no Visual FoxPro: OLE drag-and-drop e control drag-and-drop. O OLE drag-and-drop permite mover dados entre outras aplicações que suportam OLE drag-and-drop (como Visual FoxPro, Visual Basic, o Windows Explorer, Microsoft Word e Excel, entre outras). Em uma aplicação Visual FoxPro distribuída, você pode mover dados entre controles na aplicação ou entre controles e outras aplicações Windows que suportam OLE drag-and-drop.

O control drag-and-drop permite arrastar controles Visual FoxPro dentro de suas aplicações Visual FoxPro. O control drag-and-drop também é suportado em versões anteriores do Visual FoxPro. Enquanto o usuário arrasta um controle, o Visual FoxPro fornece um contorno cinza do mesmo tamanho do objeto que se move com o ponteiro do mouse. Você pode substituir esse comportamento padrão especificando um arquivo de cursor (.cur) para a propriedade DragIcon de um controle.

Esta seção descreve o control drag-and-drop. Para obter mais informações sobre OLE drag-and-drop, consulte OLE Drag-and-Drop.

Para ver exemplos de control drag-and-drop, execute Solution.app no diretório ...\Samples\Solution do Visual FoxPro. Na exibição em árvore, clique em Controls e depois em General.

> **Observação:** Arrastar um controle em tempo de execução não altera sua localização automaticamente. Você pode fazer isso, mas deve programar a realocação você mesmo, conforme descrito na seção "Causando movimento de controle em uma operação de arrastar e soltar". Frequentemente, o arrastar é usado apenas para indicar que alguma ação deve ser executada; o controle mantém sua posição original depois que o usuário solta o botão do mouse.

Você pode especificar tanto o significado de uma operação de arrastar quanto como iniciar o arrastar (se houver) para qualquer controle usando as seguintes propriedades, eventos e método de arrastar e soltar.

| Para | Use este recurso |
| --- | --- |
| Habilitar arrastar automático ou manual de um controle. | Propriedade DragMode |
| Especificar qual ícone é exibido quando o controle é arrastado. | Propriedade DragIcon |
| Reconhecer quando um controle é solto no objeto. | Evento DragDrop |
| Reconhecer quando um controle é arrastado sobre o objeto. | Evento DragOver |
| Iniciar ou parar o arrastar manual. | Método Drag |

Todos os controles visuais podem ser arrastados em tempo de execução e todos os controles compartilham as propriedades listadas na tabela anterior. Formulários reconhecem os eventos DragDrop e DragOver, mas não possuem as propriedades DragMode e DragIcon.

# Habilitando o modo de arrastar automático

Para permitir que o usuário arraste um controle sempre que clicar no controle, defina sua propriedade DragMode como 1. Isso habilita o arrastar automático do controle. Quando você define o arrastar como Automatic, o arrastar está sempre ativo.

> **Observação:** Enquanto uma operação de arrastar automático está em andamento, o controle sendo arrastado não reconhece outros eventos de mouse.

# Respondendo quando o usuário solta o objeto

Quando o usuário solta o botão do mouse após arrastar um controle, o Visual FoxPro gera um evento DragDrop. Você pode responder a esse evento de várias maneiras. Você pode realocar o controle na nova localização (indicada pela última posição do contorno cinza). Lembre-se de que o controle não se move automaticamente para a nova localização.

Dois termos são importantes ao discutir operações de arrastar e soltar — origem e destino.

| Termo | Significado |
| --- | --- |
| Origem | O controle sendo arrastado. |
| Destino | O objeto sobre o qual o usuário solta o controle. Este objeto, que pode ser um formulário ou controle, reconhece o evento DragDrop. |

Um controle torna-se o destino se a posição do mouse estiver dentro de suas bordas quando o botão é solto. Um formulário é o destino se o ponteiro estiver em uma porção em branco do formulário.

O evento DragDrop recebe três parâmetros: oSource, nXCoord e nYCoord. O parâmetro oSource é uma referência ao controle que foi solto no destino. Os parâmetros nXCoord e nYCoord contêm as coordenadas horizontal e vertical, respectivamente, do ponteiro do mouse dentro do destino.

Como oSource é um objeto, você o usa como usaria um controle — pode referenciar suas propriedades ou chamar um de seus métodos. Por exemplo, as instruções a seguir no código associado ao evento DragDrop verificam se o usuário soltou um controle sobre si mesmo:

```foxpro
LPARAMETERS oSource, nXCoord, nYCoord
IF oSource.Name != THIS.Name
   * Take some action.
ELSE
   * Control was dropped on itself.
   * Take some other action.
ENDIF
```

Todos os tipos possíveis de controle para oSource possuem uma propriedade Visible (Visual FoxPro). Portanto, você pode tornar um controle invisível quando ele é solto em determinada parte de um formulário ou em outro controle. A linha a seguir no código associado ao evento DragDrop de um Image Control (Visual FoxPro) faz um controle arrastado desaparecer quando é solto na imagem:

```foxpro
LPARAMETERS oSource, nXCoord, nYCoord
oSource.Visible = .F.
```

# Indicando zonas de soltura válidas

Quando você habilita a funcionalidade de arrastar e soltar, pode ajudar seus usuários incluindo pistas visuais sobre onde um usuário pode e não pode soltar um controle. A melhor maneira de fazer isso é alterar a propriedade DragIcon da origem no código associado ao evento DragOver.

O código a seguir no evento DragOver de um controle indica ao usuário que o controle não é um destino de soltura válido. Neste exemplo, `cOldIcon` é uma propriedade definida pelo usuário do formulário.

```foxpro
LPARAMETERS oSource, nXCoord, nYCoord, nState
DO CASE
   CASE nState = 0 && Enter
      THISFORM.cOldIcon = oSource.DragIcon
      oSource.DragIcon = "NODROP01.CUR"
   CASE nState = 1 && Leave
      oSource.DragIcon = THISFORM.cOldIcon
ENDCASE
```

# Controlando quando o arrastar inicia ou para

O Visual FoxPro possui uma configuração Manual para a propriedade DragMode que oferece mais controle do que a configuração Automatic. A configuração Manual permite especificar quando um controle pode e não pode ser arrastado. (Quando DragMode está definido como Automatic, o controle sempre pode ser arrastado enquanto a configuração não for alterada.)

Por exemplo, você pode querer habilitar o arrastar em resposta aos eventos MouseDown e MouseUp, ou em resposta a um comando de teclado ou menu. A configuração Manual também permite reconhecer um evento MouseDown antes do início do arrastar, para que você possa registrar a posição do mouse.

Para habilitar o arrastar a partir do código, deixe DragMode em sua configuração padrão (0 - Manual). Em seguida, use o método Drag sempre que desejar iniciar ou parar o arrastar de um objeto.

Se nAction for 1, o método Drag inicia o arrastar do controle. Se nAction for 2, o controle é solto, causando um evento DragDrop. O valor 0 para nAction cancela o arrastar. O efeito é semelhante ao de dar o valor 2, exceto que nenhum evento DragDrop ocorre.

> **Observação:** Para habilitar uma operação de arrastar e soltar a partir de uma list box, o melhor lugar para chamar o método Drag é no código associado ao evento MouseMove da list box de origem, depois de determinar que o botão do mouse está pressionado. Para um exemplo, consulte Lmover.scx no diretório ...\Samples\Solution\Controls\Lists do Visual FoxPro.

# Causando movimento de controle em uma operação de arrastar e soltar

Você pode querer que o controle de origem altere de posição depois que o usuário solta o botão do mouse. Para fazer um controle se mover para a nova localização do mouse, use o método Move (Visual FoxPro). Por exemplo, o código a seguir no evento DragDrop de um formulário move o controle arrastado para a localização da soltura:

```foxpro
LPARAMETERS oSource, nXCoord, nYCoord
oSource.Move(nXCoord, nYCoord)
```

Este código pode não produzir exatamente os efeitos desejados, porque o canto superior esquerdo do controle é posicionado na localização do mouse. O código a seguir posiciona o centro do controle na localização do mouse:

```foxpro
LPARAMETERS oSource, nXCoord, nYCoord
oSource.Move ((nXCoord – oSource.Width / 2), ;
   (nYCoord – oSource.Height / 2))
```

O código funciona melhor quando a propriedade DragIcon está definida com um valor diferente do padrão (o retângulo cinza). Quando o retângulo cinza está sendo usado, o usuário normalmente deseja que o controle se mova precisamente para a posição final do retângulo cinza. Para fazer isso, registre a posição inicial do mouse dentro do controle de origem. Em seguida, use essa posição como deslocamento quando o controle for movido. Para um exemplo, consulte Ddrop.scx no diretório ...\Samples\Solution\Forms do Visual FoxPro.

### Para registrar a posição inicial do mouse
- Especifique o arrastar manual do controle.
- Declare duas variáveis de nível de formulário, n DragX e n DragY.
- Ative o arrastar quando ocorrer um evento MouseDown. Além disso, armazene o valor de nXCoord e nYCoord nas variáveis de nível de formulário neste evento.
- Desative o arrastar quando ocorrer o evento MouseUp.
