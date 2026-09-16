# Criando um contêiner de visualização personalizado

Descreve como substituir o contêiner de visualização padrão pelo seu próprio componente personalizado que pode fornecer funcionalidade de visualização de relatório em todo o aplicativo automaticamente quando você SET REPORTBEHAVIOR 90.

# Pré-requisitos

Objeto ReportListener

A API Preview Container

# A visualização mais simples

O exemplo de visualização mais simples possível não usa a API Preview Container, mas usa métodos do objeto ReportListener para demonstrar o mecanismo essencial por trás da API.

Os comandos a seguir configuram um objeto Shape de destino, executam um relatório no modo assistido por objeto e usam os métodos do objeto ReportListener para exibir a primeira página do relatório no shape de destino:

```foxpro
* Set up a target for the preview rendering:
_SCREEN.AddObject("canvas","Shape")
_SCREEN.canvas.Width  = 250
_SCREEN.canvas.Height = 300
* Create a base ReportListener and buffer the entire report:
rl = NEWOBJECT("ReportListener")
rl.ListenerType = 3  && Buffer all pages, do not preview automatically
* Process the report:
REPORT FORM (_SAMPLES+"\solution\reports\colors.frx") OBJECT rl
* Render page 1 to the target:
rl.OutputPage( 1, _SCREEN.canvas, 2 )
```

Depois de executar essas instruções na janela Command, você verá uma imagem em tamanho miniatura do relatório renderizada na superfície da tela.

Pontos a observar:
 - O terceiro parâmetro passado ao método OutputPage() do ReportListener é 2, o que indica que o identificador de destino passado no segundo parâmetro é uma referência de objeto Visual FoxPro — o controle Shape.
- O objeto Shape não precisava estar visível para o relatório ser exibido.
- Um Container ou um controle Shape pode ser usado como destino.
- Arrastar a janela Command sobre a visualização a apaga da tela, porque quando a tela recebe uma mensagem de pintura, ela se repinta sem conhecimento da renderização de visualização.

# Implementando um contêiner de visualização simples

O próximo passo é encapsular o processo descrito acima em uma classe que implementa a API preview container, permitindo reutilizar a lógica de visualização.

O programa de exemplo a seguir, simplepreview.prg, contém uma definição de classe que também usa um objeto Shape como destino de renderização, desta vez em uma classe de formulário que implementa a API preview container:

```foxpro
*-----------------------------------------
* simplepreview.prg
*-----------------------------------------
DEFINE CLASS SimplePreview AS Form
    Caption     = "Click for next page"
    ListenerRef = .NULL.
    PageNo      = 1
    AllowOutput = .F.
    ADD OBJECT Canvas AS Shape WITH ;
        Top = 12, Left = 8, ;
        Height = 252, Width = 209, ;
        Name = "Canvas"
    PROCEDURE Canvas.Click
        WITH THISFORM
            IF .PageNo < .ListenerRef.OutputPageCount
                .PageNo = .PageNo + 1
                .Refresh()
            ENDIF
        ENDWITH
    ENDPROC
    PROCEDURE SetReport
        LPARAMETER oListenerRef
        THIS.ListenerRef = oListenerRef
    ENDPROC
    PROCEDURE QueryUnload
        IF NOT ISNULL( THIS.ListenerRef )
            THIS.ListenerRef.OnPreviewClose(.F.)
            THIS.ListenerRef = .NULL.
        ENDIF
        THIS.Hide()
        NODEFAULT
    ENDPROC
    PROCEDURE Paint
        IF NOT ISNULL( THIS.ListenerRef )
            THIS.ListenerRef.OutputPage( THIS.PageNo, THIS.Canvas, 2 )
        ENDIF
    ENDPROC
ENDDEFINE
```

Esta classe implementa os dois métodos da API preview container definindo explicitamente um método SetReport(); e por ser derivada da classe base Form, que já tem um método Show() apropriado.

Pontos a observar:
 - Esta classe resolve os problemas de repintura do exemplo anterior adicionando código ao evento Paint() do formulário para garantir que a imagem de visualização seja redesenhada quando necessário.
- O objeto Reportlistener chamará SetReport(), passando uma referência a si mesmo quando precisar que o contêiner de visualização execute inicialização básica não específica de relatório. SetReport() também será chamado com null (.NULL.) quando seu método OnPreviewClose() for invocado.
- O código no evento QueryUnload() informa ao report listener que você terminou de visualizar o relatório e, em seguida, anula a referência ao objeto report listener para evitar uma condição de deadlock que impediria o formulário de fechar.
- O código no método Shape.Click() usa a propriedade OutputPageCount do report listener para garantir que a visualização não solicite uma página que não exista.

O código a seguir demonstra como reutilizar um componente de contêiner de visualização, instanciando a classe SimplePreview e atribuindo-a à propriedade PreviewContainer de um objeto ReportListener. Tente na janela Command:

```foxpro
pc = NEWOBJECT("SimplePreview", "simplepreview.prg")
rl = NEWOBJECT("ReportListener")
rl.ListenerType     = 1 && Buffer all pages, use preview container
rl.PreviewContainer = pc
REPORT FORM (_SAMPLES+"\solution\reports\colors.frx") OBJECT rl
REPORT FORM (HOME()+"Tools\Filespec\60frx2.frx") OBJECT rl
```

Depois de executar este código, você observará que o formulário SimplePreview é exibido automaticamente. Isso ocorre porque o objeto report listener invocou o método PreviewContainer.Show() depois que o relatório concluiu o processamento.

Se você alterar a última linha do exemplo acima para incluir a cláusula `NOWAIT`, observará que o formulário de visualização não é mais modal quando exibido. O objeto report listener reconhece a cláusula `NOWAIT` e invoca Show(0) em vez de Show(1).

### Ocultar ou liberar?
 - Em SimplePreview.prg acima, o evento QueryUnload() suprime o comportamento padrão com NODEFAULT e oculta manualmente o formulário chamando Hide().

Isso ocorre por dois motivos:
 - Há uma referência pendente ao formulário mantida pela propriedade PreviewContainer do report listener, o que significa que, sem código adicional, o formulário não fechará e liberará quando você clicar na caixa de fechar. A caixa de fechar será desabilitada e o formulário permanecerá visível.
- O Hide() permite que o contêiner de visualização seja reutilizado em visualizações de relatório sucessivas, conforme mostra o código de exemplo anterior.

Se você não deseja que seu contêiner de visualização personalizado permaneça disponível para visualizações de relatório adicionais com o report listener, pode modificar o método QueryUnload conforme mostrado abaixo:

```foxpro
    PROCEDURE QueryUnload
        IF NOT ISNULL( THIS.ListenerRef )
            THIS.ListenerRef.PreviewContainer = .NULL.
            THIS.ListenerRef.OnPreviewClose(.F.)
            THIS.ListenerRef = .NULL.
        ENDIF
    ENDPROC
```

Esta implementação alternativa resulta no contêiner de visualização sendo descartado após uma visualização de relatório. Tente as etapas acima novamente na janela Command com a classe de contêiner de visualização revisada e verá que apenas a primeira visualização usa SimplePreview. A segunda execução de relatório reverte para o contêiner de visualização padrão porque o objeto ReportListener detecta que não tem mais uma referência em sua propriedade PreviewContainer e solicita um novo via _REPORTPREVIEW.

# Dimensionamento e impressão

### Dimensionamento

No exemplo anterior, as dimensões da página de visualização renderizada são ditadas exclusivamente pelo tamanho do controle Shape. Se você alterar a Width do Shape para o dobro do tamanho atual, observará que a imagem de visualização é distorcida de forma semelhante.

Você pode obter informações adicionais sobre o layout do relatório a partir da referência ReportListener para dimensionar a representação da página adequadamente. Adicione o seguinte código de método à definição de classe acima:

```foxpro
    PROCEDURE Show
        LPARAMETER iMode
        IF NOT ISNULL( THIS.ListenerRef )
            LOCAL nWidthInches, nHeightInches
            nWidthInches  = THIS.ListenerRef.GetPageWidth()/960
            nHeightInches = THIS.ListenerRef.GetPageHeight()/960
            * Assume: Scale by 50% on a 96 DPI screen:
            THIS.Canvas.Height = INT( nHeightInches * 96 * 0.5 )
            THIS.Canvas.Width  = INT( nWidthInches * 96 * 0.5 )
        ENDIF
        DODEFAULT( iMode )
    ENDPROC
```

Este é o local apropriado para este código porque a instância ReportListener garante invocar o método Show() do contêiner de visualização em um ponto em que os métodos GetPageHeight() e GetPageWidth() retornarão valores corretos para o relatório sendo visualizado. O método SetReport() será chamado antes que informações precisas estejam disponíveis.

### Impressão

Você pode especificar que o relatório seja impresso passando um parâmetro de `.T.` ao método OnPreviewClose() do report listener conforme o formulário é fechado.

# Definindo como padrão

Você pode substituir o contêiner de visualização padrão usado pela visualização de relatório assistida por objeto no Visual FoxPro adicionando as linhas a seguir ao topo do programa que contém a definição de classe SimplePreview introduzida anteriormente neste tópico:

```foxpro
*-----------------------------------------
* Add to the top  of simplepreview.prg
*-----------------------------------------
LPARAMETER loPreviewContainerRef
* parameter is passed by reference
loPreviewContainerRef = CREATEOBJECT("SimplePreview")
RETURN
DEFINE CLASS SimplePreview AS Form
...
```

Este programa agora é adequado para atribuição a _REPORTPREVIEW, especificando o contêiner de visualização a ser retornado ao Visual FoxPro sempre que um for solicitado por um objeto ReportListener executando um REPORT… PREVIEW no modo assistido por objeto.

Você pode testá-lo na janela Command:

```foxpro
_REPORTPREVIEW = "simplepreview.prg"
SET REPORTBEHAVIOR 90
REPORT FORM (HOME()+"Tools\Filespec\60frx2.frx") preview
```

# Próximas etapas

Consulte Leveraging the Default Preview Container
