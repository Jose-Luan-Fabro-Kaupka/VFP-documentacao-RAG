# Guia Style, caixa de diálogo Report Control Properties (Report Builder)

Permite definir opções de estilo para controles de relatório no Report Designer ou Label Designer. À medida que você altera as configurações de estilo para o controle de relatório, pode visualizar essas alterações na área Sample.

> **Observação:** Esta guia complementa a funcionalidade fornecida pelo menu Format do Visual FoxPro Report Designer quando o Report Builder está ativo. Alguns recursos ainda estão disponíveis somente no menu Format.
 - How to: Change Line Styles of Report Controls
- How to: Change Colors in Report Controls
- How to: Change Font Settings in Report Controls
- How to: Change Opacity of Report Controls

# Font

(Somente controles Label e Field) Especifica as configurações de fonte para controles de texto. Clicar no botão de reticências (…) abre a caixa de diálogo Font para que você possa selecionar uma fonte diferente.
 **Use Font Script**
Indica que o script de fonte de idioma especificado na caixa de combinação Script da caixa de diálogo Font será salvo com o relatório. Quando você seleciona uma fonte padrão na caixa de diálogo Font, a seleção de script de fonte será salva por padrão. Você pode optar por não salvar a seleção específica de script de fonte com o layout desmarcando esta caixa de seleção. Para obter mais informações, consulte Font Dialog Box .
**Strikethrough**
Especifica que o texto de saída do controle será riscado com uma linha horizontal.
**Underline**
Especifica que o texto de saída do controle será sublinhado.

# Pen style

(Somente controles Line e Rectangle) Permite alterar opções de renderização para formas e linhas.
 **Style**
Especifica o estilo de linha para um controle de relatório Line ou Rectangle.
**Weight**
Especifica a largura da linha para um controle de relatório Line ou Rectangle. Observação Qualquer seleção de estilo de linha diferente de Normal (linha sólida) forçará uma espessura de linha de 1 ponto e esta opção será desabilitada.
**Curvature**
(Somente controles Rectangle) Especifica a curvatura de um controle Rectangle/Shape. 0-98 são graus variados de arredondamento, e 99 resulta em uma forma oval em vez de um retângulo. Uma configuração de curvatura de 16 é o padrão para um novo controle Rounded Rectangle. Para obter mais informações, consulte Curvature Property .

# Color

Especifica configurações de cor para o controle de relatório.
 **Use default foreground (pen) color**
Especifica se deve usar a cor de primeiro plano padrão. Desmarcar esta caixa de seleção permite clicar no botão de reticências ( … ) para abrir a caixa de diálogo Color Picker.
**Use default background (fill) color**
Especifica se deve usar a cor de fundo padrão. Desmarcar esta caixa de seleção permite clicar no botão de reticências ( … ) para abrir a caixa de diálogo Color Picker.

# Backstyle

Especifica se objetos que aparecem atrás de um controle de relatório são visíveis.

> **Importante:** Controles Rectangle respeitam Backstyle somente se tiverem sido atribuídos a um Fill Pattern . Retângulos vazios são sempre transparentes, e retângulos sólidos são sempre opacos.
 **Opaque**
Especifica que objetos que aparecem atrás do controle de relatório não são visíveis.
**Transparent**
Especifica que objetos que aparecem atrás do controle de relatório são visíveis.

# Sample

Exibe um exemplo aproximado das opções de estilo selecionadas à medida que você faz alterações.
