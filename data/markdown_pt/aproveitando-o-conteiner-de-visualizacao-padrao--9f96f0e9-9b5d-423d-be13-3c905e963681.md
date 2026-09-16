# Aproveitando o Contêiner de Visualização Padrão

Para facilitar a configuração SET REPORTBEHAVIOR 90, o Visual FoxPro é fornecido com um aplicativo de fábrica de contêiner de visualização padrão, ReportPreview.App. Ele está localizado no diretório HOME() junto com as outras ferramentas e é referenciado por padrão na variável de sistema _REPORTPREVIEW.

Este tópico descreve as capacidades do componente Preview Container fornecido por ReportPreview.App, além da API padrão do Preview Container.

# Pré-requisitos
 - A API do Preview Container
- Variável de Sistema _REPORTPREVIEW

# Diagrama de Objetos

A ilustração a seguir mostra o diagrama de objetos do contêiner de visualização padrão conforme existe após o mecanismo de relatório ter chamado o método `Show()`. Antes desse ponto, os objetos membro `oForm` e `oForm.Toolbar` podem não ter sido instanciados:

Um objeto proxy é usado porque, para suportar várias cláusulas do comando REPORT FORM… PREVIEW no modo assistido por objeto, a visualização pode instanciar uma de várias classes de formulário específicas derivadas da classe pai frxPreviewForm como sua referência `oForm`:

| Nome da Classe | Derivada De | Observações |
| --- | --- | --- |
| Form | n/a | Classe base de formulário do Visual FoxPro |
| frxBaseForm | Form | Implementa tratamento de erros e suporte a fontes grandes. |
| frxPreviewForm | frxBaseForm | Implementa a API do Preview Container. .ShowWindow = 1 - em formulário de nível superior |
| frxPreviewAsTopForm | frxPreviewForm | .ShowWindow = 2 - Como formulário de nível superior |
| frxPreviewInScreen | frxPreviewForm | .ShowWindow = 0 - Na Tela |
| frxPreviewInDesktop | frxPreviewForm | .Desktop = .T. |

As propriedades e métodos descritos abaixo são membros do objeto frxPreviewProxy.

# Propriedades e Métodos Adicionais

Além da API padrão do contêiner de visualização, o componente padrão retornado por ReportPreview.App expõe outras propriedades e métodos que podem ser usados para controlar a aparência da janela Preview quando o modo de relatório assistido por objeto é usado.

### Propriedades

Essas propriedades controlam apenas o estado inicial da janela de visualização. Se definidas com valores não padrão, essas propriedades têm precedência sobre quaisquer preferências restauradas do arquivo de recursos.

| Nome da Propriedade | Tipo | Descrição |
| --- | --- | --- |
| Top | I | Especifica o deslocamento vertical a partir do topo da janela principal do Visual FoxPro do formulário de visualização, em pixels. |
| Left | I | Especifica o deslocamento horizontal esquerdo a partir do lado esquerdo da janela principal do Visual FoxPro do formulário de visualização, em pixels. |
| Width | I | Especifica o tamanho horizontal do formulário de visualização em pixels. |
| Height | I | Especifica o tamanho vertical do formulário de visualização, em pixels. |
| ToolbarIsVisible | L | Especifica que a barra de ferramentas da janela de visualização deve estar inicialmente visível. |
| Caption | C | Especifica o caption da janela de visualização. |
| CanvasCount | I | Especifica o número inicial de páginas renderizadas no formulário de visualização. Valores válidos são 1, 2 ou 4. |
| ZoomLevel | I | Especifica o nível de zoom inicial da janela de visualização. Valores possíveis são: 1 - 10% 2 - 25% 3 -50% 4 - 75% 5 - 100% (padrão) 6 - 150% 7 - 200% 8 - 300% 9 - 500% 10 - página inteira |
| CurrentPage | I | Especifica a página inicial a renderizar no formulário de visualização. O padrão é 1. Se for maior que o número de páginas disponíveis, a última página será exibida. |
| TopForm | L | Especifica se o formulário de visualização deve ser um formulário de nível superior independente. Isso forçará uma sessão de visualização sem modo (NOWAIT), e a barra de ferramentas é automaticamente encaixada no topo do formulário. O valor padrão é false ( .F. ). |
| TextOnToolbar | L | Especifica que os botões da barra de ferramentas devem mostrar captions de texto. O valor padrão é false ( .F. ). |
| AllowPrintFromPreview | B | Especifica se o botão Print na barra de ferramentas Preview ou o botão de comando Print no menu de atalho está habilitado para o Preview Container do objeto report listener. |

### Métodos

Além dos métodos especificados pela API do Preview Container , o contêiner de visualização padrão também expõe todos os métodos públicos da classe base Form.

Os seguintes métodos adicionais podem ser chamados após o contêiner de visualização estar visível:

| Método | Descrição |
| --- | --- |
| SetCurrentPage( iPageNo ) | Move para um número de página específico. |
| SetCanvasCount( iCount ) | Ajusta o número de páginas renderizadas no formulário de visualização. |
| SetZoomLevel( iLevel ) | Ajusta a escala das páginas renderizadas. |
| SetExtensionHandler( oRef ) | Atribui um manipulador de extensão (Consulte abaixo) |

# A Interface do Extension Handler

O contêiner de visualização padrão possui um mecanismo específico que permite modificar ou estender a funcionalidade da interface de usuário de visualização sem criar subclasse ou recompilar o código-fonte.

Você usa SetExtensionHandler() para passar ao contêiner de visualização padrão uma referência a um objeto que implementa um conjunto específico de métodos "hook" que são invocados em pontos específicos. Consulte abaixo a API e o uso de exemplo.

### Propriedades do Preview Extension Handler

| Propriedade | Descrição |
| --- | --- |
| PreviewForm | Esta é uma referência de retorno ao formulário de visualização. Se esta propriedade não existir, ela será criada pelo contêiner de visualização padrão via uma chamada ADDPROPERTY(), e atribuída uma referência ao formulário de visualização. O contêiner de visualização anula a referência de retorno automaticamente antes de liberar para evitar um loop de referência de objeto que poderia impedir isso. Propriedades úteis de .PreviewForm: .PreviewForm.oReport referencia o report listener ativo .PreviewForm.Toolbar referencia o objeto da barra de ferramentas do formulário de visualização. |

### Métodos do Preview Extension Handler

Esses métodos devem ser implementados por um Extension Handler candidato.

| Método | Descrição |
| --- | --- |
| AddBarsToMenu( cPopupName , iNextBarNum ) | Este método é chamado do evento RightClick() do formulário de visualização, diretamente antes da declaração ACTIVATE POPUP (m.cPopupName), para que você possa potencialmente remover barras de menu ou redefini-las. cPopupName é o nome do popup. iNextBarNum é o próximo número de barra disponível. Como você não pode usar a palavra-chave THIS em um comando popup ON SELECTION.., o formulário de visualização disponibiliza uma referência a si mesmo em uma variável oRef. |
| HandledKeyPress( nKey , nModifier ) | Este método é chamado do evento Keypress() do formulário de visualização. Retorne true ( .T. ) se desejar substituir a resposta padrão a uma pressão de tecla específica. Este método é chamado antes do tratamento nativo de keypress do formulário de visualização, para que você possa substituir eventos keypress selecionados. |
| Show( iStyle ) | Este método é chamado do método Show() do formulário de visualização. Você poderá manipular a barra de ferramentas de visualização através da referência THIS.PreviewForm.Toolbar. A barra de ferramentas é realmente criada no evento Init() do formulário de visualização, mas como o extension handler não foi atribuído nesse ponto, o Show() é o melhor lugar para código de configuração e decoração. Observe que a barra de ferramentas também possui uma referência de retorno PreviewForm ao formulário de visualização, para que você possa adicionar botões de comando com código Click() como THIS.Parent.PreviewForm.ExtensionHandler.MyCustomMethod() . |
| Paint() | Chamado do evento Paint() do formulário de visualização, após a visualização ter terminado de renderizar as páginas. |
| Release() | Chamado do evento Release() do formulário de visualização. Retornar false ( .F. ) deste método impedirá o fechamento do formulário de visualização. |

# Exemplo: Personalizando o contêiner de visualização usando um Extension Handler

O exemplo a seguir personaliza a aparência da janela de visualização e também implementa um extension handler que remove a capacidade de alterar o número de páginas renderizadas simultaneamente no formulário de visualização.

```foxpro
* Obtain an instance of the default preview container:
pc = .NULL.
DO (_REPORTPREVIEW) WITH pc
* Set some initial properties:
WITH pc
    .Caption = "My Custom Preview Window"
    .ZoomLevel = 4   && 75%
    .CanvasCount = 1
ENDWITH
* Create an instance of an Extension Handler:
xh = NEWOBJECT("MyRetroPreview")
* Assign it to the preview container:
pc.SetExtensionHandler( m.xh )
* Set up a report listener and give it our preview:
rl = NEWOBJECT("Reportlistener")
rl.ListenerType = 1
rl.PreviewContainer = pc
* Run a report:
REPORT FORM (_SAMPLES+"\solution\reports\colors.frx") OBJECT rl
RETURN
*---------------------------------------------
* Extension Handler Class:
*---------------------------------------------
DEFINE CLASS MyRetroPreview AS Custom
    PROCEDURE AddBarsToMenu( cPopup, iNextBar )
        * Remove the option to change page count:
        RELEASE BAR 8 OF (m.cPopup)
    ENDPROC
    PROCEDURE Show( iStyle )
        * Remove the option to change page count:
        THIS.PreviewForm.Toolbar.opgPageCount.Visible = .F.
        THIS.PreviewForm.CanvasCount = 1
    ENDPROC
    PROCEDURE HandledKeyPress( nKeyCode, nShiftAltCtrl )
        RETURN .F.
    ENDPROC
    PROCEDURE Paint()
    ENDPROC
    PROCEDURE Release()
        RETURN .T.
    ENDPROC
ENDDEFINE
```

# Uso do Arquivo de Recursos

O contêiner de visualização padrão usa o arquivo de recursos atual (como retornado por `SET("RESOURCE",1)` ) para lembrar o tamanho, posição, número de páginas visíveis, nível de zoom, etc., para cada arquivo de relatório.

As preferências de janela e barra de ferramentas são armazenadas na tabela FOXUSER com um ID de "9REPPREVIEW". As preferências de posição e tamanho de janela e barra de ferramentas são salvas independentemente para cada arquivo de relatório individual. A posição e o estado da barra de ferramentas de visualização são comuns a todas as visualizações de relatório. Se o arquivo de recursos não estiver disponível ou for somente leitura, as preferências de janela não são salvas.
