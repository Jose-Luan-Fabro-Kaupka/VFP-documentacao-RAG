# Comando MODIFY WINDOW

Modifica uma janela definida pelo usuário ou a janela principal do Visual FoxPro.

```foxpro
MODIFY WINDOW WindowName | SCREEN
[FROM nRow1, nColumn1 TO nRow2, nColumn2
   | AT nRow3, nColumn3 SIZE nRow4, nColumn4]
   [FONT cFontName [, nFontSize [, nFontCharSet]]] [STYLE cFontStyle]
   [TITLE cTitleText] [HALFHEIGHT] [DOUBLE | PANEL | NONE | SYSTEM]
   [CLOSE | NOCLOSE] [FLOAT | NOFLOAT] [GROW | NOGROW]
   [MINIMIZE | NOMINIMIZE] [ZOOM | NOZOOM] [ICON FILE FileName1]
   [FILL FILE FileName2]
   [COLOR SCHEME nSchemeNumber | COLOR ColorPairList]
```

#### Parâmetros
 **WindowName**
Especifica qual janela definida pelo usuário modificar. A janela que você especificar deve primeiro ser criada com DEFINE WINDOW.
**SCREEN**
Especifica a janela principal do Visual FoxPro como a janela a modificar. Não abrevie SCREEN ou o Visual FoxPro gerará uma mensagem de erro. Para retornar a janela principal do Visual FoxPro à sua configuração de inicialização, emita o seguinte comando sem cláusulas adicionais: MODIFY WINDOW SCREEN Dica Use MODIFY WINDOW SCREEN NOCLOSE para evitar encerrar o Visual FoxPro prematuramente por acidente.

Para obter mais informações sobre as cláusulas do MODIFY WINDOW, consulte DEFINE WINDOW Command.

# Observações

MODIFY WINDOW altera os atributos de uma janela definida pelo usuário existente (uma janela criada com DEFINE WINDOW) ou da janela principal do Visual FoxPro. MODIFY WINDOW não pode ser usado para alterar os atributos de janelas do sistema do Visual FoxPro (como a janela Command e a janela Browse).

Use MODIFY WINDOW para alterar a localização, a fonte padrão, o título, a borda, os controles, o ícone, o papel de parede e a cor de uma janela definida pelo usuário ou da janela principal do Visual FoxPro. Você pode alterar qualquer um desses atributos incluindo as cláusulas opcionais do comando MODIFY WINDOW. (Observe que, se você alterar as cores, deve usar CLEAR para aplicar as alterações de cor.)

Por exemplo, inclua as cláusulas FROM e TO ou AT e SIZE para especificar uma nova localização ou tamanho para uma janela definida pelo usuário ou para a janela principal do Visual FoxPro. Para impedir que uma janela definida pelo usuário ou a janela principal do Visual FoxPro seja movida, inclua a palavra-chave NOFLOAT.

# Exemplo

O exemplo a seguir altera o conteúdo da barra de título da janela principal do Visual FoxPro.

```foxpro
MODIFY WINDOW SCREEN TITLE 'My Application'
```
