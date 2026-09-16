# Exemplo Criar uma janela de forma irregular

Arquivo: ...\Samples\Solution\Toledo\Irregular.scx

A janela principal do Visual FoxPro e quaisquer formulários que você cria têm áreas de cliente de forma retangular por padrão. Para alterar a forma, você pode usar a função Windows API SetLayeredWindowAttributes, que define a opacidade e a chave de cor de transparência de uma janela em camadas. SetLayeredWindowAttributes é suportada no Microsoft Windows 2000 e Windows XP.

# Declarações de funções da API Windows

Neste exemplo, o evento Init do formulário contém as seguintes declarações para as funções de API necessárias:

```foxpro
DECLARE INTEGER SetLayeredWindowAttributes IN win32api;
      INTEGER HWND, INTEGER crKey, INTEGER bAlpha, INTEGER dwFlags
DECLARE INTEGER SetWindowLong IN user32.DLL ;
   INTEGER hWnd, INTEGER nIndex, INTEGER dwNewLong
DECLARE INTEGER GetWindowLong IN user32.DLL ;
   INTEGER hWnd, INTEGER nIndex
```

Para obter mais informações sobre o evento Init, consulte Init Event. Para obter informações detalhadas sobre essas declarações e funções, consulte MSDN online em http://msdn.microsoft.com.

# Exibir janelas de forma irregular

Você pode exibir um formulário não retangular usando a função SetLayeredWindowAttributes e definindo uma cor transparente. Formas desenhadas com essa cor aparecem transparentes. Além disso, quaisquer cliques do mouse nessas formas passam para o formulário visível.

Essa funcionalidade é suportada apenas no Microsoft Windows 2000 e Windows XP, mas é mais eficiente que técnicas anteriores para definir uma região delimitadora no formulário. Embora essa técnica torne um formulário transparente, o formulário deve ser configurado corretamente para funcionar com essa funcionalidade.

### Para configurar o formulário
- No formulário, defina a propriedade ShowWindow do Form como 2 (As Top-Level Form) para tornar possível desenhar uma janela em camadas.
- Desative a moldura da janela porque ela não é desenhada quando transparente definindo as seguintes propriedades para o formulário: BorderStyle = 0 Caption = "" Closable = .F. ControlBox = .F. TitleBar = 0
- No método MakeIrregular do exemplo, defina as áreas magenta, conforme especificado pela variável nColor, como transparentes usando o seguinte código: * Obtém sinalizadores existentes da janela. lnFlags = GetWindowLong(nHWND, GWL_EXSTYLE) ThisForm.nFlags = lnFlags * Anexa sinalizador Layered aos sinalizadores existentes. lnFlags = BITOR(lnFlags, WS_EX_LAYERED) * Define novos sinalizadores na janela. SetWindowLong(nHWND, GWL_EXSTYLE, lnFlags) SetLayeredWindowAttributes(nHWND, nColor, 0, LWA_COLORKEY)

Para obter mais informações, consulte Form Designer, Creating Forms e Propriedade ShowWindow.
