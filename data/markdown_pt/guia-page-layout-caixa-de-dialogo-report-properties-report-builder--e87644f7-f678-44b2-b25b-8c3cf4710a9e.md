# Guia Page Layout, Caixa de diálogo Report Properties (Report Builder)

Permite especificar configurações para o layout de página do relatório ou etiqueta.

A guia Page Setup exibe uma representação gráfica da página, que reflete seu layout no Report Designer ou Label Designer.

Esta guia é pré-selecionada quando você escolhe Page Setup no menu File; Properties no menu Report ou no menu de contexto do layout do relatório.

> **Observação:** Esta guia substitui a funcionalidade da caixa de diálogo nativa Report Page Setup Dialog Box do Visual FoxPro quando o Report Builder está ativo.
 - How to: Define Columns in Reports
- How to: Change Page Settings for Reports
- How to: Save the Printer Environment for Reports

# Columns

Especifica opções para colunas no layout de página.
 **Number**
Especifica o número de colunas a imprimir na página.
**Width**
Especifica a largura do layout dentro de uma coluna.
**Spacing**
Especifica o espaço entre colunas, quando várias colunas foram especificadas.
**Left margin**
Especifica a largura da margem esquerda. Aumentar este valor reduzirá proporcionalmente a largura do layout.

# Print area

Especifica opções para a área de impressão na página.
 **Printable page**
Especifica que o layout usa as dimensões de página imprimível da impressora atual. A impressão começa imediatamente após a área de margem não imprimível.
**Whole page**
Especifica que os atributos de tamanho físico do papel da impressora atual determinam as dimensões do layout. Observação Para impressoras que têm uma área de impressão menor que o tamanho físico do papel, você precisará verificar seus layouts de relatório para garantir que a saída renderizada não seja truncada pela impressora.

# Column print order

Especifica se layouts de várias colunas são processados de cima para baixo ou da esquerda para a direita.
 **Top to bottom**
Imprime registros de cima para baixo (padrão).
**Left to right**
Imprime registros da esquerda para a direita. Também conhecido como "estilo de etiqueta".

# Default font

Exibe as configurações de fonte padrão para o relatório. Clicar no botão de reticências (…) abre a caixa de diálogo Font para que você possa selecionar uma fonte padrão diferente.
 **Use font script**
Indica que o conjunto de caracteres de idioma especificado na caixa Script da caixa de diálogo Font será salvo com o relatório. Quando você seleciona uma fonte padrão na caixa de diálogo Font, a seleção de script de fonte será salva por padrão. Você pode optar por não salvar a seleção específica de script de fonte com o layout desmarcando esta caixa de seleção. Para obter mais informações, consulte Font Dialog Box .

# Printer

Exibe o nome da impressora no ambiente de impressora do layout. Para relatórios recém-criados, esta será a seleção de impressora padrão atual do Visual FoxPro.
 **Page setup**
Abre a caixa de diálogo Page Setup para que você possa selecionar uma impressora alternativa e configurar configurações adicionais de página e impressora. Para obter mais informações, consulte Page Setup Dialog Box (Visual FoxPro) .
**Save printer environment**
Os ambientes de impressora são salvos com o layout por padrão. Desmarcar esta caixa de seleção garante que nenhuma informação de ambiente de impressora seja armazenada no arquivo FRX do layout.
