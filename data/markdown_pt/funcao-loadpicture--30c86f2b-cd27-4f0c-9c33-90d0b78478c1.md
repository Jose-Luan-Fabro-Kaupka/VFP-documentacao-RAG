# Função LOADPICTURE( )

Cria uma referência de objeto para um bitmap, ícone ou metafile do Windows.

```foxpro
LOADPICTURE([cFileName])
```

#### Parâmetros
 **cFileName**
Especifica o arquivo de imagem no disco para o qual um objeto é criado. Os seguintes tipos de imagem são suportados: Tipos de imagem suportados Grupos de tipos de imagem Extensões de nome de arquivo bitmaps .bmp, .jpg, .jpeg, .jpe, .jfif, .gif, .giff, .gfa icons .ico windows metafiles .wmf windows enhanced metafiles .emf cursor .cur The following restrictions (tested with VFP 9 SP2 and OlePro32.dll Version 6.0.6002.18005) exist: Limitações conhecidas Grupos de tipos de imagem Restrições e problemas bitmaps Loading these .tif and .png formats will cause an OLE error. icons Icons are allowed with sizes up to 128x128 and must not have more than 256 colors. Even if there is more than one icon stored in the icon file, always only the smallest icon gets displayed. The icon file may contain much more icons - even with more colors and larger sizes - as long as there is at least one that complies with the rules above, then no exception is thrown. cursor Cursor files must not have more than 1K of file size, otherwise an OLE error is generated. Cursor files containing 16 color cursors can be loaded flawlessly, but only monochrome output is supported. Loading an animated cursor (.ani) causes an OLE error to be raised. Suporte a imagem nula Se cFileName for omitido, a "imagem nula" é retornada. You can include GETPICT( ) as cFileName to display the Open dialog from which you can choose a bitmap file.

# Valor de retorno

Objeto

A função LOADPICTURE() retorna uma referência de objeto COM do tipo Picture that can be assigned to ActiveX controls and VFP’s Image object’s PictureVal property.
 No entanto, a interface primária real iPicture só pode ser recuperada usando código como este:

```foxpro
oIPicture = GETINTERFACE(LOADPICTURE(GETPICT()), "iPicture")
```

# Observações

Objetos Picture fornecem uma abstração independente de linguagem para bitmaps, ícones e metafiles.
 Como com o objeto de fonte padrão, o sistema fornece uma implementação padrão do objeto picture.
 Suas interfaces primárias são iPicture e iPictureDisp.
 Um objeto picture é criado com OleCreatePictureIndirect e suporta as interfaces iPicture e iPictureDisp.
 O objeto picture fornecido pelo OLE implementa a semântica completa das interfaces iPicture e iPictureDisp.
 In other words, there’s no need to use another interface than iPicture!

A função LOADPICTURE( ) encapsula internamente a função OleCreatePictureIndirect() implementada em OleAut32.dll.
 Thus, all you can read about that function (above and online) is also true for VFP’s LOADPICTURE() function.
 LOADPICTURE( ) Function was added to VFP’s vocabulary to make it easier to load images with COM interfaces that many presentation properties of ActiveX controls require for their settings.
 Por exemplo, o controle ActiveX Outline tem uma propriedade PictureOpen que requer uma referência de objeto COM de imagem para sua configuração.

O objeto COM retornado pela função LOADPICTURE( ) oculta sua interface primária iPicture.
 In contrast to the reference returnd by LOADPICTURE( ) Function, the OLE-image’s primary iPicture interface is the only fully functional one.
 Em outras palavras, somente iPicture pode ser usada em programas VFP sem gerar erros OLE.
 Como iPicture é um superconjunto de Picture, pode ser, melhor, deve ser usada em todos os lugares em vez da retornada pela função LOADPICTURE( )!

 Example #1 in the examples section below proves that it makes no difference which OLE image interface gets assigned to a oIMAGE.PICTUREVAL property.

O IID da interface iPicture é definido como “{7BF80980-BF32-101A-8BBB-00AA00300CAB}”.

```foxpro
oIPicture1 = GETINTERFACE(LOADPICTURE(), "iPicture")
oIPicture2 = CREATEOBJECTEX("StdPicture","","{7BF80980-BF32-101A-8BBB-00AA00300CAB}")
```

# Membros da interface

A tabela a seguir resume os PEMs da interface iPicture.

 Membros da interface iPicture
| PEM | Name | Usado para | ValorType | Leitura/Gravação |
| --- | --- | --- | --- | --- |
| property | Attributes | O conjunto atual dos atributos de bit da imagem. | DWORD (int) | somente leitura |
| property | CurDC | O contexto de dispositivo atual no qual esta imagem está selecionada. | HDC (long) | somente leitura |
| property | Handle | Handle da imagem gerenciada dentro deste objeto picture. | OLE_Handle (int) | somente leitura |
| property | Height | A altura atual da imagem no objeto picture. | OLE_XSIZE_HIMETRIC (long) | somente leitura |
| property | hPal | A paleta atual da imagem (se houver). | OLE_Handle (int) | leitura/gravação |
| property | KeepOriginalFormat | O valor atual da propriedade KeepOriginalFormat do objeto picture. | Bool | leitura/gravação |
| property | Type | O tipo atual da imagem. | Short (int) | somente leitura |
| property | Width | A largura atual da imagem no objeto picture. | OLE_XSIZE_HIMETRIC (long) | somente leitura |
| method | PictureChanged() | Notifica o objeto picture que seu recurso de imagem mudou. | | |
| method | Render() | Desenha a porção especificada da imagem no contexto de dispositivo especificado, posicionada no local especificado. | | |
| method | SaveAsFile() | Salva os dados da imagem em um fluxo no mesmo formato em que seria salva em um arquivo. | | |
| method | SelectPicture() | Seleciona uma imagem bitmap em um contexto de dispositivo determinado, retornando o contexto de dispositivo no qual a imagem estava previamente selecionada, bem como o handle da imagem. | | |

The Attributes property is said to hold the picture’s bit attributes. Actually, there are only two, which can be set alone, or additive. The following table lists both possible values:

 Enumeração iPicture.Attributes
| Constante | Descrição | Valor |
| --- | --- | --- |
| PICTURE_SCALABLE | O objeto picture é escalável, such that it can be redrawn with a different size than was used to create the picture originally. Metafile-based pictures are considered scalable; icon and bitmap pictures, while they can be scaled, do not express this attribute because both involve bitmap stretching instead of true scaling. | 1 |
| PICTURE_TRANSPARENT | O objeto picture contém uma imagem que tem áreas transparentes, such that drawing the picture will not necessarily fill in all the spaces in the rectangle it occupies. Metafile and icon pictures have this attribute; bitmap pictures do not. | 2 |

A tabela a seguir lista todos os valores possíveis da propriedade iPicture.Type:

 iPicture.Type Property Valors
| Constante | Descrição | Valor |
| --- | --- | --- |
| PICTYPE_UNINITIALIZED | O objeto picture está atualmente não inicializado. This value is never be returned within VFP . | -1 |
| PICTYPE_NONE | Um novo objeto picture deve ser criado sem um estado inicializado. This value is returned from VFP if LoadPicture() is used without a parameter . | 0 |
| PICTYPE_BITMAP | O tipo de imagem é bitmap. | 1 |
| PICTYPE_METAFILE | O tipo de imagem é metafile. | 2 |
| PICTYPE_ICON | O tipo de imagem é ícone. | 3 |
| PICTYPE_ENHMETAFILE | O tipo de imagem é enhanced metafile. | 4 |

The most interesting method of the COM image object’s iPicture interface is render() which also works flawlessly only when called on the iPicture interface.
A tabela a seguir resume os parâmetros do método render():

 Parâmetros do Render()
| Parameter | Usado para | Unidade de escala |
| --- | --- | --- |
| hdc | Um handle do contexto de dispositivo no qual renderizar a imagem. | |
| x | A coordenada horizontal em hdc na qual posicionar a imagem renderizada (posição X do canto superior esquerdo do retângulo de saída). | pixel |
| y | A coordenada vertical em hdc na qual posicionar a imagem renderizada (posição Y do canto superior esquerdo do retângulo de saída). | pixel |
| cx | A dimensão horizontal (largura) do retângulo de destino (largura do retângulo de saída). | pixel |
| cy | A dimensão vertical (altura) do retângulo de destino (altura do retângulo de saída). | pixel |
| xSrc | O deslocamento horizontal na imagem de origem a partir do qual iniciar a cópia. | HiMetric |
| ySrc | O deslocamento vertical na imagem de origem a partir do qual iniciar a cópia. | HiMetric |
| cxSrc | The horizontal extent to copy from the source picture (width of image source’s clipping region AND direction of readout). | HiMetric |
| cySrc | The vertical extent to copy from the source picture (height of image source’s clipping region AND direction of readout). | HiMetric |
| lprcWBounds | If hdc is a metafile device context, the lprcWBounds parameter points to a RECTL structure specifying the bounding rectangle in the underlying metafile. The rectangle structure contains the window extent and window origin. These values are useful for drawing metafiles. The rectangle indicated by lprcBounds is nested inside this lprcWBounds rectangle ; they are in the same coordinate space. If hdcDraw is not a metafile device context, lprcWBounds will be NULL. If hdcDraw is a metafile device context, lprcWBounds cannot be NULL! | |

O método retorna valores padrão como E_FAIL, E_INVALIDARG e E_OUTOFMEMORY, bem como S_OK, E_POINTER e CTL_E_INVALIDPROPERTYVALUE. Esses valores são descritos no MSDN.

# Aplicações

A função render tem muitos parâmetros. Alguns passam valores em pixels, outros valores HiMetric.
 O Exemplo #3 tem algumas conversões úteis, bem como outras funções e definições de suporte.

To figure out how render() works try the VFP code below; type it in line by line into VFP’s command window:

```foxpro
* locate an image with round about 100 x 100 pixels
goPic = LOADPICTURE(GETPICT())
gIP = GETINTERFACE(m.goPic, "iPicture")
goForm = CREATEOBJECT("Form")
goForm.Show()
* declare access to the _client_area_ of a window
DECLARE Integer GetDC IN USER32 integer HWnd
* hDC should be <> 0 (otherwise that's an error)!
hDC = GetDC(goForm.HWnd)
* render your image directly onto form's client area
gIP.Render(m.hDC,0,0,100,100,0,gIP.Height,gIP.Width,- gIP.Height,NULL)
* declare release function
DECLARE Integer ReleaseDC IN USER32 integer HWnd, integer hDC
* next line should print 1 on the form's background >> "Okay"
? ReleaseDC(m.goForm.HWnd, m.hDC)
* declare access to the _whole_ window
DECLARE Integer GetWindowDC IN USER32 integer HWnd
* hDC now references form's caption an border areas as well!
hDC = GetWindowDC(goForm.HWnd)
* render out partially overwriting form's border and caption
gIP.Render(m.hDC,0,0,100,100,0,gIP.Height,gIP.Width,- gIP.Height,NULL)
* never forget to free an allocated device context
? ReleaseDC(m.goForm.HWnd, m.hDC)
```

iPicture.Render() qualifica-se para pintar em regiões de formulário de outra forma inacessíveis, como TitleBar ou WindowBorders.
 Outra aplicação interessante para renderização direta decorre do fato de que nenhuma referência de objeto VFP é necessária para pintura.
 O método render() usa exclusivamente um handle comum do Windows. Assim, é possível renderizar em qualquer contexto de dispositivo conhecido.

 Se alguém encontrar o chamado problema do relógio de areia, trabalhar com uma imagem baseada em COM pode ser a solução alternativa preferida.
 O cursor do mouse em forma de relógio de areia é exibido pelo sistema operacional durante acessos longos ao disco.
 Às vezes o VFP não redefine corretamente o cursor do mouse em forma de relógio de areia.
 Thus, the user still sees the “busy working” icon although VFP already is idle, as long she doesn’t touch the mouse.
 Most often these disk accesses stem from refreshing pictures loaded into native Image-Objetos using the Image.Picture property.
 Storing a COM memory-based object to the Image-Objeto’s .PictureVal property instead, never causes any disk access.
 Assim, nenhum cursor de mouse em forma de relógio de areia aparecerá após uma atualização!

# Desvantagem

iPicture.Render() faz seu trabalho fora de — e sem ser notado por — o próprio mecanismo VFP.
 That’s why VFP has no idea of what was painted “between the lines”.
 Each time VFP refreshes the form’s area (we’ve just rendered our picture onto), will clear out our image.
 Para tornar a saída renderizada persistente, medidas devem ser tomadas contra o VFP apagá-la!

Há outro BUG do qual se deve estar ciente ao empregar a solução alternativa do relógio de areia descrita acima!

 Para ver o que acontece, experimente o código a seguir:

```foxpro
LOCAL lnLoop, oComPic1, oComPic2
oComPic1 = LOADPICTURE(GETFILE())
oComPic2 = LOADPICTURE(GETFILE())
TRY
	_Screen.Addobject("oImage","IMAGE")
CATCH
FINALLY
	_Screen.oImage.Visible = .T.
ENDTRY
FOR lnLoop = 1 to 100
	_Screen.oImage.PictureVal = m.oComPic1
	_Screen.oImage.PictureVal = m.oComPic2
NEXT
*//
*\\ whereas the next loop will break somewhere down the road:
FOR lnLoop = 1 to 100
	_Screen.oImage.PictureVal = m.oComPic1
	_Screen.oImage.PictureVal = m.oComPic1
	_Screen.oImage.PictureVal = m.oComPic1
	_Screen.oImage.PictureVal = m.oComPic2
NEXT
```

One can see, that the first loop executes flawlessly, the second one breaks after only a few loops with a “Property value is invalid” error message!
 Este bug é difícil de rastrear e ocorre somente quando alguém tenta atribuir a mesma referência COM mais de uma vez seguida!
 The workaround for this is to keep track which COM-reference is actually assigned to the Image’s PictureVal property.
 Nunca reatribua a mesma referência uma segunda vez (sobrescrevendo a primeira com uma cópia dela mesma)!
 BTW: It doesn’t matter what interface you are using.
 The error seems to stem from VFP’s Image class instance.

# Exemplos

The following example shows that both interfaces (Picture and IPicture) of a COM image instance can be assigned to VFP’s Image.PictureVal property:

```foxpro
PUBLIC goPic AS Objeto, goIPic AS Objeto
goPic = LOADPICTURE(GETPICT())
goIPic = GETINTERFACE(m.goPic, "iPicture")
_SCREEN.AddObjeto("oPic1","IMAGE")
_SCREEN.AddObjeto("oPic2","IMAGE")
WITH _SCREEN.oPic1
	.VISIBLE = .T.
	.PICTUREVAL = m.goPic && "Picture"-Interface
ENDWITH
WITH _SCREEN.oPic2
	.LEFT = 110
	.VISIBLE = .T.
	.PICTUREVAL = m.goIPic && "IPicture"-Interface
ENDWITH
HIDE WINDOWS ALL
WAIT WINDOW "Press any key..."
_SCREEN.RemoveObjeto("oPic1")
_SCREEN.RemoveObjeto("oPic2")
STORE NULL TO goPic, goIPic
CLEAR
SHOW WINDOWS ALL
```

O exemplo a seguir mostra como consultar a interface iPicture de uma instância COM de imagem.
Intencionalmente, não há seções Try…Catch…Endtry neste código de demonstração, para que erros OLE possam ocorrer.
Você deve executar o trecho de código várias vezes com diferentes tipos de imagem para vê-los.

```foxpro
goPic = LOADPICTURE(GETPICT())
IF VARTYPE(m.goPic) == "O"
	goIPic = GETINTERFACE(m.goPic, "iPicture")
	IF VARTYPE(m.goIPic) == "O"
		CLEAR && just some informal output:
		WITH m.goIPic
			?
			? "Properties of 'IPicture'-Interface:"
			? "Attributes"		,.Attributes
			*\\ next line will fail if an ICOn loaded
			? "CurDC"	,.CurDC
			? "Handle"	,.Handle
			? "Height"	,.Height
			*\\ next line will fail if an ICOn loaded
			? "hPal"	,.hPal
			? "KeepOriginalFormat",.KeepOriginalFormat
			? "Type"	,.Type
			? "Width"	,.Width
			?
		ENDWITH
	ENDIF
ENDIF
```

O código a seguir é uma coleção de funções e declarações de suporte úteis ao programar objetos de imagem OLE.

```foxpro
* Supporting Functions & DEFINEs
#DEFINE INCH2MILLIMETER 25.4 && 1 Inch = 25.4 millimeters
#DEFINE INCH2HIMETRICS (INCH2MILLIMETER * 100) && 1 HIMETRIC = 0.01
FUNCTION PXL2HIME(tnPixel AS Integer) AS Integer
	* Pixel to HiMetric conversion
	LOCAL lnPixelsOnOneHiMetricUnit AS Integer
	lnPixelsOnOneHiMetricUnit = INCH2HIMETRICS / GetDPI()
RETURN ROUND(lnPixelsOnOneHiMetricUnit * m.tnPixel, 0)
ENDFUNC
FUNCTION HIME2PXL(tnHimetric AS Integer) AS Integer
	* HiMetric to Pixel conversion
	LOCAL lnPixelsOnOneHiMetricUnit AS Integer
	lnPixelsOnOneHiMetricUnit = INCH2HIMETRICS / GetDPI()
RETURN ROUND(m.tnHimetric / m.lnPixelsOnOneHiMetricUnit, 0)
ENDFUNC
FUNCTION GetDPI(tnHDC AS Integer) AS Integer
      * retrieve dots per inch resolution
      * for VFP's _SCREEN device context
	DECLARE Integer GetDeviceCaps IN GDI32 integer hdc, integer nIndex
	DECLARE Integer GetWindowDC IN USER32 integer HWnd
	DECLARE Integer ReleaseDC IN USER32 integer HWnd, integer hDC
	* For simplicity, we assume X- and Y- dimensions
      * using the same DPI resolution.
	#DEFINE LOGPIXELSX 88 && Logical pixels/inch in X
      #DEFINE LOGPIXELSY 90 && Logical pixels/inch in Y
	* Get VFP's _Screen-hDC to calculate resolution:
	LOCAL lhDC AS Integer, lnDPI AS Integer
	STORE 0 TO lhDC, lnDPI
	lhDC = GetWindowDC(_Screen.HWnd)
	IF NOT m.lhDC = 0
		lnDPI = GetDeviceCaps(m.lhDC, LOGPIXELSX)
	ELSE
		lnDPI = 96 && default to 96 DPI
	ENDIF
	* Free device context
	= ReleaseDC(_Screen.HWnd, m.lhDC)
RETURN m.lnDPI
ENDFUNC
FUNCTION GetCanvas(tnHWND AS Integer, tlChild AS Boolean) AS Integer
	* Retrieve hDC (handle DeviceContext) of window handle
	* tlChild = TRUE  := Use GetDC()
	* tlChild = FALSE := Use GetWindowDC()
	DECLARE Integer GetDC IN USER32 integer HWnd
	DECLARE Integer GetWindowDC IN USER32 integer HWnd
	LOCAL lnHDC AS Integer
	IF m.tlChild
		lnHDC = GetDC(m.tnHWND)
	ELSE
		lnHDC = GetWindowDC(m.tnHWND)
	ENDIF
RETURN m.lnHDC
ENDFUNC
FUNCTION ReleaseCanvas(tnHWND AS Integer, tnHDC AS Integer) AS Integer
	* Releases a borrowed hDC
	DECLARE Integer ReleaseDC IN USER32 integer HWnd, integer hDC
RETURN ReleaseDC(m.tnHWND, m.tnHDC)
ENDFUNC
* The following function is not bullert-proof, as it fails on forms with scrollbars (oForm.Scrollbars > 0)
FUNCTION GetChildAreaCanvas(tnhWnd AS Integer) AS Integer
	* VFP ‘TopLevelForms’ (oForm.ShowWindow = 2) have
	* a secondary window inside the outer one.
	* This is also true for forms showing scrollbars!
	LOCAL lnVfpHANDLE AS Integer, lnClienthWnd AS Integer, lnHDC AS Integer
	* Convert the given Windows hWnd to an internal VFP WHANDLE
	lnVfpHANDLE = SYS(2326, m.tnhWnd)
	* Retrieve the Windows hWnd for a client window
	* (WCLIENTWINDOW) of a specified Visual FoxPro parent window
	lnClienthWnd = SYS(2325, m.lnVfpHANDLE)
	* Check if there is a WCLIENTWINDOW
	IF lnClienthWnd = lnVfpHANDLE
		* No such WCLIENTWINDOW, return child’s client area
		lnHDC = GetCanvas(m.tnhWnd, .T.)
	ELSE
		* There IS a WCLIENTWINDOW!
		* Get the device context handle for the
		* whole client area of that window:
		lnHDC = GetCanvas(lnClienthWnd)
	ENDIF
RETURN m.lnHDC
ENDFUNC
```
