# Método OutputPage

Fornece acesso à página atual ou ao intervalo completo de páginas de uma execução de relatório, de acordo com o valor da propriedade ListenerType.

```foxpro
oReportListener.OutputPage(;
                  nPageNo, ;
                  eDevice, ;
                  nDeviceType ;
                 [,nleft, nTop, nWidth, nHeight ;
                 [,nClipLeft,nClipTop, nClipWidth, nClipHeight]])
```

#### Parâmetros
 **nPageNo**
No modo de uma página por vez (valores 0 e 2 de ListenerType), ReportListener usa este parâmetro para fornecer o número da página atual à medida que prepara cada página para saída. Nesse momento, você pode solicitar que essa única página seja renderizada em outro dispositivo. No modo de todas as páginas de uma vez (valores 1 e 3 de ListenerType), você usa este parâmetro para enviar a ReportListener o número da página a ser renderizada. Para obter mais informações sobre os valores compatíveis de ListenerType, consulte Propriedade ListenerType.
**eDevice**
Fornece um identificador, uma referência ou um nome de arquivo para o dispositivo no qual a saída é renderizada. Quando ListenerType é 0, ReportListener usa este parâmetro para fornecer um identificador gráfico GDI+ para a impressora atual. Quando ListenerType é 2, a saída não vai de fato para uma impressora, portanto ReportListener fornece o valor 0. No modo de todas as páginas de uma vez (valores 1 e 3), você usa este parâmetro para fornecer a ReportListener: um identificador GDI de impressora; um identificador gráfico GDI+ de outro dispositivo de saída; uma referência a um objeto derivado da classe base Shape ou Container do Visual FoxPro; ou um nome de arquivo. Você informa o tipo do valor eDevice por meio de um valor apropriado em nDeviceType.
**nDeviceType**
Representa o tipo de dispositivo no qual a saída é renderizada. Valor Tipo de dispositivo -1 Nenhum dispositivo. ReportListener fornece esse valor ao disparar OutputPage em ListenerType 2. 0 hDC (identificador GDI). Você pode fornecer um identificador GDI a ReportListener para enviar a saída a outra impressora. 1 hGraphics (identificador gráfico GDI+). ReportListener fornece esse valor ao disparar OutputPage em ListenerType 0. Você pode fornecê-lo para enviar a saída a outro contexto GDI+, como uma janela. 2 oFoxControl. Use este valor para instruir ReportListener a criar uma visualização usando um controle Shape ou Container do Visual FoxPro. 100 Especifica um nome de arquivo a ser salvo como imagem EMF. 101 TIFF. 102 JPEG. 103 GIF. 104 PNG. 105 BMP. 201 Especifica uma página a ser acrescentada a um TIFF criado anteriormente, gerando um arquivo TIFF de várias páginas. Dica: ReportListener pode realizar otimização adicional desse formato quando esse valor é usado antes do término da execução do relatório. Para ListenerType 0 ou 2, o evento OutputPage ocorre durante esse período. Um exemplo é mostrado abaixo. Para ListenerType 1 ou 3, você pode chamar OutputPage durante o evento AfterReport para aproveitar a otimização.
**[nleft, nTop, nWidth, nHeight,[nClipLeft,nClipTop, nClipWidth, nClipHeight]]**
Esses parâmetros opcionais não são relevantes quando nDeviceType é 2 (uma superfície de controle do Visual FoxPro). O primeiro conjunto de quatro coordenadas (nleft, nTop, nWidth, nHeight) especifica, em unidades de 1/960 de polegada (960 dpi), o retângulo no dispositivo atual em que essa ocorrência do elemento de layout será renderizada. O segundo conjunto (nClipLeft, nClipTop, nClipWidth, nClipHeight) permite que um dispositivo de saída de visualização indique que somente uma parte da página precisa ser atualizada.

# Valor de retorno

Nenhum.

# Observações

Aplica-se a: objeto ReportListener.

O método OutputPage é incomum porque, dependendo do valor atual de ListenerType, um ReportListener dispara esse método para sinalizar que uma página está pronta ou espera que você mesmo dispare as chamadas para solicitar as páginas desejadas.

### Noções básicas sobre os dois modos de processamento de OutputPage

No primeiro modo, ReportListener atua de maneira apropriada a impressoras e outros dispositivos que processam a saída uma página por vez. Se necessário, esses dispositivos colocam as páginas recebidas em um spool ou fila até poderem processar mais páginas. Esse processamento ocorre somente para a frente; depois que ReportListener começa a renderizar as páginas seguintes, não é possível solicitar novamente uma página específica isolada.

No segundo modo, ReportListener prepara todas as páginas de uma vez, fornecendo efetivamente uma fila de todas elas até que o dispositivo esteja pronto para solicitá-las. Você não pode solicitar páginas antes que todas estejam preparadas. Contudo, esse processamento resulta em uma coleção de páginas em cache, ou rolável, conforme exigido pelos dispositivos de visualização; depois de preparadas, elas podem ser solicitadas em qualquer ordem e várias vezes.

### Tratamento de erros dos parâmetros de OutputPage

A lista de parâmetros de OutputPage é complexa e alguns parâmetros têm vários usos. Por isso, pode ser difícil interpretar os erros recebidos quando eles são usados incorretamente.

A seguir estão as mensagens de erro esperadas quando valores inesperados ou inadequados são enviados a ReportListener neste método.

| Mensagem e número do erro | Condições que disparam o erro |
| --- | --- |
| É necessário especificar parâmetros adicionais (Erro 94) | Disparado quando os três parâmetros obrigatórios (nPageNo, eDevice, nDeviceType) não são incluídos. |
| O valor, tipo ou número de argumentos da função é inválido (Erro 11) | Disparado quando nDeviceType recebe um valor não reconhecido. |
| A propriedade DataType do campo 'eDevice' é inválida (Erro 1544) | Disparado quando o tipo de dados de eDevice não atende aos requisitos de nDeviceType. Por exemplo, quando nDeviceType é 0 ou 1 e eDevice não é um identificador válido, ou quando nDeviceType é um dos tipos de nome de arquivo e eDevice não é uma cadeia que representa um nome de arquivo válido. |
| Erro ao gravar no arquivo 'filename' (Erro 1105) | Disparado quando nDeviceType é um tipo de nome de arquivo e eDevice parece válido, mas o arquivo não pode ser criado. Por exemplo, o usuário pode não ter permissão para criar arquivos no diretório especificado. |
| A página de saída 'pageno' não está disponível (Erro 2194) | Disparado quando nPageNo não é apropriado às páginas renderizadas atuais ou quando ListenerType não está definido corretamente como 0, 1, 2 ou 3, valores nos quais ReportListener renderiza páginas. |

Para obter mais informações sobre mensagens de erro do Visual FoxPro, consulte Mensagens de erro listadas numericamente. Para saber o que fazer quando ocorrerem erros durante o processamento de relatórios, consulte Tratamento de erros durante execuções de relatórios.

> **Cuidado:** Além das mensagens acima, que podem aparecer se OutputPage for chamado com parâmetros incorretos, lembre-se de que OutputPage precisa dos recursos disponíveis para o relatório mesmo quando chamado após o término da execução. Por exemplo, se um arquivo de imagem usado no relatório estiver incorporado ao aplicativo chamador, uma chamada a OutputPage de um PreviewContainer precisará acessar esse arquivo. Embora nenhuma mensagem de erro seja gerada, a saída ficará incompleta se você descarregar o aplicativo do qual o comando REPORT FORM ou LABEL foi emitido.

# Exemplos

### Exemplo 1: OutputPage no modo de uma página por vez para arquivos de imagem das páginas de saída

Este código de exemplo cria um documento TIFF de várias páginas a partir de um relatório. Ele usa a capacidade nativa de ReportListener de especificar o parâmetro nDeviceType de OutputPage como `101` para criar um arquivo TIFF, seguido de chamadas adicionais com eDeviceType igual a `201` para acrescentar páginas ao documento. Essa classe derivada de ReportListener usa ListenerType 2; portanto, o código nativo chama OutputPage ao preparar cada página.

> **Dica:** A capacidade nativa da classe ReportListener de fornecer imagens de páginas como diversos tipos de arquivo limita-se a algumas configurações padrão de cada tipo. Para TIFFs, ReportListener fornece arquivos compactados por desempenho. Contudo, você não está limitado às configurações da implementação nativa. É possível fornecer a ReportListener um identificador gráfico GDI+ e solicitar, no método OutputPage, que ele renderize uma página nesse dispositivo. Em seguida, salve o resultado em um arquivo de imagem com especificações não padrão. O Visual FoxPro fornece uma biblioteca de classes para esta e outras tarefas relacionadas a GDI+. Para obter mais informações, consulte Classes Base de Encapsulamento da API GDI Plus.

```foxpro
#define OutputNothing -1
#define OutputTIFF 101
#define OutputTIFFAdditive (OutputTIFF+100)
LOCAL oReportListener
oReportListener = NEWOBJECT("MPTiffListener")
oReportListener.Filename = "Multi"
WAIT WINDOW "Processing report to TIFF file...." NOWAIT
REPORT FORM ? OBJECT oReportListener
WAIT CLEAR
DEFINE CLASS MPTiffListener AS ReportListener
   PROCEDURE Init
      THIS.AddProperty("Filename", "temp")
      THIS.ListenerType = 2
   ENDPROC

   PROCEDURE BeforeReport
      ERASE THIS.Filename
   ENDPROC
   PROCEDURE OutputPage(nPageNo, eDevice, nDeviceType)
      IF (nDeviceType == OutputNothing)
         IF (nPageNo == 1)
             nDeviceType = OutputTIFF
         ELSE
            nDeviceType = OutputTIFFAdditive
         ENDIF
         THIS.OutputPage(nPageNo, THIS.Filename, nDeviceType)
         NODEFAULT
     ENDIF
   ENDPROC
ENDDEFINE
```

### Exemplo 2: OutputPage no modo de uma página por vez repetindo a saída na tela

Este exemplo substitui a saída repetida na tela dos relatórios compatíveis com versões anteriores quando NOCONSOLE não é usado no comando REPORT FORM. Ele usa a capacidade de OutputPage de gravar em um identificador Graphics GDI+. Se REPORT FORM especificar NOCONSOLE, o objeto ReportListener não fornecerá saída para a tela.

Por padrão, este ReportListener usa ListenerType 2; portanto, chama OutputPage ao preparar cada página, mas não tem resultado de saída nativo. Ele avalia os valores da propriedade CommandClauses para verificar NOCONSOLE e o destino de saída especificado pelo usuário. Se o usuário escolher gerar saída para uma impressora, arquivo ou visualização, a classe ajustará o comportamento para corresponder às versões anteriores.

```foxpro
#DEFINE OUTPUTDEVICETYPE_GDIPLUS 1
#DEFINE OUTPUTTO_PRINT           1
#DEFINE OUTPUTTO_FILE            2
#DEFINE LISTENER_TYPE_PRN        0
#DEFINE LISTENER_TYPE_PRV        1
#DEFINE LISTENER_TYPE_PAGED      2
LOCAL loRL, loForm
loRL = CREATEOBJECT("EchoListener")
REPORT FORM ? OBJECT loRL && output to the console
REPORT FORM ? OBJECT loRL NEXT 1 TO PRINT && output to console and print
_SCREEN.Cls && clear screen
REPORT FORM ? OBJECT loRL PREVIEW && to preview only, no console output
loForm = CREATEOBJECT("form")
loForm.Caption = "My Output Window"
loForm.Show()
REPORT FORM ? OBJECT loRL TO FILE c:\temp\x.txt && to file and output window
REPORT FORM ? OBJECT loRL TO FILE c:\temp\x.txt NOCONSOLE && to file only
DEFINE CLASS EchoListener as ReportListener
  ListenerType = LISTENER_TYPE_PAGED
  GP = 0
  RHeight = 0
  RWidth = 0

  PROCEDURE LoadReport()
    IF THIS.CommandClauses.Preview
       THIS.ListenerType = LISTENER_TYPE_PRV
    ELSE
       IF INLIST(THIS.CommandClauses.OutputTo,OUTPUTTO_PRINT,OUTPUTTO_FILE)
          THIS.ListenerType = LISTENER_TYPE_PRN
       ENDIF
    ENDIF
  ENDPROC

  PROCEDURE BeforeReport()
     IF NOT (THIS.CommandClauses.NoConsole OR THIS.CommandClauses.Preview)
        DECLARE integer GdipCreateFromHWND IN GDIPLUS.DLL ;
          integer hwnd, integer @ nGraphics
        LOCAL lH, nG
        nG = 0
        IF TYPE("_SCREEN.ActiveForm") = "O"
           m.lH = _SCREEN.ActiveForm.HWnd
        ELSE
           m.lH = _SCREEN.HWnd
        ENDIF
       IF GdipCreateFromHWND( m.lH, @nG ) = 0
          THIS.GP = m.nG
          THIS.RHeight = THIS.GetPageHeight()/10 && convert 960 DPI to 96 DPI
          THIS.RWidth = THIS.GetPageWidth()/10
       ENDIF
    ENDIF
  ENDPROC
  PROCEDURE OutputPage(nPageNo, ;
                  eDevice, ;
                  nDeviceType, ;
                  nleft, nTop, nWidth, nHeight, ;
                  nClipLeft,nClipTop, nClipWidth, nClipHeight)
      IF THIS.GP # 0
         DODEFAULT(nPageNo, THIS.GP,OUTPUTDEVICETYPE_GDIPLUS , ;
                   0,0,THIS.RWidth, THIS.RHeight, ;
                   0,0,THIS.RWidth, THIS.RHeight)
      ENDIF

  ENDPROC

  PROCEDURE UnloadReport()
     * reset:
     IF NOT THIS.GP = 0
        DECLARE integer GdipDeleteGraphics IN GDIPLUS.DLL integer
        GdipDeleteGraphics( THIS.GP )
        THIS.GP = 0
     ENDIF
     THIS.ListenerType = LISTENER_TYPE_PAGED
  ENDPROC

ENDDEFINE
```

### Exemplo 3: OutputPage no modo de todas as páginas de uma vez

Este exemplo usa ListenerType `3`; portanto, a classe nativa ReportListener não chama OutputPage enquanto prepara as páginas. Em vez disso, a classe derivada chama OutputPage após o término da execução do relatório e exibe a saída em um objeto simples de visualização contido em um formulário. Como mostra o exemplo, variando as dimensões do objeto de visualização, é possível controlar o nível de zoom com qualquer algoritmo ou restrição. Ao passar uma referência a esse objeto no método OutputPage, você informa ao código nativo o tamanho desejado para a página visualizada. O comportamento nativo de OutputPage dimensiona a saída adequadamente.

> **Dica:** Observe que o código encapsulador DoOutputPage desta classe verifica se a chamada externa ao método incluiu um número de página válido antes de chamar o código nativo de OutputPage, evitando erros.

```foxpro
#DEFINE BASEPAGEHEIGHT  550
#DEFINE BASEPAGEWIDTH 425
CLEAR ALL
oListener = NEWOBJECT("zoomListener")
oForm = CREATEOBJECT("form")
WITH oForm
   .ScaleMode = 3
   .allowOutput = .F.
   .top = 0
   .left = 0
   .height = BASEPAGEHEIGHT
   .width = BASEPAGEWIDTH
   .backcolor = RGB(255,255,255)
   .Show()
ENDWITH
oListener.PreviewContainer = oForm
REPORT FORM ? OBJECT oListener
oListener.DoOutputPage(1,1)
WAIT window  ;
   "Previewing at 100%... " + ;
   "press any key for the next preview zoom level"
oListener.DoOutputPage(2, .21123 )
WAIT window ;
   "Previewing at 21.123%... " + ;
   "press any key for the next preview zoom level"
oListener.DoOutputPage(3,2.367)
WAIT window ;
   "Previewing at 236.7%... "
DEFINE CLASS zoomListener AS ReportListener
   ListenerType = 3
   PROCEDURE DoOutputPage(tPage, tMultiplier)
      LOCAL liPage
      IF VARTYPE(tPage) = "N" AND ;
         BETWEEN(tPage,;
                 THIS.CommandClauses.RangeFrom, ;
                 IIF(THIS.CommandClauses.RangeTo=-1, ;
                     THIS.PageTotal, ;
                     THIS.CommandClauses.RangeTo))
         liPage = INT(tPage)
      ELSE
         liPage = THIS.CommandClauses.RangeFrom
      ENDIF
      THIS.SetPreview(tMultiplier)
      THIS.OutputPage(liPage,THIS.PreviewContainer.MyPreview,2)
   ENDPROC
   PROCEDURE SetPreview(tMultiplier)
      LOCAL liHeight, liWidth
      IF TYPE("THIS.PreviewContainer.MyPreview") # "O"
         THIS.PreviewContainer.AddObject("MyPreview","shape")
      ENDIF
      IF VARTYPE(tMultiplier) = "N" AND ;
         BETWEEN(tMultiplier,.01, 10)
         liHeight = BASEPAGEHEIGHT * tMultiplier
         liWidth  = BASEPAGEWIDTH * tMultiplier
         WAIT WINDOW ;
            "H:" + TRANSFORM(liHeight)+ ;
          ", W:" + TRANSFORM(liWidth) TIMEOUT 1
         * note that VFP will round the pixels
         WITH THIS.PreviewContainer
            .LockScreen = .T.
            .MyPreview.Height = liHeight
            .MyPreview.Width = liWidth
            .Height = liHeight
            .Width = liWidth
            .LockScreen = .F.
            .Cls()
         ENDWITH
      ENDIF
   ENDPROC
   PROCEDURE Destroy
      THIS.PreviewContainer = NULL
   ENDPROC
ENDDEFINE
```
