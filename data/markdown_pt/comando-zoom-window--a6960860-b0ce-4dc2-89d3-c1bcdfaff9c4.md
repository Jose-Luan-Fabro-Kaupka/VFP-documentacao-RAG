# Comando ZOOM WINDOW

Altera o tamanho e a posição de uma janela definida pelo usuário ou de uma janela de sistema do Visual FoxPro.

```foxpro
ZOOM WINDOW WindowName MIN | MAX | NORM
   [AT nRow1, nColumn1 | FROM AT nRow1, nColumn1
   [SIZE AT nRow2, nColumn2 | TO nRow2, nColumn2]]
```

#### Parâmetros
 **WindowName**
Especifica o nome da janela cujo tamanho você deseja alterar.
**MIN**
Reduz a janela ao tamanho mínimo. No Visual FoxPro for Windows, a janela é reduzida a um ícone. Todas as janelas de sistema podem ser reduzidas ao tamanho mínimo no Visual FoxPro for Windows. Janelas de sistema do Visual FoxPro devem estar abertas na janela principal do Visual FoxPro ou em uma janela definida pelo usuário antes de poderem ser minimizadas. Uma janela definida pelo usuário pode ser minimizada depois de definida. Ela não precisa ser ativada antes de você alterar seu tamanho.
**MAX**
Expande uma janela para preencher a janela principal do Visual FoxPro, a área de trabalho do Windows ou uma janela definida pelo usuário. Se uma janela filha for colocada em uma janela pai e a janela filha for maximizada, ela preenche a janela pai. Se alguma das cláusulas adicionais de ZOOM WINDOW (AT, SIZE, TO ou FROM) for incluída com MAX, MAX é ignorado. Apenas janelas definidas pelo usuário definidas com ZOOM podem ser expandidas ao tamanho máximo.
**NORM**
Retorna uma janela ao tamanho original depois que ela foi minimizada ou maximizada. NORM também pode ser usado para mover uma janela sem alterar seu tamanho. Use ZOOM WINDOW NORM sem cláusulas adicionais para retornar uma janela minimizada ou maximizada ao tamanho e localização originais.
**AT nRow1 , nColumn1 | FROM nRow2 , nColumn2**
Você pode especificar o posicionamento de uma janela incluindo a cláusula AT ou FROM. ZOOM WINDOW WindowName NORM AT AT nRow1 , nColumn1 restaura uma janela minimizada ou maximizada ao tamanho original e a posiciona no local específico. As coordenadas AT nRow1 , nColumn1 especificam onde o canto superior esquerdo da janela é posicionado. A localização de uma janela também pode ser alterada com MOVE WINDOW. No Visual FoxPro for Windows, se NORM for incluído, o canto superior esquerdo da janela é posicionado na janela principal do Visual FoxPro no local especificado com AT nRow1 , nColumn1. Se MIN for incluído, AT e FROM são ignorados e a janela é exibida como um ícone na parte inferior da janela principal do Visual FoxPro. Se MAX for incluído, AT e FROM são ignorados e a janela é expandida para preencher a janela principal do Visual FoxPro. No Visual FoxPro for Windows, se a janela for criada com a cláusula IN DESKTOP, o canto superior esquerdo da janela é posicionado na área de trabalho do Windows no local especificado com AT nRow1 , nColumn1. Se MIN for incluído, AT e FROM são ignorados e a janela é exibida como um ícone na parte inferior da área de trabalho do Windows. Se MAX for incluído, AT e FROM são ignorados e a janela é expandida para preencher a área de trabalho do Windows.
**SIZE AT nRow2 , nColumn2 | TO nRow2 , nColumn2**
Você também pode especificar um tamanho de janela incluindo SIZE ou TO. Se SIZE for incluído, o tamanho da janela é nRow2 linhas de altura e nColumn2 colunas de largura. Se a cláusula TO for incluída, o canto superior esquerdo da janela permanece em sua posição atual e o canto inferior direito da janela é posicionado na posição especificada com nRow2 , nColumn2.

# Observações

No Visual FoxPro for Windows, janelas podem ser reduzidas ao tamanho mínimo, ampliadas para preencher toda a janela principal do Visual FoxPro ou dimensionadas em qualquer ponto intermediário.

Se você criar uma janela definida pelo usuário com DEFINE WINDOW e a cláusula IN DESKTOP no Visual FoxPro for Windows, a janela criada pode ser ampliada para preencher toda a área de trabalho.

No Visual FoxPro for Windows, janelas podem ser ampliadas diretamente do tamanho mínimo ao máximo e vice-versa.

Ao ampliar uma janela, você pode especificar onde posicionar a janela redimensionada na janela principal do Visual FoxPro ou em uma janela definida pelo usuário.

Para ampliar uma janela de sistema, coloque o nome completo da janela de sistema entre aspas. Por exemplo, para maximizar a janela Command, emita o seguinte comando:

```foxpro
ZOOM WINDOW 'Command Window' MAX
```

Você pode usar ZOOM WINDOW para redimensionar todas as janelas de sistema.

# Exemplo

No exemplo a seguir, uma janela Browse é aberta para a tabela `customer`. A janela Browse é minimizada. A janela Browse é então retornada ao tamanho padrão. Em seguida, é minimizada novamente em um local específico. A janela Browse é então ampliada para um tamanho específico e maximizada.

```foxpro
CLEAR ALL
CLEAR
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\Testdata')
USE customer  && Opens Customer table
BROWSE NORMAL NOWAIT
IF _DOS OR _WINDOWS
   ZOOM WINDOW customer MIN
   WAIT WINDOW TIMEOUT 3 ;
      'MIN clause - This window will timeout. Please wait.'
ENDIF
ZOOM WINDOW customer NORM
WAIT WINDOW TIMEOUT 3 ;
   'NORM clause - This window will timeout. Please wait.'
IF _DOS OR _WINDOWS
   ZOOM WINDOW customer MIN AT 10,10
   WAIT WINDOW TIMEOUT 3 ;
      'MIN AT 10,10 clause - This window will timeout. Please wait.'
ENDIF
ZOOM WINDOW customer NORM AT 1,1 SIZE 22,25
WAIT WINDOW TIMEOUT 3 ;
   'NORM & SIZE clauses - This window will timeout. Please wait.'
ZOOM WINDOW customer NORM FROM 10,10 TO 22,70
WAIT WINDOW TIMEOUT 3 ;
   'NORM & TO clauses - This window will timeout. Please wait.'
ZOOM WINDOW customer MAX
WAIT WINDOW TIMEOUT 3 'MAX clause - This window will timeout. Please wait.'
CLEAR ALL
```
