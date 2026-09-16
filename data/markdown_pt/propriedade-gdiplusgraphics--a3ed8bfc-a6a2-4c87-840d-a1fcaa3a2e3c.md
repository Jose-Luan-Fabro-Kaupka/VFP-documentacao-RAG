# Propriedade GDIPlusGraphics

Fornece acesso ao objeto GDIPlus Graphics que o ReportListener usa para tratar a saída.

```foxpro
ReportListener.GDIPlusGraphics
```

# Valor de retorno

Tipo de dados Integer.

O padrão é 0. Esta propriedade é somente leitura.

# Observações

Aplica-se a: ReportListener Object.

Esta propriedade dá a classes derivadas baseadas em ReportListener uma forma de injetar sua própria saída no fluxo de saída, acessando o handle da classe base ReportListener para este fluxo.

> **Importante:** Quando código escrito em Visual FoxPro acessa este handle, ele deve DECLARE e usar funções baseadas na mesma cópia de arquivo de GDIPLUS.DLL que o produto usa em código nativo. Para garantir isso, use a sintaxe IN GDIPLUS.DLL sem caminho explícito em suas instruções DECLARE DLL.

O Visual FoxPro inclui várias Foundation Classes projetadas para facilitar o uso da API GDI+. Para obter mais informações, consulte GDI Plus API Wrapper Foundation Classes.

# Exemplo

Este exemplo ajusta todo o texto na banda Page Header de um relatório rotacionando-o em um ângulo, semelhante a um conjunto inclinado de cabeçalhos em uma planilha. Essa abordagem é útil quando você tem um relatório com muitas colunas e os rótulos de cada cabeçalho de coluna ocupariam muito mais espaço do que o conteúdo de cada coluna requer na banda Detail.

```foxpro
LOCAL oListener
oListener = CREATEOBJECT("rotateText")
oListener.ListenerType = 1
REPORT FORM ? OBJECT oListener
#define FRX_OBJCOD_PAGEHEADER 1
DEFINE CLASS rotateText AS ReportListener
   IsInPageHeader = .F.
   PROCEDURE Init()
      DECLARE integer GdipRotateWorldTransform In GDIPlus.Dll ;
            integer graphics,single angle,integer enumMatrixOrder_order
      DECLARE integer GdipTranslateWorldTransform In GDIPlus.Dll ;
            integer graphics,single dx,single dy,;
            integer enumMatrixOrder_order
      DECLARE integer GdipSaveGraphics IN GDIPlus.DLL ;
          integer graphics, integer @xx
      DECLARE integer GdipRestoreGraphics IN GDIPlus.DLL ;
          integer graphics, integer xx
   ENDPROC
   PROCEDURE BeforeBand(nBandObjCode, nFRXRecNo)
      DODEFAULT(nBandObjCode, nFRXRecNo)
      IF (nBandObjCode = FRX_OBJCOD_PAGEHEADER)
         THIS.IsInPageHeader = .T.
      ENDIF
   ENDPROC
   PROCEDURE AfterBand(nBandObjCode, nFRXRecNo)
      IF (nBandObjCode = FRX_OBJCOD_PAGEHEADER)
         THIS.IsInPageHeader = .F.
      ENDIF
      DODEFAULT(nBandObjCode, nFRXRecNo)
   ENDPROC
   PROCEDURE Render(nFRXRecNo, nLeft, nTop, nWidth, nHeight,;
       nObjectContinuationType, cContentsToBeRendered, GDIPlusImage)
      LOCAL xx,x,y, z
      xx = 0
      IF THIS.IsInPageHeader
         * get appropriate versions of coords
         x = nLeft
         y = nTop
         * save the current state of the graphics handle
         z = GdipSaveGraphics(this.GDIPlusGraphics, @xx)
         * now move the 0,0 point to where we'd like it to be
         * so that when we rotate we're rotating around the
         * appropriate point
         z = GdipTranslateWorldTransform(this.GDIPlusGraphics,x,y,0)
         * should check z here -- will be 0 if no error occurred
         * now change the angle at which the draw will occur
         z = GdipRotateWorldTransform ( this.GDIPlusGraphics,-20,0)
         * should check z as above
         * restore the 0,0 point
         z = GdipTranslateWorldTransform(this.GDIPlusGraphics,-x,-y, 0)
         * should check z as above
      ENDIF
      * explicitly call the baseclass behavior
      * when we are ready for it
      DODEFAULT(nFRXRecNo, nLeft, nTop, nWidth, nHeight, ;
               nObjectContinuationType, cContentsToBeRendered, ;
               GDIPlusImage)
      * put back the state of the graphics handle
      IF THIS.IsInPageHeader
         GdipRestoreGraphics(this.GDIPlusGraphics, xx)
      ENDIF
      * don't let the baseclass render
      * when and how it would otherwise do it
      NODEFAULT
   ENDPROC
ENDDEFINE
```
