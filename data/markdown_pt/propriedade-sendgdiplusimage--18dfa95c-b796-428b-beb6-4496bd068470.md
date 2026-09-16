# Propriedade SendGDIPlusImage

Especifica se o ReportListener receberá um identificador para a origem da imagem quando ela for carregada por uma referência de objeto ou de um campo General. Não se aplica a imagens carregadas por nome de arquivo.

```foxpro
ReportListener.SendGDIPlusImage Property [= iExpr]
```

# Valor de retorno

Tipo de dados Integer.

Observe que a propriedade é definida como tipo inteiro, e não lógico, para permitir a possibilidade de uma classe derivada usar outros valores inteiros para representar o fornecimento da imagem de outras maneiras além de um identificador gráfico. Por exemplo, uma classe derivada pode reconhecer o valor 2 para indicar "carregar todas as imagens baseadas em arquivo de seus arquivos originais e copiá-las para outro local ou formato".

A lista a seguir apresenta os valores de iExpr reconhecidos pela classe base ReportListener.
 **0 ou qualquer valor inteiro negativo**
(0 é o padrão) A classe base ReportListener não fornece às classes derivadas um identificador para imagens GDI+ no método Render.
**1 e valores inteiros superiores**
A classe base ReportListener fornece às classes derivadas um identificador para imagens GDI+ no método Render.

# Observações

Aplica-se a: objeto ReportListener.

O valor desta propriedade não tem significado para objetos da classe base ReportListener; ele não afeta os recursos nativos de renderização de impressão e visualização. No entanto, ReportListeners que fornecem outros tipos de saída podem definir a propriedade como 1 e receber um identificador para o objeto gráfico que representa imagens renderizadas provenientes de campos General ou da propriedade PictureVal de um controle Image, em vez de origens baseadas em arquivo.

Por padrão, por motivos de desempenho, essas informações não são fornecidas às classes derivadas.

> **Dica:** Quando você tem uma referência a um identificador gráfico GDI+, usa a API GDI+ para manipulá-lo. O Visual FoxPro é fornecido com várias Foundation Classes destinadas a facilitar o uso da API GDI+. Para obter mais informações, consulte Classes básicas de encapsulamento da API GDI Plus.

O valor desta propriedade não afeta o tratamento de imagens baseadas em arquivo pelo ReportListener. As classes derivadas recebem o nome de arquivo apropriado como argumento para o método Render, portanto, nenhum outro identificador é necessário.

# Exemplo

O fragmento de código a seguir, que mostra três métodos de ReportListener, é semelhante aos métodos internos da classe derivada XMLDisplayListener. Consulte Classe básica ReportListener com estilo de exibição XML para obter mais informações sobre essa classe e sobre como ela trata imagens.

No evento BeforeReport, o código deste exemplo salva o valor atual de SendGDIPlusImage. Em seguida, verifica se o relatório contém algum campo General. Se encontrar referências a imagens nas informações de layout, ele define SendGDIPlusImage como 1 durante o relatório.

```foxpro
#DEFINE LISTENER_SEND_GDI_IMAGE_HANDLE 1
PROCEDURE BeforeReport()
   THIS.oldSendGDIPlusImage = THIS.SendGDIPlusImage
   IF (THIS.SendGDIPlusImage < LISTENER_SEND_GDI_IMAGE_HANDLE) ;
        AND THIS.checkReportForGeneralFields()
     THIS.SendGDIPlusImage =   LISTENER_SEND_GDI_IMAGE_HANDLE
   ENDIF
   DODEFAULT()
ENDPROC
PROCEDURE checkReportForGeneralFields()
   LOCAL liGeneralFields, llOpened
   THIS.SetFRXDataSession()
   IF USED("FRX")
      * check,because
      * the method might be called
      * in the LoadReport() as well as BeforeReport()
      SELECT FRX
   ELSE
      USE (THIS.CommandClauses.File) SHARED NOUPDATE ALIAS FRX IN 0
      SELECT FRX
      llOpened = .T.
   ENDIF
   COUNT FOR ObjType = FRX_OBJTYP_PICTURE  AND  ;
            Offset =  FRX_PICTURE_SOURCE_GENERAL TO ;
            liGeneralFields
   IF llOpened
      USE IN FRX
   ENDIF
   THIS.SetCurrentDataSession()
   RETURN ( liGeneralFields > 0 )
ENDPROC
PROCEDURE AfterReport()
   DODEFAULT()
   THIS.SendGDIPlusImage = THIS.oldSendGDIPlusImage
ENDPROC
```
